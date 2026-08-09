import { useEffect, useMemo, useState } from "react";
import api from "../api/api";
import "../styles/admin.css";

function Admin() {

    const [users, setUsers] = useState([]);

    const [stats, setStats] = useState({
        users: 0,
        invoices: 0,
        vendors: 0
    });

    const [loading, setLoading] = useState(true);

    const [search, setSearch] = useState("");

    useEffect(() => {
        loadAdminData();
    }, []);

    async function loadAdminData() {

        try {

            const [usersRes, statsRes] = await Promise.all([
                api.get("/admin/users"),
                api.get("/admin/statistics")
            ]);

            setUsers(usersRes.data);

            setStats(statsRes.data);

        }

        catch (err) {

            console.log(err);

        }

        finally {

            setLoading(false);

        }

    }

    const filteredUsers = useMemo(() => {

        return users.filter(user =>

            user.username.toLowerCase().includes(search.toLowerCase()) ||

            user.email.toLowerCase().includes(search.toLowerCase()) ||

            user.role.toLowerCase().includes(search.toLowerCase())

        );

    }, [users, search]);

    if (loading) {

        return (

            <div className="loading">

                Loading Admin Panel...

            </div>

        );

    }

    return (

        <div className="admin-page">

            <div className="page-header">

                <div>

                    <h1>Admin Dashboard</h1>

                    <p>Manage users and monitor the platform.</p>

                </div>

                <button
                    className="refresh-btn"
                    onClick={loadAdminData}
                >
                    Refresh
                </button>

            </div>

            <div className="admin-cards">

                <div className="admin-card">

                    <h4>Total Users</h4>

                    <h2>{stats.users}</h2>

                </div>

                <div className="admin-card">

                    <h4>Total Invoices</h4>

                    <h2>{stats.invoices}</h2>

                </div>

                <div className="admin-card">

                    <h4>Total Vendors</h4>

                    <h2>{stats.vendors}</h2>

                </div>

            </div>

            <div className="table-wrapper">

                <div className="table-header">

                    <h2>Registered Users</h2>

                    <input
                        type="text"
                        placeholder="Search users..."
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />

                </div>

                <table>

                    <thead>

                        <tr>

                            <th>ID</th>

                            <th>Username</th>

                            <th>Email</th>

                            <th>Role</th>

                        </tr>

                    </thead>

                    <tbody>

                        {

                            filteredUsers.length === 0 ?

                                (

                                    <tr>

                                        <td colSpan="4">

                                            No users found

                                        </td>

                                    </tr>

                                )

                                :

                                filteredUsers.map(user => (

                                    <tr key={user.id}>

                                        <td>{user.id}</td>

                                        <td>{user.username}</td>

                                        <td>{user.email}</td>

                                        <td>

                                            <span
                                                className={`role ${user.role}`}
                                            >

                                                {user.role}

                                            </span>

                                        </td>

                                    </tr>

                                ))

                        }

                    </tbody>

                </table>

            </div>

        </div>

    );

}

export default Admin;