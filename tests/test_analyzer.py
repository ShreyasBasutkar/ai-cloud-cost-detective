import pytest

from analyzer import analyze_cost_data


def test_analyze_cost_data():
    response = {
        "ResultsByTime": [
            {
                "Groups": [
                    {
                        "Keys": ["EC2 - Other"],
                        "Metrics": {
                            "UnblendedCost": {
                                "Amount": "0.0004"
                            }
                        }
                    },
                    {
                        "Keys": ["Amazon S3"],
                        "Metrics": {
                            "UnblendedCost": {
                                "Amount": "0.0001"
                            }
                        }
                    }
                ]
            },
            {
                "Groups": [
                    {
                        "Keys": ["EC2 - Other"],
                        "Metrics": {
                            "UnblendedCost": {
                                "Amount": "0.0002"
                            }
                        }
                    }
                ]
            }
        ]
    }

    result = analyze_cost_data(response)

    assert result["total_cost"] == pytest.approx(0.0007)

    assert result["highest_service"] == "EC2 - Other"

    assert result["highest_cost"] == pytest.approx(0.0006)

    assert len(result["services"]) == 2
