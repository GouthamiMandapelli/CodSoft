import random

print("\n===================================")
print("      MOVIE RECOMMENDATION")
print("===================================\n")

movies = {

    "action": [
        "John Wick",
        "Avengers: Endgame",
        "Mad Max: Fury Road",
        "Extraction"
    ],

    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar"
    ],

    "motivation": [
        "The Pursuit of Happyness",
        "Rocky",
        "Ford v Ferrari",
        "Creed"
    ],

    "comedy": [
        "3 Idiots",
        "Free Guy",
        "Jumanji",
        "The Mask"
    ]
}

print("Available Movie Genres:\n")

for genre in movies:
    print("-", genre)

user_genre = input("\nChoose a genre: ").lower()

if user_genre in movies:

    recommended_movies = random.sample(
        movies[user_genre],
        3
    )

    print("\n===================================")
    print("     YOUR MOVIE RECOMMENDATIONS")
    print("===================================\n")

    for index, movie in enumerate(recommended_movies, start=1):
        print(f"{index}. {movie}")
else:

    print("\nGenre not available.")

print("\nThank you for using the system.")
