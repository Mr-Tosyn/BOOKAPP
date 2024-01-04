from fastapi import FastAPI
from routers.books import books_router
from routers.users import users_router

app = FastAPI()

app.include_router(books_router, prefix="/books") 
app.include_router(users_router, prefix="/users")

@app.get("/")
def home():  

