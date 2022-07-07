import time
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Cookie, Header, Response
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

router = APIRouter(prefix="/product", tags=["Product"])

products = ["watch", "phone", "laptop"]


async def time_consuming_function():
    time.sleep(5)


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
        },
    },
)
async def get_products(
    accept: str = Header("application/json"), last_modified: str = Cookie(None)
):
    await time_consuming_function()
    media_types = {
        "application/json": lambda: JSONResponse(
            products, media_type="application/json"
        ),
        "text/csv": lambda: PlainTextResponse(
            ", ".join(products), media_type="text/csv"
        ),
        "text/html": lambda: HTMLResponse(
            "<h1>" + "</h1><h1>".join(products) + "</h1>", media_type="text/html"
        ),
    }
    response: Optional[Response] = None
    for type in media_types:
        if type in accept:
            response = media_types[type]()
    if response:
        response.set_cookie("last_modified", datetime.now().isoformat())
        return response
    return PlainTextResponse("No content type found", status_code=406)
