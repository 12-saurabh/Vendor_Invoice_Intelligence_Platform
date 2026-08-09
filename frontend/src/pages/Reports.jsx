import "../styles/reports.css";

function Reports(){

    const download=(type)=>{

        window.open(

            `http://localhost:8000/export/${type}`,

            "_blank"

        );

    };

    return(

        <div className="reports-page">

            <h1>Reports</h1>

            <p>Download invoice reports.</p>

            <div className="report-buttons">

                <button
                    onClick={()=>download("csv")}
                >
                    Download CSV
                </button>

                <button
                    onClick={()=>download("excel")}
                >
                    Download Excel
                </button>

                <button
                    onClick={()=>download("pdf")}
                >
                    Download PDF
                </button>

            </div>

        </div>

    );

}

export default Reports;