from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
# from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# origins = [
#    "http://127.0.0.1:5500"  # Replace with the actual URL of your web page
# ]

# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
# )

@AuthJWT.load_config
def get_config(): 
    return Settings()

app.include_router(auth_router)

app.include_router(order_router)