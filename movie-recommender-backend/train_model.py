import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
import os

# Load data
movies = pd.read_csv('dataset/tmdb_5000_movies.csv')
credits = pd.read_csv('dataset/tmdb_5000_credits.csv')

# Merge on 'id'
movies = movies.merge(credits, left_on='id', right_on='movie_id')

# Data Pre-processing
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

# Create tags
movies['tags'] = movies['overview'] + ' ' + \
                 movies['genres'].apply(lambda x: ' '.join(x)) + ' ' + \
                 movies['keywords'].apply(lambda x: ' '.join(x)) + ' ' + \
                 movies['cast'].apply(lambda x: ' '.join(x)) + ' ' + \
                 movies['crew'].apply(str)

new_df = movies[['id', 'original_title', 'tags', 'release_date', 'cast', 'genres']].copy()
new_df.dropna(inplace=True)
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# Vectorize using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_vectors = tfidf.fit_transform(new_df['tags'])
similarity_tfidf = cosine_similarity(tfidf_vectors)

# Vectorize using CountVectorizer
count = CountVectorizer(stop_words='english')
count_vectors = count.fit_transform(new_df['tags'])
similarity_count = cosine_similarity(count_vectors)

# Save models
os.makedirs('models', exist_ok=True)
pickle.dump(new_df, open('models/movies.pkl', 'wb'))
pickle.dump(similarity_tfidf, open('models/similarity_tfidf.pkl', 'wb'))
pickle.dump(similarity_count, open('models/similarity_count.pkl', 'wb'))

print("Saved both TF-IDF and CountVectorizer models!")