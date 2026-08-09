import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

function DashboardLayout({ children }) {
    return (
        <div className="layout">

            <Sidebar />

            <div className="main">

                <Navbar />

                <div className="content">
                    {children}
                </div>

            </div>

        </div>
    );
}

export default DashboardLayout;