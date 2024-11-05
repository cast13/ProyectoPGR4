from fastapi import APIRouter, HTTPException
from app.models.producto import Producto
from app.use_cases.productos import (
    agregar_producto,
    actualizar_producto,
    eliminar_producto,
    ver_producto,
    listar_productos,
)
from uuid import UUID  # Importar UUID

router = APIRouter()

@router.post("/", response_model=Producto)
def crear_producto(producto: Producto):
    # El ID se generará automáticamente en el modelo
    return agregar_producto(producto)

@router.put("/{producto_id}", response_model=Producto)
def modificar_producto(producto_id: UUID, producto: Producto):  # Cambiar a UUID
    updated_product = actualizar_producto(producto_id, producto)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_product

@router.delete("/{producto_id}")
def borrar_producto(producto_id: UUID):  # Cambiar a UUID
    return eliminar_producto(producto_id)

@router.get("/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: UUID):  # Cambiar a UUID
    producto = ver_producto(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.get("/", response_model=list[Producto])
def obtener_productos():
    return listar_productos() 