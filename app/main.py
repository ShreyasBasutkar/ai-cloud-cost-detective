from collector import collect_cost_data
from analyzer import analyze_costs
from ai_agent import generate_ai_recommendation
from report import generate_report


def main():
    print("=" * 50)
    print(" AI Cloud Cost Detective ")
    print("=" * 50)

    cost_data = collect_cost_data()

    analysis = analyze_costs(cost_data)

    recommendation = generate_ai_recommendation(analysis)

    generate_report(cost_data, analysis, recommendation)

    print("\nApplication Finished Successfully!")


if __name__ == "__main__":
    main()
