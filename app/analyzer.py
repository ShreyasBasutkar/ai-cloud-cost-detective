def analyze_cost_data(response):
    """
    Analyze AWS Cost Explorer response and return
    useful cost insights.
    """

    services = []

    total_cost = 0.0

    highest_service = None
    highest_cost = float("-inf")

    for result in response["ResultsByTime"]:

        for group in result["Groups"]:

            service = group["Keys"][0]

            cost = float(
                group["Metrics"]["UnblendedCost"]["Amount"]
            )

            services.append({
                "service": service,
                "cost": cost
            })

            total_cost += cost

            if cost > highest_cost:
                highest_cost = cost
                highest_service = service

    services.sort(
        key=lambda x: x["cost"],
        reverse=True
    )

    return {
        "total_cost": total_cost,
        "highest_service": highest_service,
        "highest_cost": highest_cost,
        "services": services
    }
