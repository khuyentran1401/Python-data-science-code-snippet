import json
pet = dict(
	kind="dog",
	name= "Bim Bim",
	age=7,
	favorite_food='yogurt'
)
print(json.dumps(pet))
# {"kind": "dog", "name": "Bim Bim", "age": 7, "favorite_food": "yogurt"}

print(json.dumps(pet, indent=4))
""" 
{
    "kind": "dog",
    "name": "Bim Bim",
    "age": 7,
    "favorite_food": "yogurt"
}
"""