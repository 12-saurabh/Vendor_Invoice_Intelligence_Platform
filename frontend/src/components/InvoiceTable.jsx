import StatusBadge from "./StatusBadge";
import RiskBadge from "./RiskBadge";

function InvoiceTable({ invoices, onView, onDelete }) {

    if (invoices.length === 0) {
        return (
            <div className="empty-table">
                <h3>No invoices found</h3>
            </div>
        );
    }

    return (

        <div className="table-container">

            <table className="invoice-table">

                <thead>

                    <tr>

                        <th>Invoice No</th>

                        <th>Vendor</th>

                        <th>Amount</th>

                        <th>Status</th>

                        <th>Risk</th>

                        <th>Date</th>

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {invoices.map((invoice) => (

                        <tr key={invoice.id}>

                            <td>{invoice.invoice_number}</td>

                            <td>{invoice.vendor_name}</td>

                            <td>

                                ₹{Number(invoice.amount).toLocaleString()}

                            </td>

                            <td>

                                <StatusBadge
                                    status={invoice.status}
                                />

                            </td>

                            <td>

                                <RiskBadge
                                    risk={invoice.risk_level}
                                />

                            </td>

                            <td>

                                {invoice.invoice_date
                                    ? new Date(invoice.invoice_date)
                                          .toLocaleDateString()
                                    : "-"}

                            </td>

                            <td>

                                <button
                                    className="view-btn"
                                    onClick={() => onView(invoice)}
                                >
                                    View
                                </button>

                                <button
                                    className="delete-btn"
                                    onClick={() => onDelete(invoice.id)}
                                >
                                    Delete
                                </button>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default InvoiceTable;