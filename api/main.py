from fastapi import FastAPI

app = FastAPI

@app.get('/')  # o ('/') significa raiz, onde tudo começa no mundo da programação
async def raiz():
    return {"msg": "FastApi na Geek University"}