from fastapi import APIRouter, Request
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
