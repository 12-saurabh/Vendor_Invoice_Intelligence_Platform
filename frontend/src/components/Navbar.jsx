import useNotifications from "../hooks/useNotifications";

import "../styles/navbar.css";


function Navbar({
    setCollapsed,
    collapsed
}){


    const {
        notifications,
        connected

    } = useNotifications();




    return (


        <div className="navbar">



            <button

                className="menu-btn"

                onClick={() =>
                    setCollapsed(!collapsed)
                }

            >

                ☰

            </button>





            <div className="navbar-right">



                <div className="connection-status">


                    {
                    connected
                    ?

                    <span className="online">

                        ● Online

                    </span>

                    :

                    <span className="offline">

                        ● Offline

                    </span>

                    }


                </div>






                <div className="notification-icon">


                    🔔



                    {

                    notifications.length > 0 &&


                    <span className="notification-count">


                        {

                        notifications.length

                        }


                    </span>


                    }



                </div>



            </div>



        </div>


    );


}


export default Navbar;