import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
import os

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

movies = pd.read_csv('dataset/tmdb_5000_movies.csv', usecols=['id', 'overview', 'genres', 'keywords', 'title'])  # only needed cols
credits = pd.read_csv('dataset/tmdb_5000_credits.csv', usecols=['movie_id', 'cast', 'crew'])

movies = movies.merge(credits, left_on='id', right_on='movie_id')

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(lambda x: convert(x)[:3])  # only top 3 cast members
movies['crew'] = movies['crew'].apply(get_director)
movies['overview'] = movies['overview'].fillna('')

movies['tags'] = movies['overview'] + ' ' + \
                 movies['genres'].apply(lambda x: ' '.join(x)) + ' ' + \
                 movies['keywords'].apply(lambda x: ' '.join(x)) + ' ' + \
                 movies['cast'].apply(lambda x: ' '.join(x)) + ' ' + \
                 movies['crew'].apply(str)

new_df = movies[['id', 'title', 'tags']].copy()
new_df.dropna(inplace=True)
new_df['tags'] = new_df['tags'].str.lower()

# === Vectorization ===
tfidf = TfidfVectorizer(stop_words='english')
tfidf_vectors = tfidf.fit_transform(new_df['tags'])

count = CountVectorizer(stop_words='english')
count_vectors = count.fit_transform(new_df['tags'])

# === Cosine Similarity ===
similarity_tfidf = cosine_similarity(tfidf_vectors, dense_output=False)
similarity_count = cosine_similarity(count_vectors, dense_output=False)

# === Save Models Efficiently ===
os.makedirs('models', exist_ok=True)
joblib.dump(new_df, 'models/movies.joblib', compress=3)
joblib.dump(similarity_tfidf, 'models/similarity_tfidf.joblib', compress=3)
joblib.dump(similarity_count, 'models/similarity_count.joblib', compress=3)

print("Both TF-IDF and Count Vectorization Models Saved.")
