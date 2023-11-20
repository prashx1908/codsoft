# Sample movie data - Replace this with your dataset
movies = {
    'Movie1': ['Action', 'Adventure', 'Sci-Fi'],
    'Movie2': ['Drama', 'Romance'],
    'Movie3': ['Action', 'Adventure', 'Fantasy'],
    'Movie4': ['Sci-Fi', 'Thriller'],
    'Movie5': ['Comedy', 'Family']
}

# Function to recommend movies based on genres
def recommend_movies(movie, data, num_recommendations=3):
    movie_genres = data.get(movie)
    if not movie_genres:
        return "Movie not found in the database"

    recommendations = []
    for key, value in data.items():
        if key != movie and any(genre in value for genre in movie_genres):
            recommendations.append(key)

    return recommendations[:num_recommendations]


movie_choice = input("Enter movie to be recommended")  # Choose a movie for which you want recommendations
recommended_movies = recommend_movies(movie_choice, movies)
print(f"Recommended movies for {movie_choice}: {recommended_movies}")
