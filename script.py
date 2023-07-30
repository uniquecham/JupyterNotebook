# import AnimalShelter class from animal_shelter
from animalShelter import AnimalShelter

a = AnimalShelter()
animal_data = [
    {
        "name":"brawndo",
        "type":"dog"
    },
    {
        "name":"princess",
        "type":"cat"
    }
    
]

for i in animal_data:
    a.create(i)
