# import tkinter to allow for the creation of windows
import tkinter as tk

# function for when it is time to save the entries in the window into a text file.
def save_recipe():

    # entry_name is the name of the recipe
    # Obtain the variable containing the recipe name and put it into a function-specific variable recipe_name
    recipe_name = entry_name.get()
    
    # text_ingredients is the list of ingredients given in the ingredients box
    # obtain the variable containing the ingredients and put it into a function-specific variable ingredients
    ingredients = text_ingredients.get("1.0", tk.END)
    
    # steps are the steps for cooking the recipe given in the box.
    # obtain the variable containing the steps for the recipe & put it into a function-specific variable steps
    steps = text_steps.get("1.0", tk.END)

    # Make sure that none of the above fields are left empty
    if not recipe_name or not ingredients or not steps:
        return

    # Open/Create a text file with the name of the recipe, and write the listed variables into each position
    with open(f"{recipe_name}.txt", "w") as file:
    
        file.write(f"Recipe Name: {recipe_name}\n\n\n")
        
        file.write("Ingredients:\n")
        file.write(ingredients)
        file.write("\n\n\n")
        
        file.write("Steps:\n")
        file.write(steps)

    # Clear the input fields after saving
    entry_name.delete(0, tk.END)
    text_ingredients.delete("1.0", tk.END)
    text_steps.delete("1.0", tk.END)


##### MAIN WINDOW #####
# Create the main window
window = tk.Tk()
window.title("Recipe Manager")


##### RECIPE NAME #####
# Label the entry for the box for the recipe name
label_name = tk.Label(window, text="Recipe Name:")
label_name.pack()

# Store what is in the recipe name box in variable entry_name
entry_name = tk.Entry(window)
entry_name.pack()


##### INGREDIENTS LIST #####
# Label the entry for the box of the ingredients list
label_ingredients = tk.Label(window, text="Ingredients:")
label_ingredients.pack()

# Store what is in the ingredients box into variable text_ingredients
text_ingredients = tk.Text(window, height=5, width=40)
text_ingredients.pack()

##### STEPS #####
# Label the box containing the steps in the window
label_steps = tk.Label(window, text="Steps:")
label_steps.pack()

# Store what is put into the steps window into variable text_steps
text_steps = tk.Text(window, height=10, width=40)
text_steps.pack()

##### SAVE BUTTON #####
# Button to Save Recipe to a txt file
save_button = tk.Button(window, text="Save Recipe", command=save_recipe)
save_button.pack()

# Start the GUI main loop
window.mainloop()