from model.abb import ABB
from model.pet import Pet


class ABBService():
    def __init__(self):
        self.abb = ABB()
        # llenar ABB

        self.abb.add(Pet(id=7,name="Lulu",age=13, race="labrador"))
        rocky = Pet(id=2,name="Rocky",age=5, race = "pitbull")
        self.abb.add(rocky)

    def exists(self, id: int):
        current = self.abb.root
        while current:
            if current.pet.id == id:
                return True  # El ID ya existe en el árbol
            elif id < current.pet.id:
                current = current.left  # Moverse a la izquierda
            else:
                current = current.right  # Moverse a la derecha
        return False  # Si se recorrió todo el árbol y no se encontró el ID

    def breed_count(self) -> dict:
        breed_counts = {}

        def count_race(node):
            if node:
                breed_counts[node.pet.race] = breed_counts.get(node.pet.race, 0) + 1
                count_race(node.left)
                count_race(node.right)

        count_race(self.abb.root)
        return breed_counts

    def delete_pet(self, id: int) -> bool:
        #""""Elimina una mascota por su ID en el ABB."""

        def delete_node(node, id):
            if not node:
                return None  # No encontrado
            if id < node.pet.id:
                node.left = delete_node(node.left, id)
            elif id > node.pet.id:
                node.right = delete_node(node.right, id)
            else:
                # Caso 1: Sin hijos
                if not node.left and not node.right:
                    return None
                    # Caso 2: Un solo hijo
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                    # Caso 3: Dos hijos
                temp = get_min(node.right)
                node.pet = temp.pet
                node.right = delete_node(node.right, temp.pet.id)

            return node

        def get_min(node):
            """Encuentra el nodo con el menor ID (más a la izquierda)."""
            while node.left:
                node = node.left
            return node

        if not self.exists(id):
            return False  # No encontrado

        self.abb.root = delete_node(self.abb.root, id)
        return True  # Eliminado con éxito

    def update_pet(self, id: int, new_name: str = None, new_age: int = None, new_race: str = None) -> bool:
        current = self.abb.root

        while current:
            if current.pet.id == id:
                if new_name is not None:
                    current.pet.name = new_name
                if new_age is not None:
                    current.pet.age = new_age
                if new_race is not None:
                    current.pet.race = new_race
                return True  # Mascota actualizada con éxito

            if id < current.pet.id:
                current = current.left  # Ir a la izquierda
            else:
                current = current.right  # Ir a la derecha

        return False  # No se encontró el ID
