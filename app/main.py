from database import initialize_database, save_cost_run
from collector import collect_cost_data
from analyzer import analyze_cost_data
from ai_agent import generate_ai_recommendation
from anomaly_detector import detect_anomalies
from report import generate_report


def main():

    initialize_database()

    response = collect_cost_data()

    summary = analyze_cost_data(response)

    anomalies = detect_anomalies(summary)

    recommendations = generate_ai_recommendation(summary)

    save_cost_run(summary, anomalies)

    generate_report(
        summary,
        recommendations,
        anomalies
    )

if __name__ == "__main__":
    main()
