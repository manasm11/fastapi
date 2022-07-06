from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

router = APIRouter(prefix="/product", tags=["Product"])

products = ["watch", "phone", "laptop"]


@router.get(
    "/",
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": ["watch", "phone", "laptop"],
                },
                "text/csv": {
                    "example": "watch,phone,laptop",
                },
                "text/html": {
                    "example": """
                    <h1>watch</h1>
                    <h1>phone</h1>
                    <h1>laptop</h1>
                    """
                },
            },
            "description": "List of products",
        },
        406: {
            "description": "No content type found",
        }
    },
)
def get_products(request: Request):
    content_type = request.headers.get("accept", "application/json")
    responses = {
        "application/json": lambda: JSONResponse(
            products, media_type="application/json"
        ),
        "text/plain": lambda: PlainTextResponse(
            ", ".join(products), media_type="text/plain"
        ),
        "text/html": lambda: HTMLResponse(
            "<h1>" + "</h1><h1>".join(products) + "</h1>", media_type="text/html"
        ),
    }
    for accept in responses:
        if accept in content_type:
            return responses[accept]()
    return PlainTextResponse("No content type found", status_code=406)
