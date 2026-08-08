from collector import collect_cost_data
from analyzer import analyze_cost_data
from report import generate_report


def main():

    response = collect_cost_data()

    summary = analyze_cost_data(response)

    generate_report(summary)


if __name__ == "__main__":
    main()
