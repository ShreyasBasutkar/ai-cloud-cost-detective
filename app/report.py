def generate_report(cost_data, analysis, recommendation):
    print("Generating report...\n")

    print("===== CLOUD COST REPORT =====")

    print("\nServices")

    for service, cost in cost_data.items():
        print(f"{service}: ${cost}")

    print(f"\nTotal Cost: ${analysis['total_cost']}")

    print(f"Highest Cost Service: {analysis['highest_service']}")

    print("\nRecommendation")

    print(recommendation)
