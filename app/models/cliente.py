from pydantic import BaseModel, EmailStr

class Cliente(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    direccion: str
    telefono: str 