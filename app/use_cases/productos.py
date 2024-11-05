from app.models.producto import Producto

# Simulación de base de datos
productos_db = []

def agregar_producto(producto: Producto) -> Producto:
    productos_db.append(producto)
    return producto

def actualizar_producto(producto_id: int, producto: Producto) -> Producto:
    if producto_id < len(productos_db):
        productos_db[producto_id] = producto
        return producto
    return None

def eliminar_producto(producto_id: int) -> bool:
    if producto_id < len(productos_db):
        productos_db.pop(producto_id)
        return True
    return False

def ver_producto(producto_id: int) -> Producto:
    if producto_id < len(productos_db):
        return productos_db[producto_id]
    return None

def listar_productos() -> list[Producto]:
    return productos_db 