from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def test_endpoint():
    """Check if the server is online or not."""
    return {"message": "API is live"}


@app.get("/blog/all", tags=["Blog"])
def all_blogs():
    """Retrieve all blogs."""
    return {"message": "All blogs"}
