import { useEffect, useState } from "react";
import API from "../services/api";
import "../App.css";

function Materials() {
  const [materials, setMaterials] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    API.get("materials/")
      .then((res) => setMaterials(res.data))
      .catch((err) => console.error(err));
  }, []);

  const filteredMaterials = materials.filter((item) =>
    item.title.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="materials-container">
      <h1>Study Materials 📚</h1>

      <input
        type="text"
        placeholder="Search materials..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="search-input"
      />

      {filteredMaterials.length === 0 ? (
        <p className="empty-text">No materials found</p>
      ) : (
        <div className="materials-grid">
          {filteredMaterials.map((item) => (
            <div key={item.id} className="material-card">
              <h3>{item.title}</h3>
              <p>{item.description}</p>

              <a
                href={item.file}
                target="_blank"
                rel="noreferrer"
                className="download-btn"
              >
                Download
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Materials;
