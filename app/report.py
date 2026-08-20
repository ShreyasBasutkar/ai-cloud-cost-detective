def generate_report(summary, recommendations):
    print()
    print("=" * 60)
    print("        AI CLOUD COST DETECTIVE")
    print("=" * 60)

    print(f"\nTotal AWS Cost : ${summary['total_cost']:.8f}")

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

    print("\nAI Cost Optimization Recommendations\n")

    for index, recommendation in enumerate(recommendations, start=1):
        print(f"{index}. {recommendation}")

    print("\n" + "=" * 60)
