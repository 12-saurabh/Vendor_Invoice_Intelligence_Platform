let socket;


export function connectWebSocket(onMessage){


    socket = new WebSocket(
        "ws://localhost:8000/ws"
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



    socket.onerror=(error)=>{

        console.log(
            "WebSocket Error",
            error
        );

    };



    socket.onclose=()=>{

        console.log(
            "WebSocket Closed"
        );

    };


}



export function disconnectWebSocket(){


    if(socket){

        socket.close();

    }


}