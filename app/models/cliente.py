from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4
from typing import List
from app.models.pedido import Pedido

class Cliente(BaseModel):
    id: UUID = Field(default_factory=uuid4)  # Generar automáticamente un UUID
    nombre: str = Field(..., min_length=1, max_length=100)
    correo: EmailStr  # Validación automática para correos electrónicos
    direccion: str = Field(..., min_length=1)
    telefono: str = Field(..., min_length=1)
    pedidos: List[Pedido] = []  # Relación con los pedidos
