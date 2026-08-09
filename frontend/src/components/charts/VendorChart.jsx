import {

BarChart,
Bar,
XAxis,
YAxis,
Tooltip,
ResponsiveContainer

}
from "recharts";


function VendorChart(){


const data=[

{
vendor:"ABC",
amount:50000
},

{
vendor:"XYZ",
amount:35000
},

{
vendor:"PQR",
amount:70000
},

{
vendor:"DEF",
amount:25000
}

];


return (

<div className="chart-card">


<h3>
Vendor Spending
</h3>


<ResponsiveContainer
width="100%"
height={300}
>


<BarChart data={data}>


<XAxis
dataKey="vendor"
/>


<YAxis/>


<Tooltip/>


<Bar

dataKey="amount"

/>


</BarChart>


</ResponsiveContainer>


</div>

);


}


export default VendorChart;