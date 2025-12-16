# 1. Ovoz chiqarish polimorfizmi

class Bird:
    def make_sound(self):
        pass


class Duck(Bird):
    def make_sound(self):
        return "Quack quack"


class Sparrow(Bird):
    def make_sound(self):
        return "Chirp chirp"


class Owl(Bird):
    def make_sound(self):
        return "Hoot hoot"


# 2. Hisoblash polimorfizmi

class Calculator:
    def calculate(self, a, b):
        pass


class Adder(Calculator):
    def calculate(self, a, b):
        return a + b


class Subtractor(Calculator):
    def calculate(self, a, b):
        return a - b


class Multiplier(Calculator):
    def calculate(self, a, b):
        return a * b


# 3. To‘lov turlari polimorfizmi

class Payment:
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        return f"{amount} so'm naqd to‘landi"


class CardPayment(Payment):
    def process_payment(self, amount):
        return f"{amount} so'm karta orqali to‘landi"


class MobilePayment(Payment):
    def process_payment(self, amount):
        return f"{amount} so'm mobil to‘lov orqali to‘landi"


# 4. Ovqat tayyorlash polimorfizmi

class Chef:
    def cook(self):
        pass


class PizzaChef(Chef):
    def cook(self):
        return "Pizza tayyorlandi"


class PastaChef(Chef):
    def cook(self):
        return "Pasta tayyorlandi"


class SushiChef(Chef):
    def cook(self):
        return "Sushi tayyorlandi"


# 5. Nashr qilish polimorfizmi

class Publisher:
    def publish(self, content):
        pass


class NewspaperPublisher(Publisher):
    def publish(self, content):
        return f"Gazetada chop etildi: {content}"


class MagazinePublisher(Publisher):
    def publish(self, content):
        return f"Jurnalda chop etildi: {content}"


class OnlinePublisher(Publisher):
    def publish(self, content):
        return f"Internetda e'lon qilindi: {content}"
