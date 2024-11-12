from fastapi import APIRouter, HTTPException
from app.models.pedido import Pedido
from app.use_cases.pedidos import (
    listar_pedidos,
    obtener_pedido_por_id,
    crear_pedido,
    eliminar_pedido,
    modificar_pedido,
)
from app.use_cases.productos import productos_db
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
        # Convertir los IDs de productos a objetos Producto
        productos = [next((p for p in productos_db if p.id == prod_id), None) for prod_id in pedido.productos]
        if None in productos:
            raise ValueError("Uno o más productos no encontrados")

        # Extraer solo los IDs de los productos encontrados
        producto_ids = [p.id for p in productos]  # Obtener solo los UUIDs

        # Crear un nuevo pedido con los IDs de productos
        pedido_con_productos = Pedido(cliente_id=pedido.cliente_id, productos=producto_ids)
        return crear_pedido(pedido_con_productos)  # Asegúrate de que esto devuelva un Pedido válido
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{pedido_id}", response_model=Pedido)
def modificar_pedido_(pedido_id: int, pedido: Pedido):
    """Modifica un pedido existente."""
    pedido_modificado = modificar_pedido(pedido_id, pedido)
    if not pedido_modificado:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido_modificado

@router.delete("/{pedido_id}")
def eliminar_pedido_(pedido_id: int):
    """Elimina un pedido existente."""
    if not eliminar_pedido(pedido_id):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"detail": "Pedido eliminado"}