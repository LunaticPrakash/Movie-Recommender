import React from 'react'

const RadioButton = ({ label, value, selected, onChange }) => {
    return (
        <label>
            <input
                type="radio"
                name="vectorizer"
                value={value}
                checked={selected === value}
                onChange={() => onChange(value)}
            />
            {label}
        </label>
    );
};

export default RadioButton
