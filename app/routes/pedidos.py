from fastapi import APIRouter, HTTPException
from app.models.pedido import Pedido
from app.models.cliente import Cliente
from app.models.producto import Producto
from app.use_cases.pedidos import (
    crear_pedido,
    ver_detalles_pedido,
    actualizar_estado_pedido,
    cancelar_pedido,
    listar_pedidos,
)
from typing import List

router = APIRouter()

@router.post("/", response_model=Pedido)
async def crear_nuevo_pedido(pedido: Pedido):
    return crear_pedido(pedido)

@router.get("/{pedido_id}", response_model=Pedido)
async def obtener_detalles_pedido(pedido_id: int):
    pedido = ver_detalles_pedido(pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.put("/{pedido_id}", response_model=Pedido)
async def modificar_estado_pedido(pedido_id: int, estado: str):
    pedido = actualizar_estado_pedido(pedido_id, estado)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.delete("/{pedido_id}")
async def eliminar_pedido(pedido_id: int):
    if not cancelar_pedido(pedido_id):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"mensaje": "Pedido eliminado exitosamente"}

@router.get("/", response_model=List[Pedido])
async def obtener_pedidos():
    return listar_pedidos() 