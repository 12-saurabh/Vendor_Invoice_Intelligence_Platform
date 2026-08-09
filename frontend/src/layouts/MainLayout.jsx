import { Outlet } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function MainLayout() {
  return (
    <div className="layout">

      <Sidebar />

      <div className="content">

        <Navbar />

        <div className="page-content">
          <Outlet />
        </div>

      </div>

    </div>
  );
}

export default MainLayout;