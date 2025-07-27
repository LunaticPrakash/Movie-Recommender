import React, { useState, useMemo } from 'react';
import './ResultTable.css';

const ITEMS_PER_PAGE = 5;

const ResultTable = ({ data, type }) => {
  const [currentPage, setCurrentPage] = useState(1);

  const totalPages = useMemo(() => {
    return data ? Math.ceil(data.length / ITEMS_PER_PAGE) : 0;
  }, [data]);

  const paginatedData = useMemo(() => {
    if (!data) return [];
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    return data.slice(startIndex, startIndex + ITEMS_PER_PAGE);
  }, [data, currentPage]);

  if (!data || data.length === 0) {
    return <p className="result__no-data">No data found.</p>;
  }

  return (
    <div className="result__container">
      <div className="table__scroll-wrapper">
        <table className="result__table">
          <colgroup>
            <col style={{ width: '25%' }} />
            <col style={{ width: '20%' }} />
            <col style={{ width: '25%' }} />
            <col style={{ width: '15%' }} />
            <col style={{ width: '15%' }} />
          </colgroup>
          <thead>
            <tr>
              <th>Title</th>
              <th>Genres</th>
              <th>Cast</th>
              <th>Year</th>
              <th>Similarity</th>
            </tr>
          </thead>
          <tbody>
            {paginatedData.map((movie, index) => (
              <tr key={index}>
                <td>{movie.title}</td>
                <td>{movie.genres?.join(', ')}</td>
                <td>{movie.cast?.slice(0, 3).join(', ')}</td>
                <td>{movie.release_year}</td>
                <td>{movie.similarity}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="pagination__controls">
        <button
          onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
          disabled={currentPage === 1}
          className="button pagination__button"
        >
          Previous
        </button>

        <span className="pagination__page">
          Page {currentPage} of {totalPages}
        </span>

        <button
          onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
          disabled={currentPage === totalPages}
          className="pagination__button button"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default ResultTable;
