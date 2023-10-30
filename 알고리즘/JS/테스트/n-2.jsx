import React, { useState, useEffect } from 'react';

const API_ENDPOINT = 'https://example.com/api/users';

const DataTable = () => {
    const [data, setData] = useState([]);
    const [page, setPage] = useState(0);
    const [count, setCount] = useState(0);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const response = await fetch(`${API_ENDPOINT}?page=${page}`);
                const result = await response.json();
                setData(result.results);
                setCount(result.count);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
            setLoading(false);
        };
        fetchData();
    }, [page]);

    return (
        <div>
            <table className="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(item => (
                        <tr key={item.id}>
                            <td>{item.id}</td>
                            <td>{item.firstName}</td>
                            <td>{item.lastName}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <div className="pagination">
                <button
                    className="first-page-btn"
                    disabled={page === 0 || loading}
                    onClick={() => setPage(0)}
                >
                    first
                </button>
                <button
                    className="previous-page-btn"
                    disabled={page === 0 || loading}
                    onClick={() => setPage(prevPage => prevPage - 1)}
                >
                    previous
                </button>
                <button
                    className="next-page-btn"
                    disabled={page >= Math.ceil(count / 10) - 1 || loading}
                    onClick={() => setPage(prevPage => prevPage + 1)}
                >
                    next
                </button>
                <button
                    className="last-page-btn"
                    disabled={page >= Math.ceil(count / 10) - 1 || loading}
                    onClick={() => setPage(Math.ceil(count / 10) - 1)}
                >
                    last
                </button>
            </div>
        </div>
    );
};

export default DataTable;
