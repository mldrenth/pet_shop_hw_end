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