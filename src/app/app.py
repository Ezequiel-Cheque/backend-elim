from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import getenv
from dotenv import  load_dotenv

load_dotenv()

def app():
    
    app = FastAPI(
        docs_url="/api",
        redoc_url=None,
        title="Microservice FEDE ELIM Backend",
        description="The documentation is from FEDE ELIM Backend",
        version=getenv("VERSION")
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    
    @app.get("/")
    async def index():
        return "Hello world !!"
    
    return app

create_app = app()