from app.models.producto import Producto
from uuid import UUID  # Importar UUID

# Simulación de base de datos
productos_db = []

def agregar_producto(producto: Producto) -> Producto:
    # No es necesario asignar un ID aquí, ya que se genera en el modelo
    productos_db.append(producto)
    return producto

def actualizar_producto(producto_id: UUID, producto: Producto) -> Producto:  # Cambiar a UUID
    for index, p in enumerate(productos_db):
        if p.id == producto_id:
            productos_db[index] = producto
            return producto
    return None

def eliminar_producto(producto_id: UUID) -> bool:  # Cambiar a UUID
    for index, p in enumerate(productos_db):
        if p.id == producto_id:
            productos_db.pop(index)
            return True
    return False

def ver_producto(producto_id: UUID) -> Producto:  # Cambiar a UUID
    for p in productos_db:
        if p.id == producto_id:
            return p
    return None

def listar_productos() -> list[Producto]:
    return productos_db