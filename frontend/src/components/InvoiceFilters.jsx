function InvoiceFilters({

    search,
    setSearch,

    status,
    setStatus,

    risk,
    setRisk

}) {


    const resetFilters = () => {

        setSearch("");

        setStatus("");

        setRisk("");

    };


    return (

        <div className="invoice-filters">


            <input

                type="text"

                placeholder="Search invoice number or vendor..."

                value={search}

                onChange={(e)=>setSearch(e.target.value)}

                className="search-input"

            />


            <select

                value={status}

                onChange={(e)=>setStatus(e.target.value)}

            >

                <option value="">

                    All Status

                </option>


                <option value="Pending">

                    Pending

                </option>


                <option value="Processing">

                    Processing

                </option>


                <option value="Approved">

                    Approved

                </option>


                <option value="Rejected">

                    Rejected

                </option>


            </select>



            <select

                value={risk}

                onChange={(e)=>setRisk(e.target.value)}

            >

                <option value="">

                    All Risk

                </option>


                <option value="Low">

                    Low Risk

                </option>


                <option value="Medium">

                    Medium Risk

                </option>


                <option value="High">

                    High Risk

                </option>


            </select>



            <button

                className="reset-btn"

                onClick={resetFilters}

            >

                Reset

            </button>


        </div>

    );

}


export default InvoiceFilters;