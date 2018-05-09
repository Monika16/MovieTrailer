import media
import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "Story of a boy and his toys coming to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine in an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


forrest_gump = media.Movie("Forrest Gump",
                           "Story of a man with childlike optimism",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

school_of_rock = media.Movie("School of Rock",
                           "Using rock music to learn",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")
movies = [toy_story, avatar, forrest_gump, school_of_rock, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)


