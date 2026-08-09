import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";


function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);



    const handleLogin = async (e) => {

        e.preventDefault();

        setLoading(true);


        try {

            const formData = new URLSearchParams();

            formData.append(
                "username",
                username
            );

            formData.append(
                "password",
                password
            );


            const response = await api.post(
                "/auth/login",
                formData,
                {
                    headers:{
                        "Content-Type":
                        "application/x-www-form-urlencoded",
                    },
                }
            );


            console.log(
                "LOGIN RESPONSE:",
                response.data
            );


            // Save JWT Token

            localStorage.setItem(
                "token",
                response.data.access_token
            );


            // Save user details

            localStorage.setItem(
                "username",
                response.data.username
            );


            localStorage.setItem(
                "role",
                response.data.role
            );


            console.log(
                "TOKEN:",
                localStorage.getItem("token")
            );


            navigate("/dashboard");


        } catch(error) {


            console.log(
                "LOGIN ERROR:",
                error.response?.data
            );


            alert(
                error.response?.data?.detail ||
                "Invalid Username or Password"
            );


        } finally {

            setLoading(false);

        }

    };



    return (

        <div className="login-page">


            <div className="login-card">


                <h1>
                    Vendor Invoice Platform
                </h1>


                <p>
                    Login to Continue
                </p>



                <form onSubmit={handleLogin}>


                    <input

                        type="text"

                        placeholder="Username or Email"

                        value={username}

                        onChange={
                            (e)=>
                            setUsername(e.target.value)
                        }

                    />



                    <input

                        type="password"

                        placeholder="Password"

                        value={password}

                        onChange={
                            (e)=>
                            setPassword(e.target.value)
                        }

                    />



                    <button
                        type="submit"
                        disabled={loading}
                    >

                        {
                            loading
                            ?
                            "Please Wait..."
                            :
                            "Login"
                        }


                    </button>


                </form>


            </div>


        </div>

    );

}


export default Login;