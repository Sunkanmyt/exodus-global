import { useEffect, useState } from "react";
import axios from "axios";

function Sermons() {
  const [sermons, setSermons] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/sermons/")
      .then((res) => setSermons(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="p-8 bg-slate-50 min-h-screen">
      <h1 className="text-4xl font-black text-slate-900 mb-8 border-b-4 border-exodus inline-block pb-2">
        Exodus Global Sermons
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {sermons.map((sermon) => (
          <div
            key={sermon.id}
            className="p-6 bg-white shadow-sm hover:shadow-xl transition-all rounded-xl border-t-4 border-exodus group"
          >
            <h2 className="text-2xl font-bold text-slate-800 group-hover:text-exodus transition-colors">
              {sermon.title}
            </h2>
            <p className="text-slate-500 mt-2 font-medium">
              By {sermon.speaker}
            </p>

            <button className="mt-6 w-full py-3 bg-exodus hover:bg-exodus-dark text-white font-bold rounded-lg transition-colors">
              See Teaching
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sermons;
