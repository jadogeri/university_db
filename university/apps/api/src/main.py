from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all feature routers
from features.student.controller import router as student_router
from features.course.controller import router as course_router
from features.classroom.controller import router as classroom_router
from features.department.controller import router as department_router
from features.section.controller import router as section_router

# 1. Initialize the Single FastAPI Application Instance
app = FastAPI(
    title="University DB API",
    description="FastAPI application root controller inside a Turborepo",
    version="1.0.0"
)

# 2. Configure CORS Middleware (Frontend Workspace Integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust if your Next.js/Vite app uses a different port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Mount all Feature Routers onto the Routing Network
app.include_router(student_router)
app.include_router(course_router)
app.include_router(classroom_router)
app.include_router(department_router)
app.include_router(section_router)


# 4. Hello API Root Route
@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Hello World from FastAPI!",
        "status": "healthy",
        "docs": "/docs"
    }
