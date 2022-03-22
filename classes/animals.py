class Animal:
    def __init__(self, name, type_animal):
        self.name = name
        self.type = type_animal

    def make_sound(self):
        print(f'{self.type} makes sound')


class Kitty(Animal):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name, "cat")

    def make_sound(self):
        print(f'{self.color} cat myaowing')
        super(Kitty, self).make_sound()


all_animals = [Animal("burenka", "cow"), Animal("sharik", "dog"), Kitty("bublik", "orange")]
for i in range(0, len(all_animals)):
    current_animal = all_animals[i]
    print(current_animal.name)
    current_animal.make_sound()
