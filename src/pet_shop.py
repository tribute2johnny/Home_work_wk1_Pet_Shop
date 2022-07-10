# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(total):
    total = total["admin"]['total_cash']
    return total


def add_or_remove_cash(total_petshop, cash):
    total_petshop["admin"]["total_cash"] += cash






def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets, pets_sold):
    pets["admin"]["pets_sold"] = pets_sold
    return pets

    
def get_stock_count(stock_update):
    return len(stock_update["pets"])

    
#makes a list to test if breeds are present in the dictionary    
def get_pets_by_breed(pets, breed):
    total_pets = []
    for pet in pets["pets"]:
        if pet["breed"] == breed:
            total_pets.append(pet)
    return total_pets


# test runs through dictionary to look for a name in list
def find_pet_by_name(list, pet_name):
    for each_pet in list["pets"]:
         if each_pet["name"] == pet_name:
          return each_pet
        
 # can call the function above to find the name in the list(had to get some help with this one)   
def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet)
      
def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(count):
    return len(count["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
    
    
      

    
            
        
    
    






   

