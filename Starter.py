movies = []

# Example movie structure:
# {"title": "Movie Name", "genre": "Genre", "rating": "8"}

def show_menu():
    print("\nMovie Collection Manager")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Exit")

def add_movie():
    # TODO: ask user for title, genre and rating
    # TODO: store the movie in the movies list
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")
    rating = input("Enter rating (0-10): ")

    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    movies.append(movie)
    print("Movie added successfully!")


def view_movies():
    if not movies:
        print("No movies available")
    
    for movie in movies:
        print("Title:", movie["title"])
        print("Genre:", movie["genre"])
        print("Rating:", movie["rating"])
        print("-" * 30)


def search_movie():
    # TODO: ask user for movie title
    # TODO: search movie in the list
    # TODO: display result
    search = input("Enter movie title to search: ")

for movie in movies:
    if search.lower() == movie["title"].lower():
        print("Found!")
        print("Title:", movie["title"])
        print("Genre:", movie["genre"])
        print("Rating:", movie["rating"])
        break
else:
    print("Movie not found.")


def main():
    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            view_movies()

        elif choice == "3":
            search_movie()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


main()
