import datetime as dt
from typing import Optional
import uuid

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    """
    Modèle représentant un produit de la base de données.
    """

    __tablename__ = "Product"
    __table_args__ = {"schema": "SalesLT"}

    ProductID: Optional[int] = Field(default=None, primary_key=True)
    Name: str
    ProductNumber: str
    Color: Optional[str] = None
    StandardCost: float
    ListPrice: float
    Size: Optional[str] = None
    Weight: Optional[float] = None
    ProductCategoryID: Optional[int] = None
    ProductModelID: Optional[int] = None
    SellStartDate: Optional[dt.datetime] = Field(default_factory=dt.datetime.today)
    SellEndDate: Optional[dt.datetime] = None
    DiscontinuedDate: Optional[dt.datetime] = None
    ThumbNailPhotoFileName: Optional[str] = None
    rowguid: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, unique=True)
    ModifiedDate: Optional[dt.datetime] = Field(default_factory=dt.datetime.today)
