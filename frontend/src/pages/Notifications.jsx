import {
useNotifications
}
from "../context/NotificationContext";


function Notifications(){


const {
notifications
}
=
useNotifications();



return (

<div className="notification-page">


<h1>
Notifications
</h1>


{

notifications.length===0

?

<p>
No notifications
</p>


:

notifications.map(
(item,index)=>(

<div
className="notification-card"
key={index}
>

<h3>
{item.title}
</h3>


<p>
{item.message}
</p>


</div>


))


}


</div>


)


}


export default Notifications;