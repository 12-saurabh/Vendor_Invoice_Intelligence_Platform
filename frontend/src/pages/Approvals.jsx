
import { useEffect, useState } from "react";
import api from "../api/api";

import "../styles/approvals.css";


function Approvals(){

    const [approvals,setApprovals] = useState([]);

    const [loading,setLoading] = useState(true);



    useEffect(()=>{

        loadApprovals();

    },[]);



    async function loadApprovals(){

        try{

            const res = await api.get(
                "/approvals"
            );

            setApprovals(res.data);

        }
        catch(err){

            console.log(err);

        }
        finally{

            setLoading(false);

        }

    }



    async function updateStatus(id,status){


        try{


            await api.put(

                `/approvals/${id}`,

                {

                    status:status

                }

            );


            loadApprovals();


        }
        catch(err){

            console.log(err);

        }


    }





    if(loading){

        return <h2>Loading approvals...</h2>

    }



    return (

    <div className="approval-container">


        <div className="approval-header">

            <h1>
                Invoice Approvals
            </h1>


            <p>
                Review and approve vendor invoices
            </p>


        </div>




        <div className="approval-card">


        <table>


        <thead>

        <tr>

        <th>
            Invoice ID
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
            Action
        </th>


        </tr>

        </thead>



        <tbody>


        {

        approvals.map(

        (invoice)=>(


        <tr key={invoice.id}>


        <td>
            #{invoice.id}
        </td>


        <td>
            {
            invoice.vendor_name ||
            "Unknown"
            }
        </td>


        <td>
            ₹ {invoice.amount}
        </td>



        <td>


        <span

        className={
        `status ${invoice.status}`
        }

        >

        {
        invoice.status
        }


        </span>


        </td>



        <td>


        <button

        className="approve"

        onClick={()=>updateStatus(
            invoice.id,
            "approved"
        )}

        >

        Approve

        </button>



        <button

        className="reject"

        onClick={()=>updateStatus(
            invoice.id,
            "rejected"
        )}

        >

        Reject

        </button>


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


export default Approvals;