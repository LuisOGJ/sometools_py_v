from fastapi import FastAPI
from api.routers import router # Import EndPoints

# Create app
app = FastAPI(title="API tools", description="Some tools for daily use", version="1.0.0")

# Registry EndPoints
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port="8000")