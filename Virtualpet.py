import tkinter as tk
from tkinter import messagebox
import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.happiness = 70  # Start with lower happiness
        self.hunger = 30     # Start with hunger, so it isn't always full

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 15
            self.health += 5
            self.update_status()
        else:
            messagebox.showinfo("Info", f"{self.name} is not hungry!")

    def play(self):
        if self.happiness < 100:
            self.happiness += 15
            self.update_status()
        else:
            messagebox.showinfo("Info", f"{self.name} is already very happy!")

    def update_status(self):
        self.hunger += 10  # Hunger increases over time automatically
        self.happiness -= 5  # Happiness decreases if not interacted with
        if self.hunger > 50:
            self.health -= 15  # If hunger is too high, health decreases
        if self.happiness < 20:
            self.health -= 10  # If happiness is too low, health decreases
        if self.health <= 0 or self.happiness <= 0:
            self.pet_passed_away()
        else:
            pet_health_var.set(f"Health: {self.health}")
            pet_happiness_var.set(f"Happiness: {self.happiness}")
            pet_hunger_var.set(f"Hunger: {self.hunger}")

    def pet_passed_away(self):
        messagebox.showinfo("Game Over", f"{self.name} has passed away due to neglect.")
        root.quit()

    def live(self):
        while self.health > 0 and self.happiness > 0:
            time.sleep(2)
            self.update_status()

# Create the main window
root = tk.Tk()
root.title("Virtual Pet Game")
root.geometry("400x400")

# Create an instance of the VirtualPet class
pet_name = "Fluffy"
pet = VirtualPet(pet_name)

# Create variables to hold pet's health, happiness, and hunger
pet_health_var = tk.StringVar()
pet_happiness_var = tk.StringVar()
pet_hunger_var = tk.StringVar()

pet_health_var.set(f"Health: {pet.health}")
pet_happiness_var.set(f"Happiness: {pet.happiness}")
pet_hunger_var.set(f"Hunger: {pet.hunger}")

# Create labels to display the pet's stats
health_label = tk.Label(root, textvariable=pet_health_var, font=("Helvetica", 14))
health_label.pack()

happiness_label = tk.Label(root, textvariable=pet_happiness_var, font=("Helvetica", 14))
happiness_label.pack()

hunger_label = tk.Label(root, textvariable=pet_hunger_var, font=("Helvetica", 14))
hunger_label.pack()

# Function to handle feeding the pet
def feed_pet():
    pet.feed()

# Function to handle playing with the pet
def play_with_pet():
    pet.play()

# Create buttons to feed the pet, play with it, and check status
feed_button = tk.Button(root, text="Feed", font=("Helvetica", 14), command=feed_pet)
feed_button.pack(pady=10)

play_button = tk.Button(root, text="Play", font=("Helvetica", 14), command=play_with_pet)
play_button.pack(pady=10)

exit_button = tk.Button(root, text="Quit", font=("Helvetica", 14), command=root.quit)
exit_button.pack(pady=20)

# Start the main event loop
root.mainloop()
