import React from 'react';
import './SearchButton.css';

const SearchButton = ({ text, onClick, loading }) => {
    return (
        <button className="button" onClick={onClick} disabled={loading}>
            {loading ? (
                <span className="spinner"></span>
            ) : (
                text
            )}
        </button>
    );
};

export default SearchButton;
