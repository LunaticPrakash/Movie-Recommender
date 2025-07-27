import pickle

movies = pickle.load(open('models/movies.pkl', 'rb'))
similarity_tfidf = pickle.load(open('models/similarity_tfidf.pkl', 'rb'))
similarity_count = pickle.load(open('models/similarity_count.pkl', 'rb'))


def search_movies(movie_title):
    movie_title = movie_title.lower()
    results = movies[movies['original_title'].str.lower().str.contains(movie_title)]
    return results['original_title'].tolist()

def recommend_by_genre(genre_name, mode='tfidf'):
    genre_name = genre_name.lower()
    filtered = movies[movies['tags'].str.contains(genre_name)]
    indices = filtered.index.tolist()

    if mode == 'tfidf':
        similarity_matrix = similarity_tfidf
    elif mode == 'count':
        similarity_matrix = similarity_count
    else:
        return []

    scores = {}
    for idx in indices:
        similar = list(enumerate(similarity_matrix[idx]))
        for i, score in similar:
            scores[i] = scores.get(i, 0) + score

    similar_movies_indices_with_score = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    max_score = similar_movies_indices_with_score[0][1] if similar_movies_indices_with_score else 1

    result = []
    for i, score in similar_movies_indices_with_score:
        row = movies.iloc[i]
        result.append({
            'title': row['original_title'],
            'cast': row.get('cast', ''),
            'genres': row.get('genres', ''),
            'release_year': row.get('release_date', ''),
            'similarity': round((score / max_score) * 100, 2)
        })

    return result

def recommend_by_title(title, mode='tfidf'):
    title = title.lower()
    titles_lower = movies['original_title'].str.lower()

    if title not in titles_lower.values:
        return []

    index = titles_lower[titles_lower == title].index[0]

    if mode == 'tfidf':
        similarity_matrix = similarity_tfidf
    elif mode == 'count':
        similarity_matrix = similarity_count
    else:
        return []

    similarity_scores = list(enumerate(similarity_matrix[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]

    max_score = similarity_scores[0][1] if similarity_scores else 1

    result = []
    for i, score in similarity_scores:
        row = movies.iloc[i]
        result.append({
            'title': row['original_title'],
            'cast': row.get('cast', ''),
            'genres': row.get('genres', ''),
            'release_year': row.get('release_date', ''),
            'similarity': round((score / max_score) * 100, 2)
        })

    return result[1:]
