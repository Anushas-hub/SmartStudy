import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

function Content() {
  const { user, logout } = useContext(AuthContext);

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-4">
        Welcome, {user?.username}
      </h1>

      <p className="mb-4">
        Email: {user?.email}
      </p>

      <button
        onClick={logout}
        className="bg-red-500 text-white px-4 py-2 rounded"
      >
        Logout
      </button>
    </div>
  );
}

export default Content;