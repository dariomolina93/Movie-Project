import media
import fresh_tomatoes

'''
Author: Dario Molina
Date: 10/21/16
Description: Create instances of object Movie, where program is compiled and \
run it creates the website displaying movie titles.
'''
# creating an instance of an object Toy Story with the necessary arguments as \
# title, movie description, poster url, and trailer url

toy_story = media.Movie(
	"Toy Story", 
	"A story of a boy and his toys that come to life",
	"http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", # noqa
	"https://www.youtube.com/watch?v=KYz2wyBy3kc") # noqa

# creating an instance of an object Avatar with the necessary arguments as \
# title, movie description, poster url, and trailer url

avatar = media.Movie(
	"Avatar",
	"A marine on an alien planet",
	"http://www.impawards.com/2009/posters/avatar.jpg", # noqa
	"https://www.youtube.com/watch?v=5PSNL1qE6VY") # noqa

# creating an instance of an object Spider Man with the necessary arguments as \
# title, movie description, poster url, and trailer url

spider_man = media.Movie(
	"Spider Man", 
	"A boy who gets bitten by a spider and becomes a super hero.",
	"http://cdn.collider.com/wp-content/uploads/amazing-spider-man-movie-poster.jpg", # noqa
	"https://www.youtube.com/watch?v=__kA4B_ut0s") # noqa

# storing the movies in a list

movies = [toy_story, avatar,spider_man]

# opening up browser to display website with movies

fresh_tomatoes.open_movies_page(movies)
