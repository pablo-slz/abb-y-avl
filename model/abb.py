from model.pet import Pet

class ABB():
    def __init__(self):
        self.root = None

    def add(self, pet:Pet):
        if self.root == None:
            self.root = NodeABB(pet)
        else:
            self.root.add(pet)

    def update(self, pet:Pet, id: int):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            self.root.update(pet, id)

    def delete(self, id: int):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        else:
            self.root = self.root.delete(id)

    def inorder(self):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.inorder()

    def preorder(self):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.preorder()

    def postorder(self):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.postorder()

    def breed_count(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.breed_count({})


class NodeABB:
    def __init__(self, pet:Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    def add(self, pet:Pet):
        if pet.id == self.pet.id:
            raise Exception("La mascota ya existe")
        if pet.id < self.pet.id:
            if self.left != None:
                self.left.add(pet)
            else:
                self.left = NodeABB(pet)
        elif self.right != None:
            self.right.add(pet)
        else:
            self.right = NodeABB(pet)
        self.size +=1

    def update(self, pet: Pet, id: int):
        if self.pet.id == id:
            self.pet.name = pet.name
            self.pet.age = pet.age
        elif pet.id < self.pet.id:
            if self.left != None:
                self.left.update(pet, id)
            else:
                raise Exception("No se encontró una mascota con el ID especificado")
        elif self.right != None:
            self.right.update(pet, id)
        else:
            raise Exception("No se encontró una mascota con el ID especificado")

    def delete(self, id: int):
        if id < self.pet.id:
            if self.left is not None:
                self.left = self.left.delete(id)
            else:
                raise Exception("No se encontró una mascota con ese ID")
        elif id > self.pet.id:
            if self.right is not None:
                self.right = self.right.delete(id)
            else:
                raise Exception("No se encontró una mascota con ese ID")
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:

                min_larger_node = self.right.find_min()
                self.pet = min_larger_node.pet
                self.right = self.right.delete(min_larger_node.pet.id)
        return self

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        listPets = []
        if self.left != None:
            listPets.extend(self.left.inorder())
        listPets.append(self.pet.id)
        if self.right != None:
            listPets.extend(self.right.inorder())
        return listPets

    def preorder(self):
        listPets = [self.pet.id]
        if self.left is not None:
            listPets.extend(self.left.preorder())
        if self.right is not None:
            listPets.extend(self.right.preorder())
        return listPets

    def postorder(self):
        listPets = []
        if self.left is not None:
            listPets.extend(self.left.postorder())
        if self.right is not None:
            listPets.extend(self.right.postorder())
        listPets.append(self.pet.id)
        return listPets

    def breed_count(self, breed_dict):
        # Contamos esta raza
        breed = self.pet.breed
        if breed in breed_dict:
            breed_dict[breed] += 1
        else:
            breed_dict[breed] = 1

        # Recorremos la rama izquierda
        if self.left is not None:
            self.left.breed_count(breed_dict)

        # Recorremos la rama derecha
        if self.right is not None:
            self.right.breed_count(breed_dict)

        return breed_dict


class NodeAVL(NodeABB):
    def __init__(self, pet:Pet):
        super().__init__(pet)
        self.height = 1
        self.balance = 1