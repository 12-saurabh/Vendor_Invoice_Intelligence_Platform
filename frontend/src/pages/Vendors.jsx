import { useEffect, useState } from "react";
import api from "../api/api";

import "../styles/vendors.css";


function Vendors(){

    const [vendors,setVendors] = useState([]);

    const [search,setSearch] = useState("");

    const [name,setName] = useState("");

    const [email,setEmail] = useState("");

    const [loading,setLoading] = useState(false);



    useEffect(()=>{

        fetchVendors();

    },[]);



    async function fetchVendors(){

        try{

            const res = await api.get(
                "/vendors"
            );

            setVendors(res.data);

        }
        catch(err){

            console.log(err);

        }

    }



    async function addVendor(){


        if(!name || !email){

            alert(
                "Enter vendor details"
            );

            return;

        }


        try{


            setLoading(true);


            await api.post(
                "/vendors",
                {

                    name:name,

                    email:email

                }

            );


            setName("");

            setEmail("");


            fetchVendors();


        }

        catch(err){

            console.log(err);

        }

        finally{

            setLoading(false);

        }


    }




    const filtered =
    vendors.filter((vendor)=>

        JSON.stringify(vendor)
        .toLowerCase()
        .includes(
            search.toLowerCase()
        )

    );



    return (

    <div className="vendor-container">


        <div className="vendor-header">

            <h1>
                Vendor Management
            </h1>

            <p>
                Manage suppliers and vendor information
            </p>

        </div>




        <div className="add-vendor">


            <input

            placeholder="Vendor Name"

            value={name}

            onChange={
                e=>setName(e.target.value)
            }

            />



            <input

            placeholder="Vendor Email"

            value={email}

            onChange={
                e=>setEmail(e.target.value)
            }

            />


            <button

            onClick={addVendor}

            >

            {
            loading
            ?
            "Adding..."
            :
            "Add Vendor"
            }


            </button>


        </div>





        <input

        className="search-vendor"

        placeholder="Search vendor..."

        value={search}

        onChange={
            e=>setSearch(e.target.value)
        }

        />





        <div className="vendor-table">


        <table>


        <thead>

        <tr>

        <th>
            ID
        </th>

        <th>
            Vendor Name
        </th>

        <th>
            Email
        </th>

        <th>
            Status
        </th>


        </tr>

        </thead>



        <tbody>


        {
        filtered.map(
        (vendor)=>(


        <tr key={vendor.id}>


        <td>
            {vendor.id}
        </td>


        <td>
            {vendor.name}
        </td>


        <td>
            {vendor.email}
        </td>


        <td>

        <span className="active">

        Active

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


export default Vendors;