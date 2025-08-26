# creating and initializing the class
class Device:
    def __init__(self, brand: str, model:str):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# The class Smatphone inheritize the atribute of Device class
class Smartphone(Device):
    def __init__(self, brand:str, model:str, storage:str, battery:int):
        super().__init__(brand, model)  
        self.storage = storage
        self.battery = battery

    def call(self, number:str):
        print(f"Calling {number} from {self.info()}...")

    def charge(self, amount:int):
        self.battery += amount
        print(f"Charging... Battery is now {self.battery}%")

    def install_app(self, app:str):
        print(f"Installing {app} on {self.info()}...")


# objects of the class smartphone
iphone = Smartphone("Apple", "iPhone 14", "128GB", 50)
huawei = Smartphone("Huawei", "P 20 lite", "256GB", 80)

iphone.call("+258 8611 44 847")
iphone.charge(20)
huawei.install_app("WhatsApp")
