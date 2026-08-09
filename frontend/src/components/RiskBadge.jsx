function RiskBadge({ risk }) {

    const value = (risk || "").toLowerCase();

    return (
        <span className={`risk-badge ${value}`}>
            {risk}
        </span>
    );

}

export default RiskBadge;