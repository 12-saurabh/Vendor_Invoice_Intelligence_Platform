import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer
} from "recharts";


function InvoiceTrend(){

const data = [

{
month:"Jan",
invoice:20
},

{
month:"Feb",
invoice:35
},

{
month:"Mar",
invoice:28
},

{
month:"Apr",
invoice:45
},

{
month:"May",
invoice:60
},

{
month:"Jun",
invoice:55
}

];


return (

<div className="chart-card">

<h3>
Invoice Processing Trend
</h3>


<ResponsiveContainer
width="100%"
height={300}
>

<LineChart data={data}>


<CartesianGrid
strokeDasharray="3 3"
/>


<XAxis
dataKey="month"
/>


<YAxis/>


<Tooltip/>


<Line

type="monotone"

dataKey="invoice"

stroke="#2563eb"

strokeWidth={3}

/>


</LineChart>


</ResponsiveContainer>


</div>


);


}


export default InvoiceTrend;