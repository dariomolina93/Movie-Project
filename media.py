import webbrowser


# name of the class

class Movie():

# documentation

	"""Author: Dario Molina
Date: 10/21/16
Description: This class provides a way to store movie related information"""

# constructor of movie object

	def __init__(self, movie_title, movie_storyLine, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyLine = movie_storyLine
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.movieRatings = 10

# function that will allow us to display the movie trailer

	def show_trailer(self):
		webbrowser.open(self.trailer)


