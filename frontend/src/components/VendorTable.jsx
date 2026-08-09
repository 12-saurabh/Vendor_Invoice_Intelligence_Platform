import React from "react";

function VendorTable({ vendors, onEdit, onDelete }) {

    return (

        <table className="vendor-table">

            <thead>

                <tr>

                    <th>Name</th>

                    <th>Email</th>

                    <th>Phone</th>

                    <th>Address</th>

                    <th>Actions</th>

                </tr>

            </thead>

            <tbody>

                {

                    vendors.map(v => (

                        <tr key={v.id}>

                            <td>{v.name}</td>

                            <td>{v.email}</td>

                            <td>{v.phone}</td>

                            <td>{v.address}</td>

                            <td>

                                <button
                                    onClick={() => onEdit(v)}
                                >
                                    Edit
                                </button>

                                <button
                                    onClick={() => onDelete(v.id)}
                                >
                                    Delete
                                </button>

                            </td>

                        </tr>

                    ))

                }

            </tbody>

        </table>

    );

}

export default VendorTable;