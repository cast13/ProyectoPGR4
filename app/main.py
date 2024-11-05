from fastapi import FastAPI
from app.routes import productos, pedidos, clientes
from app.infrastructure.database import engine, Base

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas
app.include_router(productos.router, prefix="/productos", tags=["productos"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["pedidos"])
app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])



