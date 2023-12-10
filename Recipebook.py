class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {'Ingredients': ingredients, 'Instructions': instructions}

    def get_recipe(self, name):
        return self.recipes.get(name, "Recipe not found")

    def list_recipes(self):
        return list(self.recipes.keys())


def main():
    book = RecipeBook()
    while True:
        print("\nRecipe Book Application")
        print("1. Add a Recipe")
        print("2. View a Recipe")
        print("3. List all Recipes")
        print("4. Exit")
        choice = input("Enter your choice: ")
#add
        if choice == '1':
            name = input("Enter the name of the recipe: ")
            ingredients = input("Enter the ingredients (separated by comma): ")
            instructions = input("Enter the instructions: ")
            book.add_recipe(name, ingredients, instructions)
            print("Recipe added.")
#view
        elif choice == '2':
            name = input("Enter the name of the recipe to view: ")
            recipe = book.get_recipe(name)
            if recipe != "Recipe not found":
                print("\nRecipe for", name)
                print("Ingredients:", recipe['Ingredients'])
                print("Instructions:", recipe['Instructions'])
            else:
                print(recipe)
#list
        elif choice == '3':
            recipes = book.list_recipes()
            print("\nList of Recipes:")
            for recipe in recipes:
                print(recipe)
#exit
        elif choice == '4':
            print("Exiting Recipe Book Application.")
            break
#If user puts in weird things
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
