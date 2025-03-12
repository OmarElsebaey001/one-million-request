import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.asset import Asset
from datetime import datetime, timedelta
import random

# Sample data for assets
asset_types = ["Equipment", "Vehicle", "Building", "Land", "Software", "Hardware", "Furniture"]
locations = ["New York", "San Francisco", "Chicago", "Austin", "Seattle", "Los Angeles", "Boston"]
statuses = ["active", "inactive", "maintenance", "retired"]

def create_sample_assets(db: Session, count: int = 100):
    """Create sample assets in the database"""
    print(f"Creating {count} sample assets...")
    
    # Clear existing data
    db.query(Asset).delete()
    db.commit()
    
    # Create new assets
    for i in range(1, count + 1):
        asset = Asset(
            name=f"Asset {i}",
            description=f"This is a description for asset {i}",
            asset_type=random.choice(asset_types),
            value=round(random.uniform(100, 10000), 2),
            location=random.choice(locations),
            acquisition_date=datetime.now() - timedelta(days=random.randint(1, 1000)),
            status=random.choice(statuses),
            created_at=datetime.now() - timedelta(days=random.randint(1, 100)),
            updated_at=datetime.now() - timedelta(days=random.randint(0, 50))
        )
        db.add(asset)
    
    db.commit()
    print(f"Created {count} sample assets successfully!")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        count = int(sys.argv[1]) if len(sys.argv) > 1 else 100
        create_sample_assets(db, count)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
