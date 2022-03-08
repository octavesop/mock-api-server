from turtle import color
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
import datetime

app = FastAPI()

mongouri = 'mongodb://root:root@localhost:27017/development?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false'
client = MongoClient(mongouri)
db = client['development']

class User(BaseModel):
    id: str
    pw: str
    name: str
    hobby: list

class BrandRequest(BaseModel):
    name: str
    logo: str
    color: str
    userId: str
    keywords: list

# class Brand(BaseModel): 
#     name: str
#     logo: str
#     color: str
#     keywords: list
#     blockKeywords: list
#     isActivate: True
#     channels: None
#     keywords: list
#     blockKeywords: None
#     crawlingIntervalSec: 10800
#     crawlingDays: 3
#     hideServiceBrand: True
#     id: str
#     createdAt: datetime.datetime.now()
#     updatedAt: datetime.datetime.now()
#     __v: 0



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def insert_user(brand: BrandRequest):
    brandDict = brand.dict()
    brandData = {
        "name": brandDict["name"],
        "logo": brandDict["logo"],
        "color": brandDict["color"],
        "isActivate": True,
        "channels": ["twitter", "youtube", "instagram", "naver-blog", "naver-cafe", "humoruniv", "todayhumor", "ppomppu", "dcinside-gall", "bobaedream"],
        "keywords": ["test"],
        "blockKeywords": None,
        "crawlingIntervalSec": 10800,
        "crawlingDays": 3,
        "hideServiceBrand": True,
        "id": brandDict["userId"],
        "createdAt": datetime.datetime.now(),
        "updatedAt": datetime.datetime.now(),
        "__v": 0
    }
    print("음")
    db['Brand'].insert_one(brandData)
    return {"message": "success"}