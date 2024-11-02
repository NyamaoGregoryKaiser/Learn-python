#+++++Lists++++++++++++++
print("=====Lists========")
favorite_games = ["GTA","FC24","Python Blocks"]
print("Teacher's favorite games: ", favorite_games)

##add a new game
favorite_games.append("Fortnite")
print ("updated favorite games for teacher: ", favorite_games)



# ===== Dictionaries =====
print("\n=== Dictionaries ===")
# Create a dictionary of animals and their sounds
animal_sounds = {
    "cat": "meow",
    "dog": "bark",
    "cow": "moo"
}
print("Animal Sounds:", animal_sounds)

# Add a new animal and sound
animal_sounds["duck"] = "quack"
print("Updated Animal Sounds:", animal_sounds)

# Retrieve the sound of a specific animal
print("Sound of a dog:", animal_sounds.get("dog"))

# Loop through the dictionary and print each animal and sound
print("Animals and their sounds:")
for animal, sound in animal_sounds.items():
    print(f"The {animal} goes '{sound}'")


# ===== Tuples =====
print("\n=== Tuples ===")
# Create a tuple of coordinates
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Attempt to change a tuple item (will throw an error if uncommented)
# coordinates[0] = 15  # Uncomment to see that tuples are immutable

# Use the tuple in a context where data should stay the same
character_position = coordinates
print("Character Position (Immutable):", character_position)

# ===== Recap Challenge =====
print("\n=== Recap Challenge ===")
# List of favorite movies
favorite_movies = ["Incredibles", "Toy Story", "Frozen"]
print("Favorite Movies:", favorite_movies)

# Dictionary of friends and their ages
friends_ages = {
    "Alice": 10,
    "Bob": 12,
    "Charlie": 11
}
print("Friends and their ages:", friends_ages)

# Tuple of lucky numbers
lucky_numbers = (7, 3, 11)
print("Lucky Numbers:", lucky_numbers)
