from collector import collect_cost_data
from analyzer import analyze_cost_data

response = collect_cost_data()

services = analyze_cost_data(response)

print()

print("======= Service Cost =======")

for service in services:

    print(
        f"{service['service']:<45} ${service['cost']:.8f}"
    )
