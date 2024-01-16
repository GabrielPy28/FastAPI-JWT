# FastAPI with Authentication JSON Web Tokens (JWT)
> Example app to easily add token-based authentication to your [FastAPI](https://fastapi.tiangolo.com) applications. [JWT tokens](https://jwt.io) are a secure and efficient way to authenticate users in modern web applications.
>
> ![FastAPI-JWT](https://th.bing.com/th/id/OIG.Aj5rWjqmYWxvDshIjqmU?pid=ImgGn)

## First Steps

1. Clone the Repository:
```
git clone https://github.com/GabrielPy28/FastAPI-JWT.git
```

2. In the terminal run comand: 
```
> python
> import secrets
... secrets.token_hex(16)
```

2. Configure environment variables
```
echo "SECRET_KEY = use your secret code with secrets.token_hex(16) here" >> .env
echo "ALGORITHM = HS256" >> .env
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Run app:
```
uvicorn main:app --reload
```

> [!NOTE]
> If everything is working correctly, the app is running on http://127.0.0.1:8000, to access all endpoints, go to http://127.0.0.1:8000/docs
