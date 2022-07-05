from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def test_endpoint():
    return {"message": "API is live"}
