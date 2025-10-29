from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Smart Nutrition Planner")

mainframe = ttk.Frame(root, padding=(15, 15, 50, 50))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Inputs
user_prof = StringVar()
prof_entry = ttk.Entry(mainframe, width=7, textvariable=user_prof)
prof_entry.grid(column=2, row=1, sticky=(W, E))

diet_pref = StringVar()
diet_entry = ttk.Entry(mainframe, width=7, textvariable=user_prof)
diet_entry.grid(column=4, row=1, sticky=(W, E))

goal = StringVar()
goal_entry = ttk.Entry(mainframe, width=7, textvariable=user_prof)
goal_entry.grid(column=6, row=1, sticky=(W, E))

allergies = StringVar()
allergy_entry = ttk.Entry(mainframe, width=7, textvariable=user_prof)
allergy_entry.grid(column=2, row=2, sticky=(W, E))

avalIngredients = StringVar()
avalIngredients = ttk.Entry(mainframe, width=7, textvariable=user_prof)
avalIngredients.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="user_profile").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Dietary Preferences").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Goal").grid(column=5, row=1, sticky=W)
ttk.Label(mainframe, text="Allergies").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Available Ingredients").grid(column=3, row=2, sticky=W)

# Must impliment function for calculation
ttk.Button(mainframe, text="Create").grid(column=6, row=2, sticky=W)

# Outputs

# Meal A
titleA = StringVar()
ingredientsA = StringVar()
instructionsA = StringVar()
goalReasonA = StringVar()
nutirentA = StringVar()
ttk.Label(mainframe, textvariable=titleA).grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Meal Option A").grid(column=2, row=6, sticky=W)
ttk.Label(mainframe, text="Ingredients").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, textvariable=ingredientsA).grid(column=2, row=8, sticky=W)
ttk.Label(mainframe, text="Instructions").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, textvariable=instructionsA).grid(column=2, row=9, sticky=W)
ttk.Label(mainframe, text="Goal Justification").grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, textvariable=goalReasonA).grid(column=2, row=10, sticky=W)
ttk.Label(mainframe, text="Nutritional Breakdown").grid(column=1, row=11, sticky=W)
ttk.Label(mainframe, textvariable=nutirentA).grid(column=2, row=11, sticky=W)

# Meal B
titleB = StringVar()
ingredientsB = StringVar()
instructionsB = StringVar()
goalReasonB = StringVar()
nutirentB = StringVar()
ttk.Label(mainframe, textvariable=titleB).grid(column=4, row=7, sticky=W)
ttk.Label(mainframe, text="Meal Option B").grid(column=5, row=6, sticky=W)
ttk.Label(mainframe, text="Ingredients").grid(column=4, row=8, sticky=W)
ttk.Label(mainframe, textvariable=ingredientsB).grid(column=5, row=8, sticky=W)
ttk.Label(mainframe, text="Instructions").grid(column=4, row=9, sticky=W)
ttk.Label(mainframe, textvariable=instructionsB).grid(column=5, row=9, sticky=W)
ttk.Label(mainframe, text="Goal Justification").grid(column=4, row=10, sticky=W)
ttk.Label(mainframe, textvariable=goalReasonB).grid(column=5, row=10, sticky=W)
ttk.Label(mainframe, text="Nutritional Breakdown").grid(column=4, row=11, sticky=W)
ttk.Label(mainframe, textvariable=nutirentB).grid(column=5, row=11, sticky=W)

# ETC
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()