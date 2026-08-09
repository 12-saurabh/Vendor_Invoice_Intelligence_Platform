function StatusBadge({ status }) {

    const value = (status || "").toLowerCase();

    return (
        <span className={`status-badge ${value}`}>
            {status}
        </span>
    );

}

export default StatusBadge;