import {
    LayoutDashboard,
    FileText,
    Building2,
    CheckCircle,
    Bot,
    BarChart3,
    FileBarChart,
    Settings,
    Bell,
    Activity
} from "lucide-react";

import "../styles/sidebar.css";

import { NavLink } from "react-router-dom";


function Sidebar({collapsed}) {


const menu = [

{
    name:"Dashboard",
    path:"/dashboard",
    icon:<LayoutDashboard />
},

{
    name:"Invoices",
    path:"/invoices",
    icon:<FileText />
},

{
    name:"Vendors",
    path:"/vendors",
    icon:<Building2 />
},

{
    name:"Approvals",
    path:"/approvals",
    icon:<CheckCircle />
},

{
    name:"Predictions",
    path:"/predictions",
    icon:<Bot />
},

{
    name:"Analytics",
    path:"/analytics",
    icon:<BarChart3 />
},

{
    name:"Reports",
    path:"/reports",
    icon:<FileBarChart />
},

{
    name:"Admin",
    path:"/admin",
    icon:<Settings />
},

{
    name:"Notifications",
    path:"/notifications",
    icon:<Bell />
},

{
    name:"Monitoring",
    path:"/monitoring",
    icon:<Activity />
}

];


return (

<div className="sidebar">


<div className="logo">

{
collapsed
?
"VA"
:
"Vendor AI"
}

</div>



<div className="menu">


{
menu.map((item)=>(


<NavLink

key={item.path}

to={item.path}

className={({isActive}) =>
isActive
?
"nav-item active"
:
"nav-item"
}

>


{item.icon}


{
!collapsed &&
<span>
{item.name}
</span>
}


</NavLink>


))

}


</div>


</div>

);


}


export default Sidebar;