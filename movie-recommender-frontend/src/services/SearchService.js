import axios from 'axios'

const BASE_URL = 'http://localhost:5000';

export const searchByTitle = async (title, mode = 'tfidf') => {
    try {
        const response = await axios.get(`${BASE_URL}/recommend-by-title`, {
            params: { title, mode },
        });
        console.log("Raw axios response:", response);                 // Full response object
        console.log("response.data:", response.data);                 // Parsed data
        console.log("typeof response.data:", typeof response.data);   // Should be 'object'
        console.log("response.data.recommendations:", response.data.recommendations);
        console.log("typeof response.data.recommendations:", typeof response.data.recommendations);

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