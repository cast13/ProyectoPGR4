from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Producto(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nombre: str = Field(..., min_length=1, max_length=100, description="El nombre del producto debe ser entre 1 y 100 caracteres.")
    precio: float = Field(..., gt=0, description="El precio debe ser mayor a cero.")
    cantidad: int = Field(..., gt=0, description="La cantidad debe ser mayor a cero.")
    
    # Agrega más validaciones según sea necesario