from aws_client import get_cost_explorer_client

try:
    client = get_cost_explorer_client()

    print("✅ Successfully created Cost Explorer client!")
    print(client)

except Exception as e:
    print("❌ Error:", e)
