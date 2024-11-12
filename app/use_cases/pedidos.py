from app.models.pedido import Pedido
from app.models.producto import Producto
from typing import List, Optional
from uuid import UUID, uuid4

# Simulación de base de datos
pedidos_db = []
productos_db = [
    Producto(id=uuid4(), nombre="Producto 1", precio=10.0, cantidad=5),
    Producto(id=uuid4(), nombre="Producto 2", precio=15.0, cantidad=10),
    Producto(id=uuid4(), nombre="Producto 3", precio=20.0, cantidad=3),
]

def contar_pedidos_por_cliente(cliente_id: UUID) -> int:
    """Cuenta el número de pedidos para un cliente específico."""
    return sum(1 for pedido in pedidos_db if pedido.cliente_id == cliente_id)

def crear_pedido(pedido: Pedido) -> Pedido:
    """Crea un nuevo pedido y lo agrega a la base de datos."""
    pedidos_db.append(pedido)
    return pedido  # Asegúrate de devolver el pedido creado

def listar_pedidos() -> List[Pedido]:
    """Devuelve una lista de todos los pedidos."""
    return pedidos_db

def obtener_pedido_por_id(pedido_id: int) -> Optional[Pedido]:
    """Devuelve un pedido específico por su ID."""
    for pedido in pedidos_db:
        if pedido.id == pedido_id:
            return pedido
    return None

def modificar_pedido(pedido_id: int, pedido: Pedido) -> Optional[Pedido]:
    """Modifica un pedido existente."""
    for index, p in enumerate(pedidos_db):
        if p.id == pedido_id:
            pedidos_db[index] = pedido
            return pedido
    return None

def eliminar_pedido(pedido_id: int) -> bool:
    """Elimina un pedido existente."""
    for index, p in enumerate(pedidos_db):
        if p.id == pedido_id:
            pedidos_db.pop(index)
            return True
    return False
