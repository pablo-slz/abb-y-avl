from model.pet import Pet
from service import abb_service
from fastapi import APIRouter

abb_service = abb_service.ABBService()

abb_route = APIRouter(prefix="/abb")

@abb_route.get("/")
async def get_pets():
    return abb_service.abb.root


@abb_route.get("/")
async def get_pets():
    return abb_service.abb.root


@abb_route.post("/")
async def create_pet(pet: Pet):
    if abb_service.exists(pet.id):  # Validación sin recursividad
        return {"error": f"La mascota con ID {pet.id} ya existe."}

    abb_service.abb.add(pet)
    return {"message": "Mascota agregada con éxito"}

@abb_route.get("/breed_count")
async def get_breed_count():
    return abb_service.breed_count()

@abb_route.delete("/{id}")
async def delete_pet(id: int):
    if abb_service.delete_pet(id):
        return {"message": f"Mascota con ID {id} eliminada con éxito"}
    return {"error": f"No se encontró ninguna mascota con ID {id}"}

@abb_route.put("/{id}")
async def update_pet(id: int, pet: Pet):
    updated = abb_service.update_pet(id, pet.name, pet.age, pet.race)
    if updated:
        return {"message": f"Mascota con ID {id} actualizada correctamente."}
    return {"error": f"No se encontró ninguna mascota con ID {id}."}
