import React, { useState } from 'react';
import './App.css';
import Header from './components/Header/Header.jsx';
import SearchBox from './components/SearchBox/SearchBox.jsx';
import RadioButton from './components/RadioButton/RadioButton.jsx';
import SearchButton from "./components/SearchButton/SearchButton.jsx";
import { searchByTitle, searchByGenre } from "./services/SearchService.js";
import Loader from './components/Loader/Loader.jsx';
import ResultTable from './components/ResultTable/ResultTable.jsx';

function App() {
  const [selected, setSelected] = useState('tfidf');
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState([]);
  const [resultType, setResultType] = useState(null);

  const handleSearch = async (type, selected) => {
    setLoading(true);
    setResults([]);
    setResultType(null);

    try {
      const response = type === 'title'
        ? await searchByTitle(inputValue, selected)
        : await searchByGenre(inputValue, selected);
      console.log("response : ", typeof(response));
      setResults(response.recommendations);
      setResultType(type);
    } catch (err) {
      console.error('Search failed:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {loading && <Loader />}

      <div className='container'>
        <div className='container__header'>
          <Header />
        </div>

        <div className='container__searchbox'>
          <SearchBox
            placeholder={"Enter Movie Title or Genre..."}
            inputValue={inputValue}
            setInputValue={setInputValue}
          />
        </div>

        <div className="container__vectorizer">
          <RadioButton label="TF-IDF" value="tfidf" selected={selected} onChange={setSelected} />
          <RadioButton label="Count Vectorizer" value="count" selected={selected} onChange={setSelected} />
        </div>

        <div className='container__buttongroup'>
          <SearchButton text={"Search By Title"} onClick={() => handleSearch("title", selected)} />
          <SearchButton text={"Search By Genre"} onClick={() => handleSearch("genre", selected)} />
        </div>

        <ResultTable data={results} type={resultType} />


      </div>
    </>
  );
}

export default App;