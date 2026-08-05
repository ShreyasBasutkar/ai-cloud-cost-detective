from datetime import date, timedelta

from aws_client import get_cost_explorer_client


def collect_cost_data():
    client = get_cost_explorer_client()

    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": start_date.strftime("%Y-%m-%d"),
            "End": end_date.strftime("%Y-%m-%d")
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }
        ]
    )

    return response
