import { useEffect, useState } from "react";
import api from "../api/api";

import "../styles/invoices.css";
import { useNavigate } from "react-router-dom";

function Invoices(){

    const [invoices,setInvoices] = useState([]);
    const [search,setSearch] = useState("");
    const [loading,setLoading] = useState(true);
    const navigate = useNavigate();


    useEffect(()=>{

        fetchInvoices();

    },[]);



    async function fetchInvoices(){

        try{

            const res = await api.get(
                "/invoices"
            );

            setInvoices(res.data);

        }
        catch(err){

            console.log(err);

        }
        finally{

            setLoading(false);

        }

    }



    const filteredInvoices =
    invoices.filter((invoice)=>

        JSON.stringify(invoice)
        .toLowerCase()
        .includes(
            search.toLowerCase()
        )

    );



    if(loading){

        return (

            <h2>
                Loading invoices...
            </h2>

        )

    }



    return (

        <div className="invoice-container">


            <div className="invoice-header">

                <div>

                <h1>
                    Invoice Management
                </h1>

                <p>
                    Manage uploaded vendor invoices
                </p>

                </div>


                <button
                onClick={()=>navigate("/upload")}
                >
                Upload Invoice
                </button>


            </div>



            <input

                className="search-box"

                placeholder="Search invoice..."

                value={search}

                onChange={
                    e=>setSearch(e.target.value)
                }

            />



            <div className="table-card">


            <table>


            <thead>

            <tr>

            <th>
                ID
            </th>

            <th>
                Vendor
            </th>

            <th>
                Amount
            </th>

            <th>
                Status
            </th>

            <th>
                Risk
            </th>

            </tr>

            </thead>



            <tbody>


            {
            filteredInvoices.map(
                (invoice)=>(


                <tr key={invoice.id}>


                <td>
                    {invoice.id}
                </td>


                <td>
                    {
                    invoice.vendor_name ||
                    "Unknown"
                    }
                </td>


                <td>
                    ₹ {invoice.amount || 0}
                </td>


                <td>

                <span
                className={
                `status ${invoice.status}`
                }
                >

                {
                invoice.status ||
                "Pending"
                }

                </span>

                </td>


                <td>

                <span
                className={
                invoice.risk_score > 70
                ?
                "risk high"
                :
                "risk low"
                }
                >

                {
                invoice.risk_score > 70
                ?
                "High"
                :
                "Low"
                }

                </span>


                </td>


                </tr>


            ))

            }


            </tbody>


            </table>


            </div>



        </div>

    )


}


export default Invoices;