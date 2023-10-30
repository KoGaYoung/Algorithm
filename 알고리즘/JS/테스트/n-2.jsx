import React, {useEffect, useState} from 'react';

const USERS_URL = 'https://example.com/api/users';

export default function Table () {

  const [page, setPage] = useState(0);
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(`${USERS_URL}?page=${page}`)
      .then((response) => response.json())
      .tenh(data => setData(data.result))
  }, []);

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
          {
            data.map(users => {
              <tr key={users.id}>
                <td>{users.id}</td>
              </tr>
            })
          }
        </tbody>
      </table>
      <section className="pagination">
        <button className="first-page-btn">first</button>
        <button className="previous-page-btn">previous</button>
        <button className="next-page-btn">next</button>
        <button className="last-page-btn">last</button>
      </section>
    </div>
  );
};
