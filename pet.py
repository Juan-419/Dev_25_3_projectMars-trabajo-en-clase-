from fastapi import APIRouter, HTTPException
from models import Pet, PetCreate, User
from db import SessionDep


router = APIRouter()

@router.post("/", response_model=Pet)
async def create_pet(new_pet: PetCreate, session: SessionDep):
    pet_data = new_pet.model_dump()
    user_db=session.get(User,pet_data.get("user_id"))
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    pet = Pet.model_validate(pet_data)
    session.add(pet)
    session.commit()
    session.refresh(pet)
    return pet


@router.get("/", response_model=list[Pet], summary="Get all pets from the DB")
async def all_pets(session: SessionDep):
    return session.query(Pet).all()

@router.get("/{pet_id}", response_model=Pet)
async def get_one_pet(pet_id: int, session: SessionDep):
    pet_db = session.get_one(Pet, pet_id)
    if not pet_db:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet_db