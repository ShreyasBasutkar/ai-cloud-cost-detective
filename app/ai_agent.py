def generate_ai_recommendation(analysis):
    """
    Generate cloud cost optimization recommendations
    based on analyzed AWS cost data.
    """

    recommendations = []

    highest_service = analysis["highest_service"]
    highest_cost = analysis["highest_cost"]
    services = analysis["services"]

    if not highest_service:
        return ["No significant cloud costs detected."]

    # EC2 recommendations
    if "EC2" in highest_service:
        recommendations.append(
            "Review EC2 resources for unused or underutilized instances."
        )

        recommendations.append(
            "Check EBS volumes and snapshots associated with unused EC2 resources."
        )

    # S3 recommendations
    elif "S3" in highest_service or "Simple Storage Service" in highest_service:
        recommendations.append(
            "Review S3 storage usage and identify unused objects."
        )

        recommendations.append(
            "Consider S3 lifecycle policies to move older data "
            "to cheaper storage classes."
        )

    # Data transfer recommendations
    elif "Data Transfer" in highest_service:
        recommendations.append(
            "Review AWS data transfer costs and identify unnecessary "
            "cross-region or external traffic."
        )

    # Generic recommendation
    else:
        recommendations.append(
            f"Review {highest_service} usage and identify "
            "unused or underutilized resources."
        )

    # Calculate percentage using positive service costs only.
    positive_costs = [
        service["cost"]
        for service in services
        if service["cost"] > 0
    ]

    gross_positive_cost = sum(positive_costs)

    if gross_positive_cost > 0:
        percentage = (highest_cost / gross_positive_cost) * 100

        if percentage > 70:
            recommendations.append(
                f"{highest_service} represents approximately "
                f"{percentage:.2f}% of gross positive service costs. "
                "Prioritize this service for optimization."
            )

    return recommendations
