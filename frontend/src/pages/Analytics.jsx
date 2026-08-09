import { useEffect, useState } from "react";
import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid
} from "recharts";

import api from "../api/api";

import "../styles/analytics.css";

function Analytics(){

    const [data,setData]=useState(null);

    useEffect(()=>{

        loadAnalytics();

    },[]);

    async function loadAnalytics(){

        const res=await api.get("/analytics/summary");

        setData(res.data);

    }

    if(!data){

        return <h2>Loading...</h2>;

    }

    const pieData=[

        {
            name:"Approved",
            value:data.approved
        },

        {
            name:"Pending",
            value:data.pending
        },

        {
            name:"Rejected",
            value:data.rejected
        }

    ];

    const barData=[

        {
            name:"Invoices",
            value:data.total_invoices
        },

        {
            name:"Amount",
            value:data.total_amount
        }

    ];

    return(

        <div className="analytics-page">

            <h1>Analytics Dashboard</h1>

            <div className="chart-grid">

                <div className="chart-card">

                    <h3>Invoice Status</h3>

                    <ResponsiveContainer
                        width="100%"
                        height={300}
                    >

                        <PieChart>

                            <Pie

                                data={pieData}

                                dataKey="value"

                                outerRadius={100}

                            >

                                <Cell fill="#4CAF50"/>

                                <Cell fill="#FFC107"/>

                                <Cell fill="#F44336"/>

                            </Pie>

                            <Tooltip/>

                        </PieChart>

                    </ResponsiveContainer>

                </div>

                <div className="chart-card">

                    <h3>Overview</h3>

                    <ResponsiveContainer
                        width="100%"
                        height={300}
                    >

                        <BarChart
                            data={barData}
                        >

                            <CartesianGrid/>

                            <XAxis dataKey="name"/>

                            <YAxis/>

                            <Tooltip/>

                            <Bar
                                dataKey="value"
                            />

                        </BarChart>

                    </ResponsiveContainer>

                </div>

            </div>

        </div>

    );

}

export default Analytics;