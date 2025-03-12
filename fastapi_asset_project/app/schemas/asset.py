from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from decimal import Decimal

class AssetBase(BaseModel):
    name: str
    description: Optional[str] = None
    asset_type: str
    value: Decimal = Field(default=0, ge=0, decimal_places=2)
    location: Optional[str] = None
    acquisition_date: Optional[date] = None
    status: str = "active"

class AssetCreate(AssetBase):
    pass

class AssetUpdate(AssetBase):
    name: Optional[str] = None
    asset_type: Optional[str] = None
    value: Optional[Decimal] = None
    status: Optional[str] = None

class AssetInDB(AssetBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Asset(AssetInDB):
    pass
