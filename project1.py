#я сделал систему кормления виртуальных котов, где есть проверка голодны ли они

class Cat:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger

class Life:
    def __init__(self):
        self.hunger_status = []

    def check_hunger(self, name, hunger):
        if hunger==True:
            self.feed_cat(name, hunger)
        else:
            print(name + " не голоден")

    def feed_cat(self, name, hunger):
        cat = Cat(name, hunger)
        cat.hunger = False
        self.hunger_status.append(cat)
        print(name + " был покормлен")

    def display_hunger_status(self):
        if not self.hunger_status:
            print("Котик хочет есть")
        else:
            print("Список котов и их статус голода:")
            for cat in self.hunger_status:
                print(cat.name, "голоден" if cat.hunger else "сыт")


life = Life()
life.check_hunger('masha', True)
life.check_hunger('barsik', False)
life.display_hunger_status()
