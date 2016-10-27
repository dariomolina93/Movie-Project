import webbrowser#include webbroswer that will allow us to display trailer of movie


class Movie():#name of the classs
#documentation
	"""Author: Dario Molina
Date: 10/16
Description: This class provides a way to store movie related information"""

	def __init__(self, movie_title, movie_storyLine, poster_image, trailer_youtube):#constructor of movie object
		self.title = movie_title
		self.storyLine = movie_storyLine
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.movieRatings = 10

	def show_trailer(self):#function that will allow us to display the movie trailer
		webbrowser.open(self.trailer)


