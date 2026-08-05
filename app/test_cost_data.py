import json

from collector import collect_cost_data

try:
    response = collect_cost_data()

    print("✅ Successfully fetched AWS billing data!\n")

    print(json.dumps(response, indent=4, default=str))

except Exception as e:
    print("❌ Error:", e)
