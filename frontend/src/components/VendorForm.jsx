import { useState } from "react";
import api from "../api/api";

function VendorForm({ vendor, close }) {

    const [form, setForm] = useState({

        name: vendor?.name || "",
        email: vendor?.email || "",
        phone: vendor?.phone || "",
        address: vendor?.address || ""

    });

    const change = (e) => {

        setForm({

            ...form,

            [e.target.name]: e.target.value

        });

    };

    const submit = async (e) => {

        e.preventDefault();

        if (vendor) {

            await api.put(`/vendors/${vendor.id}`, form);

        } else {

            await api.post("/vendors", form);

        }

        close();

    };

    return (

        <div className="modal">

            <form className="vendor-form" onSubmit={submit}>

                <h2>

                    {

                        vendor ?

                            "Edit Vendor"

                            :

                            "Add Vendor"

                    }

                </h2>

                <input
                    name="name"
                    placeholder="Vendor Name"
                    value={form.name}
                    onChange={change}
                />

                <input
                    name="email"
                    placeholder="Email"
                    value={form.email}
                    onChange={change}
                />

                <input
                    name="phone"
                    placeholder="Phone"
                    value={form.phone}
                    onChange={change}
                />

                <input
                    name="address"
                    placeholder="Address"
                    value={form.address}
                    onChange={change}
                />

                <button>

                    Save

                </button>

            </form>

        </div>

    );

}

export default VendorForm;