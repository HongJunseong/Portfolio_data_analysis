from pymongo import MongoClient
import pandas as pd

def connect_mongodb(db_name, collection_name):
    # MongoDB 클라이언트 생성 (기본 포트 27017)
    client = MongoClient("mongodb://localhost:27017/")  # 변경: 본인의 MongoDB URI
    db = client[db_name]  # 데이터베이스 선택
    collection = db[collection_name]  # 컬렉션 선택
    return collection

# DataFrame을 MongoDB에 저장하는 함수
def save_to_mongodb_unique(df, collection):
    data_dict = df.to_dict("records")
    for record in data_dict:
        collection.update_one(
            {"content": record["content"]},  # content 필드를 기준으로 중복 확인
            {"$setOnInsert": record},        # 데이터가 없을 때만 삽입
            upsert=True                      # 조건에 맞는 데이터가 없으면 삽입
        )

# MongoDB에서 데이터를 읽어오는 함수
def read_from_mongodb(collection):
    data = list(collection.find())  # MongoDB에서 모든 데이터 가져오기
    return pd.DataFrame(data)       # DataFrame으로 변환


# DB에서 중복을 제거하는 함수
def remove_duplicates(collection, field_name):
    # 중복을 기준으로 조건 설정
    unique_items = collection.aggregate([
        {"$group": {
            "_id": f"${field_name}",
            "count": {"$sum": 1},
            "docs": {"$push": "$_id"}
        }},
        {"$match": {"count": {"$gt": 1}}}
    ])

    # 중복된 문서 삭제
    for item in unique_items:
        # 첫 번째 문서를 제외한 나머지 삭제
        docs_to_delete = item['docs'][1:]
        collection.delete_many({"_id": {"$in": docs_to_delete}})