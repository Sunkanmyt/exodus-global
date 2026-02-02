import { useEffect, useState } from "react";
import axios from "axios";

function Gallery() {
  const [milestones, setMilestones] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/gallery/")
      .then((res) => setMilestones(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold border-l-4 border-exodus pl-4 mb-8">
        Our Journey
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {milestones.map((item) => (
          <div
            key={item.id}
            className="group relative overflow-hidden rounded-xl shadow-lg"
          >
            {/* The Image from your Backend */}
            <img
              src={item.image}
              alt={item.title}
              className="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500"
            />

            {/* An 'Exodus Gold' Overlay that appears on hover */}
            <div className="absolute inset-0 bg-exodus/80 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-center p-6 text-white">
              <h3 className="text-xl font-bold">{item.title}</h3>
              <p className="text-sm mt-2">{item.description}</p>
              <span className="text-xs mt-4 font-mono">
                {item.date_achieved}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Gallery;
