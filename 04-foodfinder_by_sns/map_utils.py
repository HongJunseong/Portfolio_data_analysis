import re
import requests
import json

# Your KAKAO REST API KEY
KAKAO_REST_API_KEY = 'YOUR KAKAO REST API KEY' # Kakao REST API KEY 입력

# 층, 호 정보 제거 함수
def extract_road_address(address):
    # 도로명 주소 패턴: '도로명' + '건물번호'
    pattern = r'([가-힣]+\s[가-힣]+\s[가-힣0-9\-]+(?:로|길)\s*\d+(-\d+)?)'  # 도로명과 번호 추출
    match = re.search(pattern, address)
    if match:
        return match.group(0)  # 매칭된 첫 번째 그룹 반환
    return address  # 매칭 실패 시 원본 반환


# address를 입력하면 좌표를 반환하는 함수
def coord_info(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    params = {
        'query': address
    }
    headers = {
    "Authorization": f"KakaoAK {KAKAO_REST_API_KEY}"  # 실제 API 키를 넣어야 합니다
    }
    response = requests.get(url, headers=headers, params=params)
    result = response.json()

    if result['documents']:
        address = result['documents'][0]
        return address['y'], address['x']
    else:
        print("해당 주소를 찾을 수 없습니다.")
        return None, None
    

# 매장명과 주소를 통해 매장의 정보를 얻는 함수
def search_place_by_address(address, place_name):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_REST_API_KEY}"}
    params = {"query": address}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        result = json.loads(response.text)
        if result['documents']:
            # 정확한 검색 결과 정보 반환
            for i in result['documents']:
                if i['place_name'] == place_name:
                    
                    return {
                        'place_name': i['place_name'], # 정확한 매장명 확인을 위함
                        'address_name': i['road_address_name'], # 도로명 주소
                        'x': float(i['x']),  # 경도
                        'y': float(i['y'])   # 위도
                        }
                else:
                    continue
            
    return None