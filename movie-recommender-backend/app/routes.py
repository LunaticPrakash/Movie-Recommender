from flask import request, jsonify
from app.recommender import recommend_by_title, search_movies, recommend_by_genre

def register_routes(app):

    @app.route('/recommend-by-title', methods=['GET'])
    def recommend_title():
        title = request.args.get('title')
        mode = request.args.get('mode')
        if not title:
            return jsonify({'error': 'Title is required'}), 400
        result = recommend_by_title(title, mode)
        return jsonify({
            'input': title,
            'recommendations': result 
        })
    
    @app.route('/recommend-by-genre', methods=['GET'])
    def recommend_genre():
        genre = request.args.get('genre')
        mode = request.args.get('mode')
        if not genre:
            return jsonify({'error': 'Genre is required'}), 400
        result = recommend_by_genre(genre, mode)
        
        return jsonify({'input': genre, 'recommendations': result})

    @app.route('/search', methods=['GET'])
    def search():
        query = request.args.get('query')
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        result = search_movies(query)
        return jsonify({'results': result})
