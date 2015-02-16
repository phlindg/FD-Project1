# -*- coding: utf-8 -*-
#Not sure why I had to add that, but it kept popping up as I tried to save, so I did.

#these are the imports I used in this project
import medias
import fresh_tomatoes



#an instance of the class Movies()
salt = medias.Movies("Salt",
                   "100 min",
                   "Angelina Jolie, Chiwetel Ejiofor",
                   "A CIA agent goes on the run after a defector accuses her of being a Russian spy.",
                   "http://upload.wikimedia.org/wikipedia/en/5/52/Salt_film_theatrical_poster.jpg",
                   "https://www.youtube.com/watch?v=QZ40WlshNwU")
#an instance of the class Movies()
up = medias.Movies("Up",
                   "96 min",
                   "Edward Asner, Jordan Nagai",
                   "To avoid being taken away to a nursing home, an old widower tries to fly his home to Paradise Falls, South America, along with a boy scout who accidentally lifted off with him.",
                   "http://upload.wikimedia.org/wikipedia/en/0/05/Up_(2009_film).jpg",
                   "https://www.youtube.com/watch?v=pkqzFUhGPJg")
#an instance of the class Movies()
kingdom_of_heaven = medias.Movies("Kingdom of Heaven",
                                "144 min",
                                "Orlando Bloom, Eva Green",
                                "Jerusalem at warBalian of Ibelin travels to Jerusalem during the crusades of the 12th century, and there he finds himself as the defender of the city and its people.",
                                "http://upload.wikimedia.org/wikipedia/en/thumb/9/9e/KoHposter.jpg/220px-KoHposter.jpg",
                                "https://www.youtube.com/watch?v=Kfq9U2tWWGo")


#an instance of the class TV_Show()
bron = medias.TV_Show("Bron",
                      "40 min",
                      "Sofia Helin, Kim Bodnia",
                      "Murders on ÖresundsbronWhen a body is found on the bridge between Denmark and Sweden, right on the border, Danish inspector Martin Rohde and Swedish Saga Norén have to share jurisdiction and work together to find the killer.",
                      "2",
                      "10",
                      "http://ia.media-imdb.com/images/M/MV5BMTM3NjQyMTAwMF5BMl5BanBnXkFtZTcwMDQ2Mjc0OQ@@._V1_SY317_CR3,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=EzidbHbvAuw")
#an instance of the class TV_Show()
game_of_thrones = medias.TV_Show("Game of Thrones",
                                "40 min",
                                "Emilia Clarke, Lena Headey",
                                "Several noble families fight for control of the mythical land of Westeros.",
                                "4",
                                "10",
                                "https://pbs.twimg.com/profile_images/458746137621454848/hMTavgm1_400x400.jpeg",
                                "https://www.youtube.com/watch?v=8ixEWrTLiZg")
#an instance of teh class TV_Show()
the_tudors = medias.TV_Show("The Tudors",
                            "40 min",
                            "Jonathan Rhys Meyers, Henry Cavill",
                                "A dramatic series about the reign and marriages of King Henry VIII",
                            "4",
                            "10",
                            "http://upload.wikimedia.org/wikipedia/en/b/bf/TudorsPromo4-2.jpg",
                            "https://www.youtube.com/watch?v=qTiL8pgNqhs")

                      
                      


#this line puts the movies and series in an array
movies_and_series = [salt, game_of_thrones, up, kingdom_of_heaven, bron, the_tudors]
#this line displays the movies and series on the website.
fresh_tomatoes.open_movies_page(movies_and_series)
