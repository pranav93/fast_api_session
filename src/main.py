from fastapi import FastAPI, Path, Query, HTTPException, status, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.model import Item as DBItem
from src.schemas import CreateItemRequest, UpdateItemRequest, ItemResponse

app = FastAPI()


@app.post("/create-item/")
def create_item(item: CreateItemRequest, db_session: Session = Depends(get_db)):
    to_create = DBItem(
        name=item.name,
        price=item.price,
        brand=item.brand
    )
    db_session.add(to_create)
    db_session.commit()
    return ItemResponse(
        id=to_create.id,
        name=to_create.name,
        price=to_create.price,
        brand=to_create.brand,
    )


@app.get("/get-item/{item_id}")
def get_item(
        item_id: int = Path(None, title="Id of the item", description="The ID of the item you would like to view"),
        db_session: Session = Depends(get_db)):
    to_get = db_session.query(DBItem).filter(DBItem.id == item_id).first()
    if to_get is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The item with provided id does not exist")
    return ItemResponse(
        id=to_get.id,
        name=to_get.name,
        price=to_get.price,
        brand=to_get.brand,
    )


@app.get("/get-by-name")
def get_by_name(
        name: str = Query(None, title="Name", description="Name of the item"),
        db_session: Session = Depends(get_db)):
    to_get = db_session.query(DBItem).filter(DBItem.name == name).first()
    if to_get is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The item with provided name does not exist")
    return ItemResponse(
        id=to_get.id,
        name=to_get.name,
        price=to_get.price,
        brand=to_get.brand,
    )


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int = Path(None, title="Item Id", description="Id of the item"),
                db_session: Session = Depends(get_db)):
    db_session.query(DBItem).filter(DBItem.id == item_id).delete()
    db_session.commit()
    return {"deleted": True}


@app.put("/update-item/{item_id}")
def update_item(item: UpdateItemRequest, item_id: int = Path(None, title="Item Id", description="Id of the item"),
                db_session: Session = Depends(get_db)):
    to_update = db_session.query(DBItem).filter(DBItem.id == item_id).first()
    if to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The item with provided it does not exist")

    if item.name is not None:
        to_update.name = item.name
    if item.price is not None:
        to_update.price = item.price
    if item.brand is not None:
        to_update.brand = item.brand

    db_session.add(to_update)
    db_session.commit()
    return ItemResponse(
        id=to_update.id,
        name=to_update.name,
        price=to_update.price,
        brand=to_update.brand,
    )


@app.get("/")
def hello():
    return {"msg": "Hello World"}
