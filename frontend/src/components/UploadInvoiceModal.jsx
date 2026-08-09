import { useState } from "react";
import api from "../api/api";


function UploadInvoiceModal({ close }) {


    const [file, setFile] = useState(null);

    const [loading, setLoading] = useState(false);

    const [message, setMessage] = useState("");



    const uploadInvoice = async (e)=>{

        e.preventDefault();


        if(!file){

            alert("Please select invoice file");

            return;

        }


        const formData = new FormData();


        formData.append(
            "file",
            file
        );


        try{


            setLoading(true);

            setMessage(
                "Uploading invoice..."
            );


            const response = await api.post(

                "/upload",

                formData,

                {
                    headers:{
                        "Content-Type":
                        "multipart/form-data"
                    }
                }

            );


            console.log(
                "UPLOAD RESPONSE:",
                response.data
            );


            setMessage(
                "Invoice uploaded successfully"
            );


            setTimeout(()=>{

                close();

            },1500);



        }
        catch(error){


            console.log(
                error
            );


            setMessage(
                "Upload failed"
            );


        }
        finally{

            setLoading(false);

        }


    };



    return (

        <div className="modal">


            <div className="upload-modal">


                <h2>
                    Upload Invoice
                </h2>



                <form onSubmit={uploadInvoice}>


                    <input

                        type="file"

                        accept=".pdf,.png,.jpg,.jpeg"

                        onChange={
                            (e)=>
                            setFile(
                                e.target.files[0]
                            )
                        }

                    />



                    {

                        file &&

                        <p>

                            Selected:
                            {" "}
                            {file.name}

                        </p>

                    }




                    <button

                        disabled={loading}

                    >

                        {

                            loading ?

                            "Uploading..."

                            :

                            "Upload"

                        }


                    </button>



                    {

                        message &&

                        <p className="upload-message">

                            {message}

                        </p>

                    }



                </form>




                <button

                    className="close-btn"

                    onClick={close}

                >

                    Cancel

                </button>



            </div>


        </div>

    );


}


export default UploadInvoiceModal;