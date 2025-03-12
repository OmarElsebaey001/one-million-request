from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.asset import Asset as AssetModel
from app.schemas.asset import Asset as AssetSchema

router = APIRouter()

@router.get("/{pk}/", response_model=AssetSchema)
def get_asset(pk: int, db: Session = Depends(get_db)):
    """
    API endpoint that allows a specific asset to be viewed.
    
    Retrieves a specific asset by its ID.
    URL: /api/assets/<id>/
    Method: GET
    """
    asset = db.query(AssetModel).filter(AssetModel.id == pk).first()
    if asset is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found")
    return asset
