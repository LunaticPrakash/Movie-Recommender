import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os
import logging

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

movies = pd.read_csv('dataset/tmdb_5000_movies.csv')
credits = pd.read_csv('dataset/tmdb_5000_credits.csv')
movies = movies.merge(credits, left_on='id', right_on='movie_id')

def convert(obj):
    try:
        return [i['name'] for i in ast.literal_eval(obj)]
    except:
        return []

def get_director(obj):
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return i['name']
        return ''
    except:
        return ''

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(lambda x: convert(x)[:3])
movies['crew'] = movies['crew'].apply(get_director)
movies['overview'] = movies['overview'].fillna('')
movies['tags'] = (
    movies['overview'] + ' ' +
    movies['genres'].apply(lambda x: ' '.join(x)) + ' ' +
    movies['keywords'].apply(lambda x: ' '.join(x)) + ' ' +
    movies['cast'].apply(lambda x: ' '.join(x)) + ' ' +
    movies['crew'].apply(str)
)

movies['tags'] = movies['tags'].fillna('').str.lower()
final_movies = movies[['id', 'original_title', 'tags', 'release_date', 'cast', 'genres']].copy()
final_movies.rename(columns={'original_title': 'title'}, inplace=True)
final_movies.dropna(inplace=True)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_vectors = tfidf.fit_transform(final_movies['tags'])

count = CountVectorizer(stop_words='english')
count_vectors = count.fit_transform(final_movies['tags'])

similarity_tfidf = cosine_similarity(tfidf_vectors)
similarity_count = cosine_similarity(count_vectors)

os.makedirs('models', exist_ok=True)
joblib.dump(final_movies, 'models/movies.joblib')
joblib.dump(similarity_tfidf, 'models/similarity_tfidf.joblib')
joblib.dump(similarity_count, 'models/similarity_count.joblib')
logger.info("Saved both TF-IDF and CountVectorizer models!")

