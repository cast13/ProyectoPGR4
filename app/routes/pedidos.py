from fastapi import APIRouter, HTTPException
from app.models.pedido import Pedido
from app.use_cases.pedidos import (
    crear_pedido,
    ver_detalles_pedido,
    actualizar_estado_pedido,
    cancelar_pedido,
    listar_pedidos,
)

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
    return cancelar_pedido(pedido_id)

@router.get("/", response_model=list[Pedido])
async def obtener_pedidos():
    return listar_pedidos() 