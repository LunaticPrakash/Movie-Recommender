import joblib
import logging

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

logger.info("Loading joblib models from memory")
movies = joblib.load('models/movies.joblib')
similarity_tfidf = joblib.load('models/similarity_tfidf.joblib')
similarity_count = joblib.load('models/similarity_count.joblib')
logger.info("Joblib models loaded successfully.")

def search_movies(movie_title):
    movie_title = movie_title.lower()
    results = movies[movies['title'].str.lower().str.contains(movie_title)]
    return results['title'].tolist()

def recommend_by_title(title, mode='tfidf'):
    title = title.lower()
    matched = movies[movies['title'].str.lower().str.contains(title)]
    if matched.empty:
        return []
    index = matched.index[0]
    similarity_matrix = similarity_tfidf if mode == 'tfidf' else similarity_count
    similarity_scores = list(enumerate(similarity_matrix[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]
    max_score = similarity_scores[0][1] if similarity_scores else 1
    result = []
    for i, score in similarity_scores:
        if score == 0:
            continue
        row = movies.iloc[i]
        result.append({
            'title': row['title'],
            'cast': row.get('cast', ''),
            'genres': row.get('genres', ''),
            'release_year': row.get('release_date', ''),
            'similarity': round((score / max_score) * 100, 2)
        })
    return result

def recommend_by_genre(genre_name, mode='tfidf'):
    genre_name = genre_name.lower()
    filtered = movies[movies['tags'].str.contains(genre_name)]
    indices = filtered.index.tolist()
    similarity_matrix = similarity_tfidf if mode == 'tfidf' else similarity_count
    scores = {}
    for idx in indices:
        similar = list(enumerate(similarity_matrix[idx]))
        for i, score in similar:
            scores[i] = scores.get(i, 0) + score
    similar_movies_indices_with_score = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    max_score = similar_movies_indices_with_score[0][1] if similar_movies_indices_with_score else 1
    result = []
    for i, score in similar_movies_indices_with_score:
        if score == 0:
            continue
        row = movies.iloc[i]
        result.append({
            'title': row['title'],
            'cast': row.get('cast', ''),
            'genres': row.get('genres', ''),
            'release_year': row.get('release_date', ''),
            'similarity': round((score / max_score) * 100, 2)
        })
    return result
