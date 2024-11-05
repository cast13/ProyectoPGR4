from pydantic import BaseModel
from uuid import UUID, uuid4  # Importar UUID y uuid4

class Producto(BaseModel):
    id: UUID  # Cambiar el tipo a UUID
    nombre: str
    descripcion: str
    precio: float
    stock: int

    def __init__(self, **data):
        if 'id' not in data or data['id'] is None:  # Generar un UUID si no se proporciona
            data['id'] = uuid4()  # Generar un nuevo UUID
        super().__init__(**data)