from model.pet import Pet
from service import abb_service
from fastapi import APIRouter, Response, status
from service.messages_service import MessageService

abb_service = abb_service.ABBService()
abb_route = APIRouter(prefix="/abb")
messages = MessageService()

@abb_route.get("/")
async def get_pets():
    try:
        pets = abb_service.abb.root
        if pets is None:
            return {"message": messages.get("null_pet_list")}
        return pets
    except Exception:
        return {"message": messages.get("internal_error")}

@abb_route.get("/inorder")
async def get_pets_inorder():
    try:
        pets = abb_service.abb.inorder()
        if not pets:
            return {"message": messages.get("empty_pet_list")}
        return pets
    except Exception:
        return {"message": messages.get("internal_error")}

@abb_route.get("/preorder")
async def get_pets_preorder():
    try:
        pets = abb_service.abb.preorder()
        if not pets:
            return {"message": messages.get("empty_pet_list")}
        return pets
    except Exception:
        return {"message": messages.get("internal_error")}

@abb_route.get("/postorder")
async def get_pets_postorder():
    try:
        pets = abb_service.abb.postorder()
        if not pets:
            return {"message": messages.get("empty_pet_list")}
        return pets
    except Exception:
        return {"message": messages.get("internal_error")}

@abb_route.post("/", status_code=200)
async def create_pet(pet: Pet, response: Response):
    if pet.name.strip() == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": messages.get("name_required")}

    if pet.age < 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": messages.get("invalid_age")}

    if pet.breed.strip() == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": messages.get("breed_required")}

    try:
        abb_service.abb.add(pet)
        return {"message": messages.get("pet_created_success")}
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": messages.get("internal_error")}

@abb_route.put("/{id}")
async def update_pet(id: int, pet: Pet, response: Response):
    try:
        abb_service.abb.update(pet, id)
        return {"message": messages.get("pet_updated_success")}
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": messages.get("internal_error")}

@abb_route.delete("/{id}")
async def delete_pet(id: int, response: Response):
    try:
        abb_service.abb.delete(id)
        return {"message": messages.get("pet_deleted_success")}
    except Exception:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": messages.get("internal_error")}

@abb_route.get("/breed")
async def breed_count():
    try:
        return abb_service.abb.breed_count()
    except Exception:
        return {"message": messages.get("internal_error")}



