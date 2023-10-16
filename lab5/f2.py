"""
#task1
def imdbscoreisabove55(movie):
    return movie["imdb"] > 5.5

#task2
def getmoviesabove55(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

#task3
def moviesbycategory(movies, category):
    return [movie for movie in movies if movie["category"] == category]

#task4
def calculateaverageimdbscore(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
"""
#task5
def calculateaverageimdbscorebycategory(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]
    
    if not category_movies:
        return 0
    total_score = sum(movie["imdb"] for movie in category_movies)
    return total_score / len(category_movies)

movies = [{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"},
{"name": "Hitman",
"imdb": 6.3,
"category": "Action"},
{"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"},
{"name": "The Help",
"imdb": 8.0,
"category": "Drama"},
{"name": "The Choice",
"imdb": 6.2,
"category": "Romance"},
{"name": "Colonia",
"imdb": 7.4,
"category": "Romance"},
{"name": "Love",
"imdb": 6.0,
"category": "Romance"},
{"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"},
{"name": "AlphaJet",
"imdb": 3.2,
"category": "War"},
{"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"},
{"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"},
{"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"},
{"name": "Detective",
"imdb": 7.0,
"category": "Suspense"},
{"name": "Exam",
"imdb": 4.2,
"category": "Thriller"},
{"name": "We Two",
"imdb": 7.2,
"category": "Romance"}]

#Print the results
"""
#task1
results = [imdbscoreisabove55(movie) for movie in movies]
for result in results:
    print(result)

#task2
selected_movies = getmoviesabove55(movies)
for movie in selected_movies:
    print(movie)

#task3
category=str(input()) #типа Romance или Action
selected_movies = moviesbycategory(movies, category)
for movie in selected_movies:
    print(movie)

#task4
average_score = calculateaverageimdbscore(movies)
print("Average IMDB score:", average_score)
"""
#task5
category =str(input())
average_score = calculateaverageimdbscorebycategory(movies, category)
print(f"Average IMDB score for {category} movies:", average_score)

