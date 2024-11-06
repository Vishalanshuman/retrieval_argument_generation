from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base,engine
from Users.users import router as user_router
from chatbot.api import router as chat_router

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user_router)
app.include_router(chat_router)

@app.get("/")
def health():
    return {"message":"Hello world!!!"}