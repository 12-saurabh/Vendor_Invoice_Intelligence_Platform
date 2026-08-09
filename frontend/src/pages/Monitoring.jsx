import "../styles/monitoring.css";

function Monitoring(){

    return(

        <div className="monitoring-page">

            <div className="monitoring-header">

                <h1>
                    System Monitoring
                </h1>

                <p>
                    Real-time application metrics powered by Prometheus and Grafana
                </p>

            </div>


            <div className="grafana-container">


                <iframe

                    src="http://localhost:3000/d/fastapi-dashboard/vendor-invoice-monitoring?orgId=1&refresh=5s"

                    title="Grafana Dashboard"

                    width="100%"

                    height="700"

                    frameBorder="0"

                />


            </div>


        </div>

    );

}


export default Monitoring;