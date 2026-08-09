import { useEffect, useState } from "react";
import api from "../api/api";

import {
    FileText,
    IndianRupee,
    Clock,
    AlertTriangle
} from "lucide-react";

import {
    PieChart,
    Pie,
    Cell,
    ResponsiveContainer
} from "recharts";


import "../styles/dashboard.css";


function Dashboard(){


const [summary,setSummary]=useState(null);



useEffect(()=>{

    loadDashboard();

},[]);



async function loadDashboard(){

    try{

        const res=await api.get(
            "/dashboard/summary"
        );

        setSummary(res.data);

    }
    catch(err){

        console.log(err);

    }

}



if(!summary)
{
    return <h2>Loading...</h2>
}



const chartData=[

{
name:"Approved",
value:
summary.invoice_status.approved || 0
},

{
name:"Pending",
value:
summary.invoice_status.pending || 0
},

{
name:"Rejected",
value:
summary.invoice_status.rejected || 0
}

];



return (

<div className="dashboard-container">


<div className="dashboard-header">

<h1>
Vendor Invoice Intelligence
</h1>

<p>
AI powered invoice processing dashboard
</p>

</div>




<div className="cards">


<div className="stat-card">

<FileText size={35}/>

<h3>
Total Invoices
</h3>

<h2>
{summary.total_invoices}
</h2>

</div>




<div className="stat-card">

<IndianRupee size={35}/>

<h3>
Total Amount
</h3>

<h2>
₹ {summary.total_amount}
</h2>

</div>




<div className="stat-card">

<Clock size={35}/>

<h3>
Pending Approval
</h3>

<h2>
{summary.invoice_status.pending}
</h2>

</div>




<div className="stat-card">

<AlertTriangle size={35}/>

<h3>
High Risk
</h3>

<h2>
{summary.risk.high}
</h2>

</div>


</div>





<div className="chart-box">


<h2>
Invoice Status
</h2>


<ResponsiveContainer
width="100%"
height={300}
>

<PieChart>

<Pie
data={chartData}
dataKey="value"
nameKey="name"
outerRadius={100}
>

{
chartData.map(
(entry,index)=>(

<Cell key={index}/>

))
}


</Pie>


</PieChart>


</ResponsiveContainer>


</div>



</div>

)


}


export default Dashboard;