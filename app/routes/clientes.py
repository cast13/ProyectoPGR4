from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

router = APIRouter()

# Modelo de Cliente
class Cliente(BaseModel):
    nombre: str
    correo: EmailStr
    direccion: str
    telefono: str

# Simulación de base de datos
clientes_db = []

@router.post("/", response_model=Cliente)
def crear_cliente(cliente: Cliente):
    clientes_db.append(cliente)
    return cliente

@router.put("/{cliente_id}", response_model=Cliente)
def editar_cliente(cliente_id: int, cliente: Cliente):
    if cliente_id >= len(clientes_db):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    clientes_db[cliente_id] = cliente
    return cliente

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    if cliente_id >= len(clientes_db):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    clientes_db.pop(cliente_id)
    return {"detail": "Cliente eliminado"}

@router.get("/{cliente_id}", response_model=Cliente)
def ver_cliente(cliente_id: int):
    if cliente_id >= len(clientes_db):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return clientes_db[cliente_id]

@router.get("/", response_model=list[Cliente])
def listar_clientes():
    return clientes_db 