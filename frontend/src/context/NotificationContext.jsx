import {
createContext,
useContext,
useEffect,
useState
}
from "react";


import {
connectWebSocket,
disconnectWebSocket
}
from "../api/websocket";



const NotificationContext =
createContext();



export function NotificationProvider({
children
}){


const [
notifications,
setNotifications
]
=
useState([]);



useEffect(()=>{


connectWebSocket(
(message)=>{


setNotifications(
(prev)=>[
message,
...prev
]
);


}
);



return ()=>{

disconnectWebSocket();

};


},[]);




return (

<NotificationContext.Provider

value={{

notifications,

setNotifications

}}

>

{children}


</NotificationContext.Provider>


);


}



export function useNotifications(){

return useContext(
NotificationContext
);

}