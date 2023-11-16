import uvicorn
from pathlib import Path
from src.app.app import *
from os import getenv
from dotenv import  load_dotenv

load_dotenv()

if __name__ == "__main__":
    
    uvicorn.run(
        f"{Path(__file__).stem}:app",
        host=getenv("HOST"),
        port=int(getenv("PORT")),
        reload=getenv("RELOAD"),
        debug=getenv("DEBUG"),
        log_level="info",
        workers=int(getenv("WORKERS")),
        factory=False
    )