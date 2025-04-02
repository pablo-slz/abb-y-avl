from fastapi import FastAPI
from controller import abb_controller

app = FastAPI()

app.include_router(abb_controller.abb_route)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
