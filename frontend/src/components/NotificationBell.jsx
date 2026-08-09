import {
    useEffect,
    useState
} from "react";


import {
    connectSocket,
    disconnectSocket
}
from "../services/socket";



function NotificationBell(){



    const [
        notifications,
        setNotifications
    ] = useState([]);




    useEffect(()=>{


        connectSocket(
            (message)=>{


                setNotifications(
                    prev=>[
                        message,
                        ...prev
                    ]
                );


            }
        );



        return ()=>{

            disconnectSocket();

        };


    },[]);







    return (

        <div className="notification-box">


            <div className="notification-title">

                🔔 Notifications

                <span>

                    {notifications.length}

                </span>


            </div>





            <div className="notification-list">


            {

            notifications.length===0 ?


            (

                <p>

                    No notifications

                </p>

            )


            :


            notifications.map(
            (item,index)=>(


                <div

                key={index}

                className="notification-item"

                >


                    <strong>

                        {item.title ||
                        "System"}

                    </strong>


                    <p>

                        {item.message ||
                        JSON.stringify(item)}

                    </p>


                </div>


            ))

            }



            </div>



        </div>

    );


}


export default NotificationBell;