class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        print(f"ЖК называется {self.name}, этажей в доме {self.number_of_floors}, этаж номер {self.new_floor} ")

        if  self.number_of_floors < 1:
            print(f"В ЖК {self.name} Такого этажа не существует")
            return
        if self.new_floor > self.number_of_floors:
            print(f"В ЖК {self.name} Такого этажа не существует")
            return


        for i in range(1,self.new_floor + 1):
            print(i)








hous = House('ЖК Горский', 5)
hous1 = House('Домик в деревне', 7)
hous.go_to(3)
hous1.go_to(8)




