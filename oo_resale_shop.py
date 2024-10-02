
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
    def buy_computer (self, computer: Computer) -> None:
        self.inventory.append(computer)
        print(self.inventory)

    # create a function for selling computer
    def sell_computer (self, computer: Computer) -> None:
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item", computer.description, "sold!")
        else: 
            print("Item", computer.description, "not found. Please select another item to sell.")

    # crete a function for refurbishing computer
    def refurbish(self, computer: Computer, new_os: str = None) -> None:
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system= new_os # update details after installing new OS
        else:
            print("Item", computer.description, "not found. Please select another item to refurbish.")
    
    # create a method for printing inventory
    def printInventory(self) -> None:
        if not self.inventory:
            print("The inventory is currently empty.")
        else:
            print("Inventory: ")
            for computer in self.inventory:
                print(computer.description)

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
    ResaleShop_1.refurbish(computer_1, "Windows 12.")
    print("The operating system of",computer_1.description,"is updated to",computer_1.operating_system)

    # print the inventory
    ResaleShop_1.printInventory()

if __name__ == "__main__":
    main()