
import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import ProtectedRoute from "./routes/ProtectedRoute";
import Layout from "./layouts/Layout";
import Monitoring from "./pages/Monitoring";
import Invoices from "./pages/Invoices";
import Vendors from "./pages/Vendors";
import Approvals from "./pages/Approvals";
import Predictions from "./pages/Predictions";
import Analytics from "./pages/Analytics";
import Reports from "./pages/Reports";
import Admin from "./pages/Admin";
import Notifications from "./pages/Notifications";
import UploadInvoice from "./pages/UploadInvoice";

function App() {

    return (

        <Routes>

            {/* Public Routes */}

            <Route
                path="/"
                element={<Login />}
            />

            <Route
                path="/login"
                element={<Login />}
            />


            {/* Protected Dashboard */}

            <Route
                path="/dashboard"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Dashboard />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            {/* Protected Pages */}

            <Route
                path="/invoices"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Invoices />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            <Route
                path="/vendors"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Vendors />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            <Route
                path="/approvals"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Approvals />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            <Route
                path="/predictions"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Predictions />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            <Route
                path="/analytics"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Analytics />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            <Route
                path="/reports"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Reports />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            <Route
                path="/admin"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Admin />
                        </Layout>
                    </ProtectedRoute>
                }
            />


            <Route
                path="/notifications"
                element={
                    <ProtectedRoute>
                        <Layout>
                            <Notifications />
                        </Layout>
                    </ProtectedRoute>
                }
            />

            <Route

                path="/upload"

                element={

                    <ProtectedRoute>

                    <Layout>

                    <UploadInvoice />

                    </Layout>

                    </ProtectedRoute>

                }

            />

            <Route

                path="/monitoring"

                element={

                    <ProtectedRoute>

                    <Layout>

                    <Monitoring/>

                    </Layout>

                    </ProtectedRoute>

                }

            />


            {/* Unknown Route */}

            <Route
                path="*"
                element={<Login />}
            />

        </Routes>

    );

}


export default App;