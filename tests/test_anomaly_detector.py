from anomaly_detector import detect_anomalies


def test_new_spend_is_detected():
    analysis = {
        "services": [
            {
                "service": "Amazon EC2",
                "cost": 10.0
            }
        ],
        "previous_costs": {
            "Amazon EC2": 0.0
        }
    }

    anomalies = detect_anomalies(analysis)

    assert len(anomalies) == 1

    anomaly = anomalies[0]

    assert anomaly["service"] == "Amazon EC2"
    assert anomaly["previous_cost"] == 0.0
    assert anomaly["current_cost"] == 10.0
    assert anomaly["increase"] == 10.0
    assert anomaly["severity"] == "HIGH"


def test_near_zero_previous_cost_is_treated_as_new_spend():
    analysis = {
        "services": [
            {
                "service": "Amazon S3",
                "cost": 0.000002
            }
        ],
        "previous_costs": {
            "Amazon S3": 0.0000000016
        }
    }

    anomalies = detect_anomalies(analysis)

    assert len(anomalies) == 1

    anomaly = anomalies[0]

    assert anomaly["service"] == "Amazon S3"
    assert anomaly["previous_cost"] == 0.0000000016
    assert anomaly["current_cost"] == 0.000002
    assert anomaly["severity"] == "HIGH"
