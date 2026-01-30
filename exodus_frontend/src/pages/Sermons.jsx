import { useEffect, useState } from 'react';
import axios from 'axios';

function Sermons() {
  const [sermons, setSermons] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/sermons/')
      .then(res => setSermons(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div className="p-8 bg-gray-50 min-h-screen">
      <h1 className="text-4xl font-bold text-blue-900 mb-6">Exodus Global Teachings</h1>
      <div className="grid gap-4">
        {sermons.map(sermon => (
          <div key={sermon.id} className="p-4 bg-white shadow rounded-lg border-l-4 border-blue-600">
            <h2 className="text-xl font-semibold">{sermon.title}</h2>
            <p className="text-gray-600">By {sermon.speaker}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sermons;