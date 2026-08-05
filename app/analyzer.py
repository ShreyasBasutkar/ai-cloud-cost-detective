def analyze_cost_data(response):
    """
    Extract service-wise cost information from the
    AWS Cost Explorer response.
    """

    services = []

    for result in response["ResultsByTime"]:

        for group in result["Groups"]:

            service = group["Keys"][0]

            amount = float(
                group["Metrics"]["UnblendedCost"]["Amount"]
            )

            services.append(
                {
                    "service": service,
                    "cost": amount
                }
            )

    return services
