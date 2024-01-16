import uvicorn
from fastapi import FastAPI, Body, Depends
from app.models import Ads, User, UserLogin
from app.auth.handler import signJWT
from app.auth.bearer import JWTBearer

example_ads = [
    {
        "id": 1, 
        "title": "Automobile 🚗", 
        "content":  "wheeled motor vehicle used for transportation. It is made up of various parts, such as engine, chassis, body and steering, brakes and suspension systems."
    },
    {
        "id": 2, 
        "title": "Airplane 🛫", 
        "content":  "It is a fixed-wing aerodyne, or aircraft with greater density than air, equipped with wings and a cargo space, and capable of flying powered by one or more engines. Airplanes include monoplanes, biplanes, and triplanes."
    },
    {
        "id": 3, 
        "title": "Boat 🚢", 
        "content":  "It is a construction, made of wood, metal or other material, capable of floating in water and used as a means of transportation. Remember: Barco is both a light canoe and an imposing aircraft carrier."
    }
]

users = []

app = FastAPI(
    title="FastAPI Authentication with JWT",
    description="",
)

# Testing App
@app.get('/', tags=["Test API"])
def app_is_run():
    return {'Hellow':'World!'}

# Posts
## Add New Ad
@app.post('/ads/new_ad', dependencies=[Depends(JWTBearer())], tags=['Ad Posts'], description='Add New Ad')
def create_add(ad: Ads):
    ad.id = len(example_ads) + 1
    example_ads.append(ad.dict())

    return {'info': 'New Ad created Successfully'}

## Create New User
@app.post('/users/new_user', tags=['Users'], description='Add New User')
def create_user(user: User = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

## Validate Credentials User
def check_user(data: UserLogin):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            return False

## User Login and Token Obtain
@app.post('/user/login', tags=['Users'], description='User Login and Get Token')
def login(user: UserLogin = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {"Error": "User credentials are incorrect!"}

# Gets
## Get all Ads
@app.get('/ads', tags=['Ads'], description='Get all Ads')
def get_ads():
    return {'data': example_ads}

## Get Ad by Id
@app.get('/ads/{id}', tags=['Ads'], description='Get Specific Ad')
def get_specific_ad(id:int):
    if id > len(example_ads):
        return {'error': 'the number of ID exceeds the number of ads published'}
    
    for ad in example_ads:

        if ad["id"] == id:
            return {'data':ad}