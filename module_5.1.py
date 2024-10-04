class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        for i in range(1, int(new_floor + 1)):
            if new_floor > self.number_of_floors or new_floor == 0:
                print('Такого этажа не существует')
                break
            else:
                print(i)

house_love = House('Пятиэтажка', 5)
house_love.go_to(5)