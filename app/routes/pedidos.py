from fastapi import APIRouter, HTTPException
from app.models.pedido import Pedido
from app.use_cases.pedidos import (
    listar_pedidos,
    obtener_pedido_por_id,
    crear_pedido,
)
from typing import List
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=List[Pedido])
def obtener_pedidos():
    """Devuelve una lista de todos los pedidos."""
    pedidos = listar_pedidos()
    if not pedidos:
        raise HTTPException(status_code=404, detail="No se encontraron pedidos")
    return pedidos

@router.get("/{pedido_id}", response_model=Pedido)
def ver_pedido(pedido_id: int):
    """Devuelve los detalles de un pedido específico."""
    pedido = obtener_pedido_por_id(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.post("/", response_model=Pedido)
def crear_nuevo_pedido(pedido: Pedido):
    """Crea un nuevo pedido."""
    try:
        return crear_pedido(pedido)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))