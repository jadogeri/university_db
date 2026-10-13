from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI application
app = FastAPI(
    title="University DB API",
    description="FastAPI application root controller",
    version="1.0.0"
)

# Enable CORS so frontend workspaces can query it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hello API Root Route
@app.get("/")
def read_root():
    return {
        "message": "Hello World from FastAPI!",
        "status": "healthy",
        "docs": "/docs"
    }
