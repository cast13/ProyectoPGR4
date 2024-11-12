from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.routes import productos, pedidos, clientes
from app.infrastructure.database import engine, Base

app = FastAPI()

# Middleware para permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "detail": [
                {
                    "loc": error["loc"],
                    "msg": f"Error en el campo {error['loc'][-1]}: {traducir_mensaje_error(error['msg'])} ({traducir_tipo_error(error['type'])})",
                } for error in exc.errors()
            ],
            "body": exc.body,
        },
    )

def traducir_mensaje_error(msg: str) -> str:
    traducciones = {
        "Input should be a valid number, unable to parse string as a number": "El valor debe ser un número válido",
        "value is not a valid email address": "El valor no es una dirección de correo electrónico válida",
        "An email address must have an @-sign": "Una dirección de correo electrónico debe tener un @",
        "Input should be greater than 0": "El valor debe ser mayor que 0",
        "String should have at least 1 character": "La cadena debe tener al menos 1 caracter",
        "value is not a valid string": "el valor no es una cadena válida",
        "string does not match regex": "la cadena no coincide con el patrón",
        "field required": "el campo es obligatorio",
        "value is not a valid float": "el valor no es un número decimal válido",
        "ensure this value is greater than 0": "asegúrate de que este valor sea mayor que 0",
        "value is not a valid integer": "el valor no es un número entero válido",
        "string is too short": "la cadena es demasiado corta",
        "string is too long": "la cadena es demasiado larga",
    }
    return traducciones.get(msg, msg)

def traducir_tipo_error(tipo: str) -> str:
    traducciones_tipo = {
        "float_parsing": "error de número decimal",
        "greater_than": "mayor_que",
        "string_too_short": "cadena_corta",
        "value_error": "error de valor",
        "type_error": "error de tipo",
        "value_error.str": "error de cadena",
        "value_error.float": "error de número decimal",
        "value_error.integer": "error de número entero",
    }
    return traducciones_tipo.get(tipo, tipo)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas
app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
app.include_router(productos.router, prefix="/productos", tags=["productos"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["pedidos"])




