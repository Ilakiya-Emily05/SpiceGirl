from fastapi import APIRouter

router = APIRouter(
    prefix="/clothes",
    tags=["Clothes"]
)


@router.get("/")
def get_clothes():
    return []


@router.post("/")
def add_clothing():
    return {
        "message": "Clothing added"
    }


@router.get("/{clothing_id}")
def get_clothing(clothing_id: str):
    return {
        "id": clothing_id
    }


@router.put("/{clothing_id}")
def update_clothing(clothing_id: str):
    return {
        "message": "Updated"
    }


@router.delete("/{clothing_id}")
def delete_clothing(clothing_id: str):
    return {
        "message": "Deleted"
    }