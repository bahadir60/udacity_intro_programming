
import media
import fresh_tomatoes

# each movie has movie_title, poster_image, youtube_trailer, year, rating instance

planet_earth2 = media.Movie("Planet Earth II",
                             "https://static1.telepisodes.co/wp-content/uploads/2016/11/Planet-Earth-2.jpg",
                             "https://www.youtube.com/watch?v=c8aFcHFu8QM", 2017, 9.6 )

dunkirk = media.Movie("Dunkirk",
                      "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/dunkirk-poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU", 2017, 8.8 )

valerian = media.Movie("Valerian and the City of a Thousand Planets",
                       "https://i0.wp.com/teaser-trailer.com/wp-content/uploads/Valerian-and-the-City-of-a-Thousand-Planets.jpg?ssl=1",
                       "https://www.youtube.com/watch?v=NNrK7xVG3PM", 2017, 7.0)

girls_trip = media.Movie("Girls Trip",
                       "https://muviefunaticdotcom.files.wordpress.com/2017/06/girlstriposter.jpg",
                       "https://www.youtube.com/watch?v=7jE61BzKmgQ", 2017, 6.7)

landline = media.Movie("Landline",
                       "https://cdn.traileraddict.com/content/amazon-studios/landline-poster.jpg",
                       "https://www.youtube.com/watch?v=ucRVBvMsV2o", 2017, 8.0)

midwife  = media.Movie("Midwife (Sage femme)",
                       "https://cdn.traileraddict.com/content/music-box-films/the-midwife-poster.jpg",
                       "https://www.youtube.com/watch?v=S_FLOFTvqdQ", 2017, 7.1)


toy_story = media.Movie("Toy Story",
                      "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc", 1995, 8.3)


avatar = media.Movie("Avatar",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                   "https://www.youtube.com/watch?v=cRdxXPV9GNQ", 2009, 7.8)


ice_age4 = media.Movie("Ice Age-4",
                     "http://www.zerkaya.com/wp-content/uploads/2012/06/Buz-Devri-4-5.jpg",
                     "https://www.youtube.com/watch?v=hzixp8s4pyg", 2012, 6.6)

war_planet_apes = media.Movie("War for the Planet of the Apes",
                     "https://s-media-cache-ak0.pinimg.com/originals/70/b4/37/70b437a040010e6cd3f09bba554c5930.jpg",
                     "https://www.youtube.com/watch?v=qxjPjPzQ1iU", 2017, 8.1)

spiderman_homecoming = media.Movie( "Spider-Man: Homecoming",
                                    "https://i.redditmedia.com/_f2xAyA2D7AbyflScUU7cwU2fsVuqOOtRoH3_IdZIhM.jpg?w=518&s=eb631b5b47d7c5f687dc891d0dd96662",
                                    "https://www.youtube.com/watch?v=DiTECkLZ8HM", 2017, 8.7)

baby_driver = media.Movie("Baby Driver",
                          "http://www.rowthree.com/wp-content/uploads/2017/06/baby_driver_french.jpg",
                          "https://www.youtube.com/watch?v=z2z857RSfhk", 2017, 8.3)

big_sick = media.Movie("The Big Sick",
                       "http://tr.web.img4.acsta.net/pictures/17/05/03/10/27/081770.jpg",
                       "https://www.youtube.com/watch?v=PJmpSMRQhhs", 2017, 8.1)

wonder_woman = media.Movie("Wonder Woman",
                           "http://pre05.deviantart.net/3262/th/pre/i/2017/153/2/4/wonder_woman__captain_america__the_first_avenger__by_tclarke597-dbba9ie.png",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo", 2017, 7.9)

despicableMe3 = media.Movie("Despicable Me 3",
                            "https://movies.universalpictures.com/media/dm3-adv1sheet-rgb-5-58c818a68f809-1.png?download",
                            "https://www.youtube.com/watch?v=6DBi41reeF0",2017, 6.3)


movies = [planet_earth2,dunkirk ,valerian, girls_trip, landline, midwife, toy_story, avatar, ice_age4,
          war_planet_apes, spiderman_homecoming, big_sick, wonder_woman, baby_driver, despicableMe3]

"""calling fresh tomatoes html and its function for opening movies on browser"""
fresh_tomatoes.open_movies_page(movies)

