import { useState } from "react";
import api from "../api/api";

import "../styles/upload.css";


function UploadInvoice(){

    const [file,setFile] = useState(null);

    const [loading,setLoading] = useState(false);

    const [message,setMessage] = useState("");



    function handleFile(e){

        const selected = e.target.files[0];

        if(selected){

            setFile(selected);

            setMessage("");

        }

    }



    async function uploadInvoice(){


        if(!file){

            setMessage(
                "Please select invoice PDF"
            );

            return;

        }



        const formData = new FormData();

        formData.append(
            "file",
            file
        );



        try{


            setLoading(true);


            const res = await api.post(

                "/upload",

                formData,

                {

                    headers:{

                        "Content-Type":
                        "multipart/form-data"

                    }

                }

            );



            console.log(res.data);


            setMessage(
                "Invoice uploaded successfully"
            );


        }

        catch(err){


            console.log(err);


            setMessage(
                "Upload failed"
            );


        }

        finally{


            setLoading(false);


        }


    }



    return (

        <div className="upload-container">


            <h1>
                Upload Invoice
            </h1>


            <p>
                Upload vendor invoice PDF for AI processing
            </p>



            <div className="upload-box">


                <input

                    type="file"

                    accept="application/pdf"

                    onChange={handleFile}

                />



                {

                file &&

                <div className="file">

                    Selected:

                    <b>
                        {file.name}
                    </b>

                </div>

                }



                <button

                    onClick={uploadInvoice}

                    disabled={loading}

                >

                {

                loading

                ?

                "Processing..."

                :

                "Upload Invoice"

                }


                </button>



                {

                message &&

                <p className="message">

                    {message}

                </p>

                }


            </div>


        </div>

    );


}


export default UploadInvoice;