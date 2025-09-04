# Lists are created using square brackets [], and items are separated by commas.
# Lists maintain the order of items, and you can access individual items using their index, starting from 0. 
# For instance, fav_movies[0] would give you "The Little Princess"

fav_movies = ["The Little Princess", "The King and I", "The Lego Movie"]

print(fav_movies[0])
#--> The Little Princess

# To find the length of a list in Python, you can use the len() function. 
# For example, if you have a list called fav_movies, you can find its length by using:
print(len(fav_movies))
#--> 3

fav_movies.append("Finding Nemo")

print(len(fav_movies))
#--> 4

fav_movies.insert(1, "Batman")
print((fav_movies))

# Remove 1 item
del(fav_movies[1])
print(fav_movies)

