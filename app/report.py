def generate_report(summary, recommendations, anomalies):
    print()
    print("=" * 60)
    print("        AI CLOUD COST DETECTIVE")
    print("=" * 60)

    print(f"\nCurrent Period Cost : ${summary['total_cost']:.8f}")
    print(f"Previous Period Cost : ${summary['previous_total']:.8f}")

    change = summary["cost_change_percent"]

    print(f"Cost Change : {change:+.2f}%")

    if summary["highest_service"]:
        print(
            f"Highest Cost Service : "
            f"{summary['highest_service']} "
            f"(${summary['highest_cost']:.8f})"
        )
    else:
        print("Highest Cost Service : None")

    print("\nService Wise Cost\n")

    for service in summary["services"]:
        print(
            f"{service['service']:<45}"
            f"${service['cost']:.8f}"
        )

    print("\nCost Anomalies\n")

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

    print("\nAI Cost Optimization Recommendations\n")

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):
        print(f"{index}. {recommendation}")

    print("\n" + "=" * 60)
