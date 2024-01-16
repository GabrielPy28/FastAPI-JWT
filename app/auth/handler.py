#this file is responsible to signing,  encoding, decoding and returning JSON Web Tokens
import time
import jwt
from decouple import config

JWT_SECRET = config('SECRET_KEY')
JWT_ALGORITHM = config('ALGORITHM')

def token_response(token:str) -> dict:
    return {
        "Access Token": token
    }

def signJWT(userID: str):
    payload = {
        "User ID": userID,
        "Expiry Toke": time.time() + 600
    }

    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

    return token_response(token=token)

def decode_token(token: str):
    try:
        decode = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)

        return decode if decode['expires'] >= time.time() else  None

    except jwt.exceptions.InvalidTokenError as e:
        return {'Error': 'Invalid token'}
    except jwt.exceptions.ExpiredSignatureError as e:
        return {'Error': 'Signature expired'}