import { useEffect, useState } from "react";


function useNotifications(){


    const [notifications,setNotifications] = useState([]);


    const [connected,setConnected] = useState(false);



    useEffect(()=>{


        const token =
        localStorage.getItem(
            "token"
        );



        if(!token){

            console.log(
                "No token found"
            );

            return;

        }




        const socket = new WebSocket(

            `ws://localhost:8000/ws/notifications?token=${token}`

        );





        socket.onopen = ()=>{


            console.log(
                "WebSocket Connected"
            );


            setConnected(true);


        };






        socket.onmessage = (event)=>{


            try{


                const data =
                JSON.parse(
                    event.data
                );



                setNotifications(

                    (prev)=>[

                        data,

                        ...prev

                    ]

                );


            }


            catch(error){


                console.log(

                    "Invalid notification data",

                    error

                );


            }


        };







        socket.onerror = (error)=>{


            console.log(

                "WebSocket Error",

                error

            );


            setConnected(false);


        };







        socket.onclose = ()=>{


            console.log(

                "WebSocket Disconnected"

            );


            setConnected(false);


        };






        return ()=>{


            socket.close();


        };



    },[]);





    return {

        notifications,

        connected

    };


}



export default useNotifications;