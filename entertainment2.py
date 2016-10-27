import media#include media file where we have the code for the movie objects
import fresh_tomatoes#include this file that allows us to display the movies in a webiste

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc") #creating an instance of an object toy story with the necessary requirements


avatar = media.Movie("Avatar","A marine on an alien planet","http://www.impawards.com/2009/posters/avatar.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")#creating an instance of an object avatar with the necessary requirements

spider_man = media.Movie("Spider Man", "A boy who gets bitten by a spider and becomes a super hero.","http://cdn.collider.com/wp-content/uploads/amazing-spider-man-movie-poster.jpg","https://www.youtube.com/watch?v=__kA4B_ut0s")#creating an instance of an object spider man with the necessary requirements


movies = [toy_story, avatar,spider_man]#storing the movies in a list

fresh_tomatoes.open_movies_page(movies)#opening up browser to display website with movies
