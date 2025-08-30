# smartphone.py

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__total_storage = storage      # Private: total storage (e.g., 256GB)
        self.__available_storage = storage  # Private: track remaining space
        self.battery = 100

    def call(self, number):
        if self.battery > 5:
            print(f"{self.brand} {self.model} is calling {number}...")
            self.battery -= 5
        else:
            print("Battery too low to make a call.")

    def charge(self, amount=100):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}% battery.")

    def use_storage(self, amount):
        if amount <= self.__available_storage:
            self.__available_storage -= amount
            print(f"{amount}GB used. Remaining storage: {self.__available_storage}GB / {self.__total_storage}GB")
        else:
            print(f"Not enough storage! Only {self.__available_storage}GB available.")

    def get_storage_info(self):
        return f"Available: {self.__available_storage}GB / {self.__total_storage}GB"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.battery}% battery)"


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def play_game(self, game, intensity=20):
        if self.battery > intensity:
            print(f"Playing {game} with {self.cooling_system} cooling system.")
            self.battery -= intensity
        else:
            print("Battery too low to play games.")

    # Polymorphism: Fast charging with boost
    def charge(self, amount=50):
        boosted = amount * 1.5
        self.battery = min(100, self.battery + boosted)
        print(f"{self.brand} {self.model} fast charged to {self.battery}% battery! (+{boosted:.1f}%)")
        return self


class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.battery < 10:
            print("Battery too low to take photos.")
            return
        if self.use_storage(2):
            print(f"📸 {self.camera_megapixels}MP photo captured!")
            self.battery -= 10

    def use_storage(self, amount):
        # Override to return True/False for photo logic
        available = getattr(self, '_Smartphone__available_storage')  # Access private parent attr
        if amount <= available:
            object.__setattr__(self, '_Smartphone__available_storage', available - amount)
            print(f"{amount}GB used. Remaining: {available - amount}GB / {getattr(self, '_Smartphone__total_storage')}GB")
            return True
        else:
            print("📷 Not enough storage to save photo!")
            return False

    # Polymorphism: Optimized charging
    def charge(self, amount=100):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} optimized charging completed: {self.battery}% battery ⚙️")
        return self


# === DEMONSTRATION ===
if __name__ == "__main__":
    print("=== Regular Smartphone: iPhone 16 ===")
    iphone16 = Smartphone("Apple", "iPhone 16", 256)
    iphone16.call("123-456-7890")
    iphone16.use_storage(30)
    iphone16.charge(20)
    print()

    print("=== Gaming Smartphone: iPhone 16 Pro (Gaming Edition) ===")
    gaming_phone = GamingSmartphone("Apple", "iPhone 16 Pro Max", 512, "Liquid Cooling")
    gaming_phone.play_game("Genshin Impact", intensity=40)
    gaming_phone.charge(30)
    print()

    print("=== Camera Smartphone: iPhone 16 Pro with 108MP Camera ===")
    camera_phone = CameraSmartphone("Apple", "iPhone 16 Pro", 256, 108)
    camera_phone.take_photo()
    camera_phone.take_photo()
    camera_phone.charge(40)