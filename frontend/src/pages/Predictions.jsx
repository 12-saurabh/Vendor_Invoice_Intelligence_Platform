
import { useState } from "react";
import api from "../api/api";

import "../styles/predictions.css";


function Predictions(){

    const [invoiceId,setInvoiceId] = useState("");

    const [result,setResult] = useState(null);

    const [loading,setLoading] = useState(false);



    async function runPrediction(){


        if(!invoiceId){

            alert(
                "Enter Invoice ID"
            );

            return;

        }


        try{


            setLoading(true);



            const res = await api.post(

                "/prediction",

                {

                    invoice_id:
                    invoiceId

                }

            );


            setResult(
                res.data
            );


        }

        catch(err){

            console.log(err);

            alert(
                "Prediction failed"
            );

        }

        finally{

            setLoading(false);

        }

    }




    return (

    <div className="prediction-container">


        <div className="prediction-header">


            <h1>
                AI Prediction Engine
            </h1>


            <p>
                ML powered invoice risk and cost prediction
            </p>


        </div>





        <div className="prediction-box">


            <input

            placeholder="Enter Invoice ID"

            value={invoiceId}

            onChange={
                e=>setInvoiceId(
                    e.target.value
                )
            }

            />



            <button

            onClick={runPrediction}

            >

            {
            loading
            ?
            "Analyzing..."
            :
            "Run AI Prediction"
            }


            </button>


        </div>





        {
        result &&


        <div className="result-grid">



            <div className="result-card">

                <h3>
                    Predicted Freight Cost
                </h3>


                <h2>
                    ₹ {result.freight_cost}
                </h2>


            </div>





            <div className="result-card">


                <h3>
                    Approval Prediction
                </h3>


                <h2>

                {
                result.manual_approval
                ?
                "Manual Review"
                :
                "Auto Approved"
                }

                </h2>


            </div>





            <div className="result-card">


                <h3>
                    Risk Score
                </h3>


                <h2>

                {
                result.risk_score
                }%

                </h2>


            </div>



        </div>


        }


    </div>

    )


}


export default Predictions;