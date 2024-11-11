from app.models.pedido import Pedido
from app.models.cliente import Cliente
from app.models.producto import Producto
from typing import List, Optional
from uuid import UUID

# Simulación de base de datos
pedidos_db = []
clientes_db = []  # Simulación de base de datos para clientes

def crear_pedido(pedido: Pedido) -> Pedido:
    # Verificar si el cliente existe
    cliente = next((c for c in clientes_db if c.id == pedido.cliente_id), None)
    if not cliente:
        raise ValueError("Cliente no encontrado")

    # Calcular el total del pedido
    total = sum(producto.precio * producto.cantidad for producto in pedido.productos)
    pedido.total = total  # Asignar el total al pedido

    # Agregar el pedido a la base de datos
    pedidos_db.append(pedido)
    
    # Agregar el pedido a la lista de pedidos del cliente
    cliente.pedidos.append(pedido)  # Asegúrate de que el cliente tenga una lista de pedidos

    return pedido

def listar_pedidos() -> List[Pedido]:
    """Devuelve una lista de todos los pedidos."""
    return pedidos_db

def obtener_pedido_por_id(pedido_id: int) -> Optional[Pedido]:
    """Devuelve un pedido específico por su ID."""
    for pedido in pedidos_db:
        if pedido.id == pedido_id:
            return pedido
    return None
def listar_pedidos_por_cliente(cliente_id: UUID) -> List[Pedido]:
    """Devuelve una lista de pedidos para un cliente específico."""
    return [pedido for pedido in pedidos_db if pedido.cliente_id == cliente_id]

def contar_pedidos_por_cliente(cliente_id: UUID) -> int:
    """Devuelve la cantidad de pedidos para un cliente específico."""
    return len(listar_pedidos_por_cliente(cliente_id))
