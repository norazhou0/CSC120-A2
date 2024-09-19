# create a class for computer
class Computer:

    # attricutes of computer
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # build a constructor for computer 
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # create a function for updating price
    def update_price (self, new_price: int) -> None:
        self.price = new_price
        print("The price is updated to $",self.price)

    # create a function for updating OS
    def update_OS (self, new_os: str) -> None:
        self.operating_system = new_os
        print("The operating system is updated to",self.operating_system)

def main():
    # make a computer
    computer_1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    print(computer_1.description)

    # updating a computer's price
    computer_1.update_price (2000)

    # updating a computer's OS
    computer_1.update_OS ("14.6.1 (23G93)")
    
if __name__ == "__main__":
    main()

   

