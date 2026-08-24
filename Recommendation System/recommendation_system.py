import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("../Image Caption/movie.csv")

cv = CountVectorizer()
matrix = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(matrix)

movie_name = input("Enter movie name: ").strip().title()
if movie_name not in movies["title"].values:
    print("Movie not found!")
else:
    idx = movies[movies["title"] == movie_name].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")

    for i in scores[1:6]:
        print(movies.iloc[i[0]]["title"])