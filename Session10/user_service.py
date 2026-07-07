from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import InventoryModel
from schemas import InventoryCreate

def create_inventory(item: InventoryCreate, db: Session):
    inventory = (
        db.query(InventoryModel)
        .filter(InventoryModel.warehouse_code == item.warehouse_code)
        .first()
    )

    if inventory:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Mã kho vận đã tồn tại trên hệ thống, không thể tạo trùng"
        )

    new_inventory = InventoryModel(
        warehouse_code=item.warehouse_code,
        location=item.location
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)

    return {
        "message": "Tạo kho vận thành công",
        "data": new_inventory
    }