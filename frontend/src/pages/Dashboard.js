import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await API.get("users/me/");
        setUser(response.data);
      } catch (error) {
        console.log("Not authenticated");
      }
    };

    fetchProfile();
  }, []);

  if (!user) {
    return <h3>Loading...</h3>;
  }

  return (
    <div>
      <h2>Dashboard</h2>

      <h3>Welcome, {user.username}</h3>

      <p>Credits: {user.profile.credits}</p>
      <p>Level: {user.profile.level}</p>
      <p>Badge: {user.profile.badge}</p>
    </div>
  );
}

export default Dashboard;
