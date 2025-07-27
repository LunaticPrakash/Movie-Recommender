import React, { useState } from 'react';
import './SearchBox.css';

const SearchBox = ({ placeholder, inputValue, setInputValue }) => {

    return (
        <div className='searchbox__container'>
            <input
                type="input"
                placeholder={placeholder}
                onChange={(e) => setInputValue(e.target.value)}
                className="searchbox__input"
                value={inputValue}
            />
        </div>
    );
};

export default SearchBox;