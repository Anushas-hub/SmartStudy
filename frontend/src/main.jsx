import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";

function App() {
  const [materials, setMaterials] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/materials/")
      .then((response) => response.json())
      .then((data) => setMaterials(data))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>SmartStudy Notes</h1>

      {materials.length === 0 ? (
        <p>No notes available</p>
      ) : (
        materials.map((item) => (
          <div
            key={item.id}
            style={{
              border: "1px solid #ccc",
              padding: "10px",
              marginBottom: "10px",
            }}
          >
            <h3>{item.title}</h3>
            <p>{item.content}</p>
          </div>
        ))
      )}
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
