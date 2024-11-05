from fastapi import APIRouter, HTTPException
from app.models.cliente import Cliente as ClienteModel
from uuid import UUID

router = APIRouter()

# Simulación de base de datos
clientes_db = []

@router.post("/", response_model=ClienteModel)
def crear_cliente(cliente: ClienteModel):
    # El ID se generará automáticamente en el modelo
    clientes_db.append(cliente)
    return cliente

@router.put("/{cliente_id}", response_model=ClienteModel)
def editar_cliente(cliente_id: UUID, cliente: ClienteModel):
    for index, c in enumerate(clientes_db):
        if c.id == cliente_id:
            clientes_db[index] = cliente
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: UUID):
    for index, c in enumerate(clientes_db):
        if c.id == cliente_id:
            clientes_db.pop(index)
            return {"detail": "Cliente eliminado"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.get("/{cliente_id}", response_model=ClienteModel)
def ver_cliente(cliente_id: UUID):
    for c in clientes_db:
        if c.id == cliente_id:
            return c
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.get("/", response_model=list[ClienteModel])
def listar_clientes():
    return clientes_db