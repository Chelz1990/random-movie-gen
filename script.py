#import sys and random

import sys, random

#greet the user

print("Hey there! I'm going to help you decide what to watch!")

# create the movie list
movies = []

# script to get user input
addmovie = input("type 1 to add a show/movie to the list, 2 to select a random move, or 3 to quit: ")
while addmovie == '1' or addmovie == '3' or addmovie == '2':
    if addmovie == '1':
        movies.append(input("Okay! Please enter the title of the show/movie: "))
    elif addmovie == '3':
        print ("Happy watching!")
        sys.exit()
    elif addmovie == '2':
        break
    addmovie = input("type 1 to add a show/movie to the list, 2 to select a random move, or 3 to quit: ")


# selection of random choice after user input
random_movie = random.choice(movies)
print (random_movie)

#selection of random choice without user input
