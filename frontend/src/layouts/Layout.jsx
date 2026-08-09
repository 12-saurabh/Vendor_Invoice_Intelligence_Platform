import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";


function Layout({children}){


    const [collapsed,setCollapsed] = useState(false);



    return (

        <div className="app-layout">


            <Sidebar

                collapsed={collapsed}

            />



            <div
                className={
                    collapsed
                    ?
                    "main-content collapsed"
                    :
                    "main-content"
                }
            >


                <Navbar

                    setCollapsed={
                        setCollapsed
                    }

                    collapsed={
                        collapsed
                    }

                />



                <div className="page-content">

                    {children}

                </div>



            </div>


        </div>

    );


}


export default Layout;