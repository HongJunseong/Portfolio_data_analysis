import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import re
import unicodedata
import emoji


# 첫번째 게시물 클릭하는 함수
def select_first(driver):
    first = driver.find_element(By.CSS_SELECTOR, "div._aagw")
    first.click()
    time.sleep(5)


# 다음 게시글로 넘어가는 함수
def move_next(driver):
    right = driver.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh")
    right.click()
    time.sleep(3)



# 좋아요 갯수가 숫자가 아닐 때('여러명'이라고 표기) 추정하는 함수
def estimate_likes_from_comments_and_tags(comments_count, tags_count):
    # 댓글과 태그 수를 기반으로 좋아요를 추정
    estimated_likes = (comments_count * 5) + (tags_count * 2) + random.randint(1, 10)
    return estimated_likes



# LLM을 이용하여 게시글로부터 식당 정보를 추출하는 함수
# GPT-3.5 turbo 모델 사용
def extract_restaurant_info(content):

    api_key = 'YOUR API KEY' # OpenAI API Key 입력
    llm = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo", temperature=0.2)

    # 프롬프트 템플릿 작성
    prompt_template = """
    다음 텍스트에서 식당 이름과 지역 주소를 각각 추출해 주세요.
    출력 형식은 반드시 다음과 같아야 합니다:

    - 식당 이름: [식당 이름1]
    지역 주소: [지역 주소1]
    - 식당 이름: [식당 이름2]
    지역 주소: [지역 주소2]

    * 주소 정보가 없는 경우 "없음"이라고 표시해 주세요.

    텍스트: {content}
    """

    # PromptTemplate을 사용해 템플릿 정의
    template = PromptTemplate(input_variables=["content"], template=prompt_template)

    # LLMChain 설정
    llm_chain = LLMChain(prompt=template, llm=llm)

    # LLMChain을 통해 결과 생성
    result = llm_chain.predict(content=content)

    # 식당 이름이 여러 개 있는지 확인 (정확한 키워드 사용)
    restaurant_name = re.findall(r"식당 이름: (.*?)\n", result)

    # 식당 이름이 1개 초과인 경우 건너뛰기 (무분별한 추천 방지)
    if len(restaurant_name) > 1:
        return None  # 건너뛰기

    # 주소 추출
    address = re.findall(r"주소: (.*)", result)

    return [restaurant_name, address]


# 게시글 요소(좋아요 수, 내용, 댓글 등) 가져오기
def get_content(driver):
    try:
        # 본문 내용
        content_element = driver.find_element(By.CSS_SELECTOR, 'div._a9zr')
        content = content_element.text
        content = unicodedata.normalize('NFC', content)

        content = content.replace('\n', ' ')
        
        # 식당 정보 추출 (식당 이름과 주소)
        restaurant_info = extract_restaurant_info(content)
        if restaurant_info is None:
            return None
        else:
            restaurant_name = restaurant_info[0]
            restaurant_addr = restaurant_info[1]
            
    except Exception as e:
        content = ''
        restaurant_name = ''
        restaurant_addr = ''
        print(f"Error extracting content: {e}")

    
    # 본문 내용에서 해시태그 가져오기
    tags = re.findall(r'#[^\s#,\\]+', content)

    if not tags:  # tags 리스트가 비어 있으면 None
        tags = []

    try:
        # 댓글 가져오기
        comments_elements = driver.find_elements(By.CSS_SELECTOR, 'div._a9zr span._ap3a')
        comments = [unicodedata.normalize('NFC', c.text) for c in comments_elements]
        if not comments:
            comments = []
    except Exception as e:
        comments = []
        print(f"Error extracting comments: {e}")
        
    try:
        # 좋아요 수
        likes_element = driver.find_element(By.CSS_SELECTOR, 'section.x12nagc span.xdj266r')
        likes = likes_element.text

        
    except Exception as e:
        likes = estimate_likes_from_comments_and_tags(len(comments), len(tags))
        print(f"error: {e}")

    date_tag = driver.find_element(By.TAG_NAME, 'time')
    date = date_tag.get_attribute('datetime')  # datetime 속성 가져오기

    # 수집한 정보 저장하기
    data = [content, likes, tags, comments, restaurant_name, restaurant_addr, date]
    
    return data


# 이모지 등 특수문자 제거 함수
def remove_emoji(text):
    text = emoji.replace_emoji(text, replace='')
    return text

def clear_emoji(df):
    df['content'] = df['content'].apply(remove_emoji)
    df['hashtags'] = df['hashtags'].apply(lambda tags: [remove_emoji(tag) for tag in tags] if tags else [])
    df['comments'] = df['comments'].apply(lambda comments: [remove_emoji(comment) for comment in comments])
    df['comments'] = df['comments'].apply(lambda x: '' if x == [] else x)
    df['restaurant name'] = df['restaurant name'].apply(lambda restaurant_name: [remove_emoji(name) for name in restaurant_name])
    df['address'] = df['address'].apply(lambda addresses: [remove_emoji(address) for address in addresses])
    return df