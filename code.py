def show_menu():
    print('''\n--- Movie Watchlist Menu ---
1. Add to Watchlist
2. Remove from Watchlist
3. View Watchlist
4. Exit
''')

def add_movie(watchlist):
    movie = input("Enter movie name to add: ").strip().lower()
    if movie:
        if movie not in watchlist:
            watchlist.append(movie)
            print(f"'{movie}' added to watchlist.")
        else:
            print("Movie already exists.")
    else:
        print("Movie name cannot be empty.")

def remove_movie(watchlist):
    movie = input("Enter movie name to remove: ").strip().lower()
    if movie in watchlist:
        watchlist.remove(movie)
        print(f"'{movie}' removed from watchlist.")
    else:
        print("Movie not found in watchlist.")

def view_watchlist(watchlist):
    if not watchlist:
        print("Your watchlist is empty.")
    else:
        print("\nYour Watchlist:")
        for i, movie in enumerate(watchlist, start=1):
            print(f"{i}. {movie}")


watchlist = []

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_movie(watchlist)
    elif choice == "2":
        remove_movie(watchlist)
    elif choice == "3":
        view_watchlist(watchlist)
    elif choice == "4":
        print("Thanks for using...")
        break
    else:
        print("Invalid choice. Please select 1-4.")
