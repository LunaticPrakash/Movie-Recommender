import axios from 'axios'

const BASE_URL = 'https://movie-recommender-q93t.onrender.com/';

export const searchByTitle = async (title, mode = 'tfidf') => {
    try {
        const response = await axios.get(`${BASE_URL}/recommend-by-title`, {
            params: { title, mode },
        });

        return response.data;
    } catch (error) {
        console.error('Error fetching recommendations by title:', error);
        throw error;
    }
};

export const searchByGenre = async (genre, mode = 'tfidf') => {
    try {
        const response = await axios.get(`${BASE_URL}/recommend-by-genre`, {
            params: { genre, mode },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching recommendations by genre:', error);
        throw error;
    }
};

export const searchMovies = async (query) => {
    try {
        const response = await axios.get(`${BASE_URL}/search`, {
            params: { query },
        });
        return response.data;
    } catch (error) {
        console.error('Error searching movies:', error);
        throw error;
    }
};