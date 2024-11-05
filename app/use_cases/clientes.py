from app.models.cliente import Cliente

# Simulación de base de datos
clientes_db = []

def crear_cliente(cliente: Cliente) -> Cliente:
    clientes_db.append(cliente)
    return cliente

def editar_cliente(cliente_id: int, cliente: Cliente) -> Cliente:
    if cliente_id < len(clientes_db):
        clientes_db[cliente_id] = cliente
        return cliente
    return None

def eliminar_cliente(cliente_id: int) -> bool:
    if cliente_id < len(clientes_db):
        clientes_db.pop(cliente_id)
        return True
    return False

def ver_cliente(cliente_id: int) -> Cliente:
    if cliente_id < len(clientes_db):
        return clientes_db[cliente_id]
    return None

def listar_clientes() -> list[Cliente]:
    return clientes_db 