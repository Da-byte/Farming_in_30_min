import numpy as np


def plant(farm_land, place_x, place_y):
    farm_land[place_x, place_y] += 1


def harvest(current_harvest, farm_land, place_x, place_y):
    if farm_land[place_x, place_y] == 1:
        current_harvest += 1
        farm_land[place_x, place_y] = 0
        return current_harvest
    else:
        print("There is nothing here! Try planting")


def see_current_harvest(current_harvest):
    print(current_harvest)


def start_game(width, length):
    on = 0
    start = input("Are you ready to farm?(y/n)")
    if start == 'y':
        on = 1

    current_harvest = 0
    farm_land = np.zeros(shape=(width, length))

    while on == 1:
        print(farm_land)

        action = int(input("What do you want to do?(1 = plant corn/2 = harvest)"))
        place_x = int(input("On what row do you want to do this?"))
        place_y = int(input("On what column do you want to do this"))

        if action == 1:
            plant(farm_land, place_x, place_y)
        elif action == 2:
            current_harvest = harvest(current_harvest, farm_land, place_x, place_y)

        current_harvest_indicator = int(input("Do you want to see current harvest?(1 = yes/0 = no)"))
        if current_harvest_indicator == 1:
            see_current_harvest(current_harvest)

        end = int(input("What do you want to do?(1 = wait six months/0 = end game)"))

        if current_harvest == 2:
            print("You have reached 10 batches of harvest and therefore you win!")
            on = 0

        if end == 0:
            on = 0


current_width = int(input("How much width will your land have?"))
current_length = int(input("How much length will your land have?"))
start_game(current_width, current_length)
