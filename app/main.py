from collector import collect_cost_data
from analyzer import analyze_cost_data
from ai_agent import generate_ai_recommendation
from anomaly_detector import detect_anomalies
from report import generate_report


def main():

    response = collect_cost_data()

    summary = analyze_cost_data(response)

    anomalies = detect_anomalies(summary)

    recommendations = generate_ai_recommendation(summary)

    generate_report(
        summary,
        recommendations,
        anomalies
    )


if __name__ == "__main__":
    main()
