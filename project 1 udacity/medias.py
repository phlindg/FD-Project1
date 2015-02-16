
#a template for the classes Movies and TV_Show
class Video():
    #this function initializes the class Video
    def __init__(self, title, duration, actors, storyline, poster_image, trailer_youtube):
        self.title = title
        self.duration = duration
        self.actors = actors
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#a template for putting movies on the website
class Movies(Video):
    def __init__(self, title, duration, actors, storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration, actors, storyline, poster_image, trailer_youtube)
#a template for putting tv-shows on the website
class TV_Show(Video):
    def __init__(self, title, duration, actors, storyline,num_of_seasons, episodes_per_season, poster_image, trailer_youtube):
        Video.__init__(self, title, duration, actors, storyline, poster_image, trailer_youtube)
        self.episodes_per_season = episodes_per_season
        self.num_of_seasons = num_of_seasons
