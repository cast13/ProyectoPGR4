from fastapi import APIRouter, HTTPException
from app.models.producto import Producto
from app.use_cases.productos import (
    agregar_producto,
    actualizar_producto,
    eliminar_producto,
    ver_producto,
    listar_productos,
)

router = APIRouter()

@router.post("/", response_model=Producto)
async def crear_producto(producto: Producto):
    return agregar_producto(producto)

@router.put("/{producto_id}", response_model=Producto)
async def modificar_producto(producto_id: int, producto: Producto):
    updated_product = actualizar_producto(producto_id, producto)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_product

@router.delete("/{producto_id}")
async def borrar_producto(producto_id: int):
    return eliminar_producto(producto_id)

@router.get("/{producto_id}", response_model=Producto)
async def obtener_producto(producto_id: int):
    producto = ver_producto(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.get("/", response_model=list[Producto])
async def obtener_productos():
    return listar_productos() 