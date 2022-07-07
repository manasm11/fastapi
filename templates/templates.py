import os
import time

from fastapi import APIRouter, BackgroundTasks, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas import ProductRequest

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="/template", tags=["Template"])


@router.get("/products/{id}", tags=["Template"], response_class=HTMLResponse)
async def get_products(id: int, request: Request):
    return templates.TemplateResponse("products.html", {"request": request, "id": id})


@router.post("/products", tags=["Template"], response_class=HTMLResponse)
async def post_products(request: Request, product: ProductRequest):
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "title": product.title,
            "description": product.description,
            "price": product.price,
        },
    )


def log_request():
    time.sleep(10)
    if not os.path.exists("logs/"):
        os.makedirs("logs/")
    with open("logs/template-logs.txt", "w") as f:
        f.write(f"{time.time()}: Request Logged")


@router.get("/log-request", tags=["Template"])
def log_response_in_background(bt: BackgroundTasks):
    bt.add_task(log_request)
    return "ok"
