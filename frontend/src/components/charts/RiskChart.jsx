import {
PieChart,
Pie,
Cell,
Tooltip,
ResponsiveContainer
}
from "recharts";


function RiskChart(){


const data=[

{
name:"Low Risk",
value:70
},

{
name:"Medium Risk",
value:20
},

{
name:"High Risk",
value:10
}

];


return (

<div className="chart-card">


<h3>
Invoice Risk Analysis
</h3>


<ResponsiveContainer
width="100%"
height={300}
>


<PieChart>


<Pie

data={data}

dataKey="value"

outerRadius={100}

label

>


{
data.map(
(entry,index)=>(

<Cell
key={index}
/>

)

)

}


</Pie>


<Tooltip/>


</PieChart>


</ResponsiveContainer>


</div>

);


}


export default RiskChart;