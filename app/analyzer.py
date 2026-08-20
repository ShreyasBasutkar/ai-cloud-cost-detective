def analyze_cost_data(response):
    """
    Analyze AWS Cost Explorer response and return
    service-level costs and period comparison.
    """

    periods = response["ResultsByTime"]

    current_costs = {}
    previous_costs = {}

    for index, result in enumerate(periods):

        target = previous_costs if index == 0 else current_costs

        for group in result["Groups"]:

            service = group["Keys"][0]

            cost = float(
                group["Metrics"]["UnblendedCost"]["Amount"]
            )

            target[service] = (
                target.get(service, 0.0) + cost
            )

    # Current period services
    services = [
        {
            "service": service,
            "cost": cost
        }
        for service, cost in current_costs.items()
    ]

    services.sort(
        key=lambda x: x["cost"],
        reverse=True
    )

    total_cost = sum(
        service["cost"]
        for service in services
    )

    # Previous period total
    previous_total = sum(previous_costs.values())

    # Highest current-cost service
    positive_services = [
        service
        for service in services
        if service["cost"] > 0
    ]

    if positive_services:
        highest = positive_services[0]
        highest_service = highest["service"]
        highest_cost = highest["cost"]
    else:
        highest_service = None
        highest_cost = 0.0

    # Overall cost change
    if previous_total != 0:
        cost_change_percent = (
            (total_cost - previous_total)
            / abs(previous_total)
        ) * 100
    else:
        cost_change_percent = 0.0

    return {
        "total_cost": total_cost,
        "previous_total": previous_total,
        "cost_change_percent": cost_change_percent,
        "highest_service": highest_service,
        "highest_cost": highest_cost,
        "services": services,
        "previous_costs": previous_costs
    }
