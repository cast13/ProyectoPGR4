from app.models.cliente import Cliente
from uuid import UUID

# Simulación de base de datos
clientes_db = []

def crear_cliente(cliente: Cliente) -> Cliente:
    clientes_db.append(cliente)
    return cliente

def editar_cliente(cliente_id: UUID, cliente: Cliente) -> Cliente:
    for index, c in enumerate(clientes_db):
        if c.id == cliente_id:
            clientes_db[index] = cliente
            return cliente
    return None

def eliminar_cliente(cliente_id: UUID) -> bool:
    for index, c in enumerate(clientes_db):
        if c.id == cliente_id:
            clientes_db.pop(index)
            return True
    return False

def ver_cliente(cliente_id: UUID) -> Cliente:
    for c in clientes_db:
        if c.id == cliente_id:
            return c
    return None

def listar_clientes() -> list[Cliente]:
    return clientes_db 