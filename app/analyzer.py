from datetime import date


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

    # Highest cost first
    services.sort(
        key=lambda x: x["cost"],
        reverse=True
    )

    # Net current-period cost
    # Includes positive service costs and negative
    # credits/refunds/adjustments.
    total_cost = sum(
        service["cost"]
        for service in services
    )

    # Gross positive service cost
    # Represents actual positive service spending
    # before credits/refunds/adjustments.
    gross_positive_cost = sum(
        service["cost"]
        for service in services
        if service["cost"] > 0
    )

    # Credits / adjustments
    credits_adjustments = (
        total_cost - gross_positive_cost
    )

    # Previous period total
    previous_total = sum(
        previous_costs.values()
    )

    # Previous gross positive service cost
    previous_gross_positive_cost = sum(
        cost
        for cost in previous_costs.values()
        if cost > 0
    )

    # Highest positive-cost service
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

    # Gross service cost change
    #
    # This measures the change in actual positive
    # service spending and prevents credits/refunds
    # from distorting the percentage.
    if previous_gross_positive_cost != 0:
        cost_change_percent = (
            (gross_positive_cost - previous_gross_positive_cost)
            / previous_gross_positive_cost
        ) * 100
    else:
        cost_change_percent = 0.0

    return {
        "run_date": date.today().isoformat(),
        "total_cost": total_cost,
        "gross_positive_cost": gross_positive_cost,
        "credits_adjustments": credits_adjustments,
        "previous_total": previous_total,
        "previous_gross_positive_cost": previous_gross_positive_cost,
        "cost_change_percent": cost_change_percent,
        "highest_service": highest_service,
        "highest_cost": highest_cost,
        "services": services,
        "previous_costs": previous_costs
    }
