import fresh_tomatoes, media

# create instances of various movies
deadpool = media.Movie("Deadpool",
                        "A former Special Forces operative who now works as a mercenary.",
                        "http://www.impawards.com/2016/posters/deadpool_ver4.jpg",
                        "https://www.youtube.com/watch?v=ONHBaC-pfsk")

zootopia = media.Movie("Zootopia",
                        "In a city of anthropomorphic animals,"
                        " a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy",
                        "https://lumiere-a.akamaihd.net/v1/images/movie_poster_zootopia_866a1bf2.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=CzvH6_e2a-U")                        

suicide_squad = media.Movie("Suicide Squad",
                            "A secret government agency recruits some of the most dangerous"
                            " incarcerated super-villains to form a defensive task force",
                            "http://orig15.deviantart.net/c5d7/f/2016/012/f/7/suicide_squad_movie_poster_by_bryanzap-d9nqilm.jpg",
                            "https://www.youtube.com/watch?v=WI3hecGO_04")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://www.impawards.com/1995/posters/toy_story_ver2.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://www.impawards.com/2009/posters/avatar.jpg",
                    "https://www.youtube.com/watch?v=a0CDJZu4M5I")

school_of_rock = media.Movie("School of Rock",
                            "Using rock music to learn",
                            "https://fanart.tv/api/download.php?type=download&image=79534&section=3",
                            "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie("Ratatouille",
                            "A rat is a chef in Paris",
                            "http://www.canmag.com/images/front/movies2007/ratatouilleposter5.jpg",
                            "https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg",
                                "https://www.youtube.com/watch?v=dtiklALGz20")

hunger_games = media.Movie("Hunger Games",
                            "A really real reality show",
                            "https://2982-presscdn-29-70-pagely.netdna-ssl.com/wp-content/uploads/2015/11/The-Hunger-Games-Poster1.jpg",
                            "https://www.youtube.com/watch?v=GWU-xLViib0")

# create a list of the movies
movies = [
    deadpool,
    zootopia,
    suicide_squad,
    toy_story,
    avatar,
    school_of_rock,
    ratatouille,
    midnight_in_paris,
    hunger_games
    ]

# pass list of movies to be displayed in html page
fresh_tomatoes.open_movies_page(movies)