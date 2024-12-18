from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, conint, field_validator
from typing import List, Optional
from app.models.producto import Producto
from uuid import UUID

class Cliente(BaseModel):
    id: int  # ID del cliente
    nombre: str  # Nombre del cliente
    pedidos: List['Pedido'] = []  # Relación con los pedidos

class Pedido(BaseModel):
    cliente_id: UUID  # ID del cliente
    productos: List[UUID]  # Lista de IDs de productos en el pedido
    estado: str = "Pendiente"  # Estado por defecto

    @field_validator('productos')
    def verificar_productos(cls, v):
        if len(v) == 0:
            raise ValueError("El número de productos debe ser mayor a cero.")
        return v

    def detalles(self):
        productos_detalle = [producto.model_dump() for producto in self.productos]
        return {
            "cliente_id": self.cliente_id,
            "productos": productos_detalle,
            "estado": self.estado
        }

# Método para obtener pedidos de un cliente
def obtener_pedidos_por_cliente(cliente_id: int, pedidos: List[Pedido]) -> List[Pedido]:
    return [pedido for pedido in pedidos if pedido.cliente_id == cliente_id]