from pydantic import BaseModel
from typing import List

class Pedido(BaseModel):
    id: int
    cliente_id: int
    productos: List[int]  # Lista de IDs de productos
    total: float
    estado: str  # Ejemplo: "Pendiente", "Enviado", "Entregado" 