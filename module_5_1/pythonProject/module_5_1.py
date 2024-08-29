class Hause:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = new_floor
        print(f"ЖК называется {self.name}, Номер этажа {self.new_floor}")
        if new_floor > self.number_of_floors:
            print(f"Такого этажа не существует")
        elif new_floor < 1:
            print(f"Такого этажа не существует")





haus = Hause('ЖК Эльбрус',30 )
