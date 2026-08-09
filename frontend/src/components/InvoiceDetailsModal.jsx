import { useEffect, useState } from "react";
import api from "../api/api";

function InvoiceDetailsModal({ invoice, close }) {


    const [details, setDetails] = useState(null);

    const [loading, setLoading] = useState(true);



    const loadDetails = async ()=>{

        try{


            const response = await api.get(
                `/invoice/${invoice.id}`
            );


            setDetails(
                response.data
            );


        }
        catch(error){

            console.log(error);

        }
        finally{

            setLoading(false);

        }

    };



    useEffect(()=>{

        loadDetails();

    },[]);



    if(loading){

        return (

            <div className="modal">

                <div className="details-modal">

                    <h2>
                        Loading invoice...
                    </h2>

                </div>

            </div>

        );

    }



    return (

        <div className="modal">


            <div className="details-modal">


                <div className="details-header">


                    <h2>
                        Invoice Details
                    </h2>


                    <button
                        onClick={close}
                    >
                        ✕
                    </button>


                </div>



                <div className="details-grid">


                    <div>

                        <label>
                            Invoice Number
                        </label>

                        <p>
                            {details.invoice_number}
                        </p>

                    </div>



                    <div>

                        <label>
                            Vendor
                        </label>

                        <p>
                            {details.vendor_name}
                        </p>

                    </div>



                    <div>

                        <label>
                            Amount
                        </label>

                        <p>

                            ₹
                            {details.amount}

                        </p>

                    </div>



                    <div>

                        <label>
                            Status
                        </label>

                        <p>
                            {details.status}
                        </p>

                    </div>



                    <div>

                        <label>
                            Risk Level
                        </label>

                        <p>
                            {details.risk_level || "Low"}
                        </p>

                    </div>



                    <div>

                        <label>
                            Invoice Date
                        </label>

                        <p>

                            {
                                details.invoice_date
                                ?
                                new Date(
                                    details.invoice_date
                                )
                                .toLocaleDateString()
                                :
                                "-"
                            }

                        </p>

                    </div>


                </div>




                <hr />



                <h3>
                    OCR Extracted Data
                </h3>


                <div className="ocr-box">


                    {

                        details.extracted_text

                        ?

                        details.extracted_text

                        :

                        "No OCR data available"

                    }


                </div>




                <hr />



                <h3>
                    Prediction
                </h3>


                <div className="prediction-card">


                    <p>

                        Risk Score:

                        {" "}

                        {

                            details.risk_score || 0

                        }


                    </p>



                    <p>

                        Manual Approval:

                        {" "}

                        {

                            details.manual_review

                            ?

                            "Required"

                            :

                            "Not Required"

                        }

                    </p>



                </div>



            </div>


        </div>

    );

}


export default InvoiceDetailsModal;