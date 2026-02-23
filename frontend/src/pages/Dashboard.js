import { useEffect, useState } from "react";
import API from "../services/api";
import "../App.css";

function Dashboard() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    API.get("users/me/")
      .then((res) => setUser(res.data))
      .catch(() => {
        localStorage.removeItem("token");
        window.location.href = "/login";
      });
  }, []);

  if (!user) return <h2 style={{ color: "white" }}>Loading...</h2>;

  return (
    <div className="card">
      <h1>Welcome, {user.username} 👋</h1>

      <div className="info">
        <p><strong>Credits:</strong> {user.profile.credits}</p>
        <p><strong>Level:</strong> {user.profile.level}</p>
        <p><strong>Badge:</strong> {user.profile.badge}</p>
      </div>

      <button
        className="logout"
        onClick={() => {
          localStorage.removeItem("token");
          window.location.href = "/login";
        }}
      >
        Logout
      </button>
      <button
      onClick={() => (window.location.href = "/materials")}
>
     View Study Materials
    </button>

    </div>
  );
}

export default Dashboard;
