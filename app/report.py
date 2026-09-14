def generate_report(summary, recommendations, anomalies):

    print()
    print("=" * 60)
    print("        AI CLOUD COST DETECTIVE")
    print("=" * 60)

    print("\nCURRENT PERIOD")

    print(
        f"Net Cost              : "
        f"${summary['total_cost']:.8f}"
    )

    print(
        f"Gross Service Cost    : "
        f"${summary['gross_positive_cost']:.8f}"
    )

    print(
        f"Credits / Adjustments : "
        f"${summary['credits_adjustments']:.8f}"
    )

    print("\nPREVIOUS PERIOD")

    print(
        f"Net Cost              : "
        f"${summary['previous_total']:.8f}"
    )

    change = summary["cost_change_percent"]

    print(
        f"\nCost Change           : "
        f"{change:+.2f}%"
    )

    if summary["highest_service"]:

        print(
            f"Highest Cost Service  : "
            f"{summary['highest_service']} "
            f"(${summary['highest_cost']:.8f})"
        )

    else:

        print("Highest Cost Service  : None")

    print("\nTOP COST DRIVERS\n")

    positive_services = [
        service
        for service in summary["services"]
        if service["cost"] > 0
    ]

    for index, service in enumerate(
        positive_services[:5],
        start=1
    ):

        print(
            f"{index}. "
            f"{service['service']:<40}"
            f"${service['cost']:.8f}"
        )

    print("\nCOST ANOMALIES\n")

    if anomalies:

        for anomaly in anomalies:

            print(
                f"⚠️ {anomaly['severity']} | "
                f"{anomaly['service']} | "
                f"{anomaly['change_percent']:+.2f}%"
            )

            print(
                f"   Previous : "
                f"${anomaly['previous_cost']:.8f}"
            )

            print(
                f"   Current  : "
                f"${anomaly['current_cost']:.8f}"
            )

    else:

        print("No significant cost anomalies detected.")

    print("\nAI COST OPTIMIZATION RECOMMENDATIONS\n")

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        print(
            f"{index}. {recommendation}"
        )

    print("\n" + "=" * 60)
