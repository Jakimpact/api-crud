from datetime import timedelta
from typing import Annotated, List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select, Session

from connect_db import get_session, ENGINE
from generate_auth import authenticate_user, create_access_token, get_current_active_user, Token, User, users_db
from models import Product


ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(
    title="API CRUD Adventuresworks",
    description="""
        API CRUD avec authentification OAuth2 permettant les opérations suivantes : 
            - Lister les produits
            - Consulter un produit spécifique
            - Ajouter un produit
            - Modifier un produit
            - Supprimer un produit
    """
)


@app.get("/")
async def home():
    return {"Hello": "HELLO THERE"}


@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    Login un utilisateur et récupère un token d'authentification.
    """

    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/products", response_model=List[Product])
async def get_products(current_user: Annotated[User, Depends(get_current_active_user)], session: Session=Depends(get_session)):
    """
    Liste l'ensemble des produits de la base de données.
    """

    products = select(Product)
    results = session.exec(products)
    return results.all()
    

@app.get("/products/{product_id}", response_model=Product)
async def get_product(current_user: Annotated[User, Depends(get_current_active_user)], product_id: int, session: Session=Depends(get_session)):
    """
    Récupère un produit spécifique de la base de données.
    Params :
        - product_id : int -> ProductID du produit à récupérer.
    """

    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Error 404: Product not found")
    return product


@app.post("/products", response_model=Product)
async def add_product(current_user: Annotated[User, Depends(get_current_active_user)], product: Product, session: Session=Depends(get_session)):
    """
    Crée un nouveau produit dans la base de données.
    Params :
        - product : Product -> JSON avec les informations du modèle représentant un produit de la base de données.
    """

    new_product = Product.model_validate(product)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product


@app.put("/products/{product_id}",response_model=Product)
async def update_product(current_user: Annotated[User, Depends(get_current_active_user)], product: Product, product_id: int, session: Session=Depends(get_session)):
    """
    Modifie un produit existant dans la base de données.
    Params :
        - product_id : int -> ProductID du produit à modifier.
        - product : Product -> JSON avec les informations du modèle représentant un produit de la base de données.
    """

    product_updated = session.get(Product, product_id)
    if not product_updated:
        raise HTTPException(status_code=404, detail="Error 404: Product not found")
    product_data = product.model_dump(exclude_unset=True)
    for key, value in product_data.items():
        setattr(product_updated, key, value)
    session.add(product_updated)
    session.commit()
    session.refresh(product_updated)
    return product_updated


@app.delete("/products/{product_id}", response_model=Product)
async def delete_product(current_user: Annotated[User, Depends(get_current_active_user)], product_id: int, session: Session=Depends(get_session)):
    """
    Supprime un produit de la base de données.
    Params :
        - product_id : int -> ProductID du produit à supprimer.
    """

    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Error 404: Product not found")
    session.delete(product)
    session.commit()
    return {"Confirmation message": "Product successfuly deleted"}