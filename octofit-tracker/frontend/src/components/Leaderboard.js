import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboards, setLeaderboards] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME || 'localhost';
  const apiUrl = `https://${codespace}-8000.app.github.dev/api/leaderboards/`;

  useEffect(() => {
    console.log('Fetching leaderboards from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboards(results);
        console.log('Fetched leaderboards:', results);
      })
      .catch(err => console.error('Error fetching leaderboards:', err));
  }, [apiUrl]);

  return (
    <div>
      <h2 className="mb-4 text-primary">Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-light">
            <tr>
              <th>Team</th>
              <th>Total Points</th>
              <th>Last Updated</th>
            </tr>
          </thead>
          <tbody>
            {leaderboards.map((lb, idx) => (
              <tr key={lb.id || idx}>
                <td>{lb.team}</td>
                <td>{lb.total_points}</td>
                <td>{lb.last_updated}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;
