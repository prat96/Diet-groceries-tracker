import numpy as np


def daily_ingredients():
    ingredients = [ingredients.rstrip('\n') for ingredients in open('ingredients.txt')]
    servings = [servings.rstrip('\n') for servings in open('servings.txt')]
    print(ingredients[0])
    print(servings[0])





if __name__ == '__main__':
    print("Pratheek's diet tracker")
    daily_ingredients()
