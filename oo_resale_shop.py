
from typing import Dict, Optional
from computer import *

# create a class for resaleshop
class ResaleShop:

    # attribute of resaleshop
    inventory: list

    # build a constructor for resaleshop
    inventory = []
    def __init__(self, inventory: list):
        self.inventory = inventory

    # create a function for buying computer
    def buy_computer (self, c: Computer) -> None:
        self.inventory.append(c)
        print(self.inventory)

    # create a function for selling computer
    def sell_computer (self, c: Computer) -> None:
        if c in self.inventory:
            self.inventory.remove(c)
            print("Item", c.description, "sold!")
        else: 
            print("Item", c.description, "not found. Please select another item to sell.")

    # crete a function for refurbishing computer
    def refurbish(self, c: Computer, new_os: Optional[str] = None) -> None:
        if c in self.inventory:
            if int(c.year_made) < 2000:
                c.price = 0 # too old to sell, donation only
            elif int(c.year_made) < 2012:
                c.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(c.year_made) < 2018:
                c.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                c.price = 1000 # recent stuff

            if new_os is not None:
                c.operating_system= new_os # update details after installing new OS
        else:
            print("Item", c.description, "not found. Please select another item to refurbish.")
        

def main():
    # make a computer 
    computer_1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # make a second computer
    computer_2 = Computer(
        "Mac Air (2024)",
        "Apple M3",
        512, 16,
        "14.6.1 (23G93)", 2024, 2000
    )

    # make a resaleshop
    inventory_1 = []
    ResaleShop_1 = ResaleShop(inventory_1)

    # buying a computer (add to inventory)
    ResaleShop_1.buy_computer(computer_1)
    ResaleShop_1.buy_computer(computer_2)
    print("There are", len(ResaleShop_1.inventory), "items in stock.")

    # selling a computer (remove from inventory)
    ResaleShop_1.sell_computer(computer_2)
    print("There is", len(ResaleShop_1.inventory), "item in stock.")
    
    # refurbishing a computer
    ResaleShop_1.refurbish(computer_1, "Windows 12")
    print("The operating system of",computer_1.description,"is updated to",computer_1.operating_system)

if __name__ == "__main__":
    main()