def analyze_cost_data(response):
    """
    Analyze AWS Cost Explorer response and return
    aggregated service-level cost insights.
    """

    service_costs = {}

    for result in response["ResultsByTime"]:

        for group in result["Groups"]:

            service = group["Keys"][0]

            cost = float(
                group["Metrics"]["UnblendedCost"]["Amount"]
            )

            service_costs[service] = (
                service_costs.get(service, 0.0) + cost
            )

    # Convert dictionary into a list
    services = [
        {
            "service": service,
            "cost": cost
        }
        for service, cost in service_costs.items()
    ]

    # Sort from highest to lowest cost
    services.sort(
        key=lambda x: x["cost"],
        reverse=True
    )

    # Net total across all services
    total_cost = sum(
        service["cost"]
        for service in services
    )

    # Find highest positive-cost service
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

    return {
        "total_cost": total_cost,
        "highest_service": highest_service,
        "highest_cost": highest_cost,
        "services": services
    }
