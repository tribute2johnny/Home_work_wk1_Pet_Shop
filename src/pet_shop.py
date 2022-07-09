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
        
    
     
    
    






   

