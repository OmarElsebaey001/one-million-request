from sqlalchemy import Column, Integer, String, Text, Numeric, Date, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Asset(Base):
    """Model representing an asset in the system"""
    __tablename__ = "assets"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    asset_type = Column(String(100), nullable=False)
    value = Column(Numeric(12, 2), default=0)
    location = Column(String(255), nullable=True)
    acquisition_date = Column(Date, default=func.now())
    status = Column(String(20), default="active")  # Choices: active, inactive, maintenance, retired
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Asset {self.name}>"
