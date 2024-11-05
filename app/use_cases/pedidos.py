from app.models.pedido import Pedido
from app.models.cliente import Cliente
from app.models.producto import Producto
from typing import List

# Simulación de base de datos
pedidos_db = []

def crear_pedido(pedido: Pedido) -> Pedido:
    pedidos_db.append(pedido)
    return pedido

def ver_detalles_pedido(pedido_id: int) -> Pedido:
    if pedido_id < len(pedidos_db):
        return pedidos_db[pedido_id]
    return None

def actualizar_estado_pedido(pedido_id: int, estado: str) -> Pedido:
    if pedido_id < len(pedidos_db):
        pedidos_db[pedido_id].estado = estado
        return pedidos_db[pedido_id]
    return None

def cancelar_pedido(pedido_id: int) -> bool:
    if pedido_id < len(pedidos_db):
        pedidos_db.pop(pedido_id)
        return True
    return False

def listar_pedidos() -> List[Pedido]:
    return pedidos_db