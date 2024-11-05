from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.models.producto import Producto

class Pedido(BaseModel):
    id: int  # El ID debe ser proporcionado al crear un pedido
    cliente_id: int  # ID del cliente
    productos: List[Producto]
    total: float
    estado: str  # Ejemplo: "Pendiente", "Enviado", "Entregado"

    def detalles(self):
        productos_detalle = [producto.model_dump() for producto in self.productos]
        return {
            "cliente_id": self.cliente_id,
            "productos": productos_detalle,
            "total": self.total,
            "estado": self.estado
        }