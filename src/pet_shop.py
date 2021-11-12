# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
     return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,cash_amount):
    current_total_cash = pet_shop["admin"]["total_cash"]
    pet_shop["admin"]["total_cash"] = current_total_cash + cash_amount
    
    return current_total_cash

def get_pets_sold(pet_shop):
    return  pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pet_amount):
    current_total_pets_sold = pet_shop["admin"]["pets_sold"]
    pet_shop["admin"]["pets_sold"] = current_total_pets_sold + pet_amount
    
    return current_total_pets_sold

def get_stock_count(pet_shop):
   return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,breed):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

def remove_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)
