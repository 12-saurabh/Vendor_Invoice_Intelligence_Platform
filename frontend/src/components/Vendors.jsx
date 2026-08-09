import { useEffect, useState } from "react";

import api from "../api/api";


function Vendors(){


    const [vendors,setVendors] = useState([]);

    const [loading,setLoading] = useState(true);

    const [search,setSearch] = useState("");


    const [vendor,setVendor] = useState({

        name:"",
        email:"",
        phone:""

    });



    const loadVendors = async()=>{


        try{


            const response = await api.get(
                "/vendors"
            );


            setVendors(
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

        loadVendors();

    },[]);




    const addVendor = async(e)=>{


        e.preventDefault();


        try{


            await api.post(
                "/vendors",
                vendor
            );


            setVendor({

                name:"",
                email:"",
                phone:""

            });


            loadVendors();


        }
        catch(error){

            console.log(error);

        }


    };




    const deleteVendor = async(id)=>{


        if(
            !window.confirm(
                "Delete vendor?"
            )
        )
        return;



        try{


            await api.delete(
                `/vendors/${id}`
            );


            loadVendors();


        }
        catch(error){

            console.log(error);

        }


    };





    const filtered = vendors.filter(
        (v)=>

        v.name
        ?.toLowerCase()
        .includes(
            search.toLowerCase()
        )

    );




    if(loading){

        return (

            <h2>
                Loading vendors...
            </h2>

        );

    }





    return (

        <div>


            <div className="invoice-header">


                <h2>

                    Vendor Management

                </h2>


            </div>





            <div className="vendor-form">


                <h3>
                    Add Vendor
                </h3>



                <form onSubmit={addVendor}>


                    <input

                        placeholder="Vendor Name"

                        value={vendor.name}

                        onChange={
                            e=>
                            setVendor({

                                ...vendor,

                                name:e.target.value

                            })
                        }

                    />



                    <input

                        placeholder="Email"

                        value={vendor.email}

                        onChange={
                            e=>
                            setVendor({

                                ...vendor,

                                email:e.target.value

                            })
                        }

                    />



                    <input

                        placeholder="Phone"

                        value={vendor.phone}

                        onChange={
                            e=>
                            setVendor({

                                ...vendor,

                                phone:e.target.value

                            })
                        }

                    />




                    <button>

                        Add Vendor

                    </button>



                </form>


            </div>





            <input

                className="search-input"

                placeholder="Search vendor..."

                value={search}

                onChange={
                    e=>
                    setSearch(
                        e.target.value
                    )
                }

            />





            <div className="table-container">


                <table>


                    <thead>

                        <tr>


                            <th>
                                Name
                            </th>


                            <th>
                                Email
                            </th>


                            <th>
                                Phone
                            </th>


                            <th>
                                Action
                            </th>


                        </tr>


                    </thead>



                    <tbody>


                    {

                    filtered.map(
                    (v)=>(


                    <tr key={v.id}>


                        <td>
                            {v.name}
                        </td>


                        <td>
                            {v.email}
                        </td>


                        <td>
                            {v.phone}
                        </td>



                        <td>


                            <button

                            onClick={()=>
                            deleteVendor(v.id)}

                            >

                                Delete

                            </button>


                        </td>


                    </tr>


                    ))

                    }


                    </tbody>


                </table>


            </div>



        </div>

    );


}


export default Vendors;