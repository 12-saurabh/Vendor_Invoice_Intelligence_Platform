let socket = null;


export const connectSocket = (onMessage)=>{


    const token = localStorage.getItem(
        "token"
    );


    if(!token){

        return;

    }



    const protocol =
        window.location.protocol === "https:" ? "wss" : "ws";

    socket = new WebSocket(
        `${protocol}://${window.location.host}/ws/dashboard`
    );




    socket.onopen = ()=>{

        console.log(
            "WebSocket Connected"
        );

    };





    socket.onmessage = (event)=>{


        const data =
        JSON.parse(
            event.data
        );


        onMessage(data);


    };





    socket.onerror = (error)=>{

        console.log(
            "Socket Error",
            error
        );

    };





    socket.onclose = ()=>{

        console.log(
            "WebSocket Disconnected"
        );

    };


};





export const disconnectSocket = ()=>{


    if(socket){

        socket.close();

    }

};