def print_name_and_student_id(My_data):

    full_name = My_data['name']
    name_split = full_name.split() # Split the full name into a list of strings

    print(f"My full name is {My_data['name']}, but you can call me Sir {name_split[0]}.")
    print(f"My student ID is {My_data['student ID']}.\n") 


    return

def print_toppings_list(My_data):

    print("My favourite pizza toppings are:")

    for _ in My_data['pizza toppings']:
        print(f"- {_}")
    print() 

    return

def add_pizza_topping(My_data, newer_topping):

    for _ in newer_topping:

        My_data['pizza toppings'].append(_)
        My_data['pizza toppings'] = [topping.lower() for topping in My_data['pizza toppings']]
        My_data['pizza toppings'].sort()

    return

def add_movie(My_data, title, genre):

    new_movie = {'title': title, 'genre': genre}
    My_data['Movies'].append(new_movie) # This line adds the new movie to the existing list of movies in My_data.
   
    return

def print_genres(My_data):
    genres = [movie['genre'] for movie in My_data['Movies']]
    if len(genres) > 1:
        genres_str = ", ".join(genres[:-1]) + f", {genres[-1]}"
    else:
        genres_str = "".join(genres)
    print(f"I like to watch {genres_str} movies.\n")

    return 

def print_movie_titles(movie_list):
    titles = [movie['title'].title() for movie in movie_list]
    if len(titles) > 1:
        titles_str = ", ".join(titles[:-1]) + f", and {titles[-1]}"
    else:
        titles_str = "".join(titles)
    print(f"Some of my favourite movies are {titles_str}!\n")

    return

def main():
    My_data = {

'name':'Sanamdeep Singh', 
'student ID': '10333491',
'pizza toppings':['PEPPERONI', 'MUSHROOMS', 'ONIONS', 'EXTRA CHEESE'],
'Movies':[

    {'title': 'The Shawshank Redemption', 'genre': 'Drama'},
    {'title': 'The Godfather', 'genre': 'Crime'},
]
    }

    print_name_and_student_id(My_data) 

    print_toppings_list(My_data)

    new_toppings = ['OLIVES', 'GREEN PEPPERS']
    add_pizza_topping(My_data, new_toppings)
    print_toppings_list(My_data)

    add_movie(My_data, 'Inception', 'Sci-Fi') # This line adds the movie "Inception" with the genre "Sci-Fi" to the list of movies in My_data.

    print_genres(My_data)
    print_movie_titles(My_data['Movies'])











    return



if __name__ == "__main__":
    main()