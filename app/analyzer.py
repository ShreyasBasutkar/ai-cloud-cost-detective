def analyze_costs(cost_data):
    print("Analyzing cloud costs...")

    total = sum(cost_data.values())

    highest_service = max(cost_data, key=cost_data.get)

    return {
        "total_cost": total,
        "highest_service": highest_service
    }
