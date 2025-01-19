import datetime as dt
from typing import Optional
import uuid

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    ProductID: Optional[int] = Field(default=None, primary_key=True)
    Name: str
    ProductNumber: str
    Color: Optional[str] = None
    StandartCost: float
    ListPrice: float
    Size: Optional[str] = None
    Weight: Optional[float] = None
    ProductCategoryID: Optional[int] = None
    ProductModelID: Optional[int] = None
    SellStartDate: Optional[dt.datetime] = Field(default_factory=dt.datetime.now(dt.timezone.utc))
    SellEndDate: Optional[dt.datetime] = None
    DiscontinuedDate: Optional[dt.datetime] = None
    ThumbNailPhoto: str = None
    ThumbNailPhotoFileName: str = None
    rowguid: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, unique=True)
    ModifiedDate: Optional[dt.datetime] = Field(default_factory=dt.datetime.now(dt.timezone.utc))
