def detect_anomalies(analysis):
    """
    Detect meaningful cost increases between
    the previous and current periods.
    """

    anomalies = []

    current_costs = {
        service["service"]: service["cost"]
        for service in analysis["services"]
    }

    previous_costs = analysis["previous_costs"]

    for service, current_cost in current_costs.items():

        previous_cost = previous_costs.get(service, 0.0)

        if previous_cost <= 0:
            continue

        increase = current_cost - previous_cost

        if increase <= 0:
            continue

        change_percent = (
            increase / abs(previous_cost)
        ) * 100

        # Ignore tiny cost movements.
        if increase < 1.00 and change_percent < 50:
            continue

        if change_percent >= 100:
            severity = "HIGH"
        elif change_percent >= 75:
            severity = "MEDIUM"
        elif change_percent >= 50:
            severity = "LOW"
        else:
            continue

        anomalies.append({
            "service": service,
            "previous_cost": previous_cost,
            "current_cost": current_cost,
            "increase": increase,
            "change_percent": change_percent,
            "severity": severity
        })

    anomalies.sort(
        key=lambda x: x["increase"],
        reverse=True
    )
