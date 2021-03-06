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

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer,cash_amount):
    customer["cash"] -= cash_amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]
        

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None:
        return
    elif customer_can_afford_pet(customer,pet) == True: 
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(pet_shop, pet)
        increase_pets_sold(pet_shop,len(customer["pets"]))
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop,pet["price"])
    
        
        

