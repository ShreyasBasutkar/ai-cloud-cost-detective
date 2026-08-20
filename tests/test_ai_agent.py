from ai_agent import generate_ai_recommendation


def test_ec2_recommendation():

    analysis = {
        "highest_service": "EC2 - Other",
        "highest_cost": 0.0004,
        "total_cost": 0.0007,
        "services": [
            {
                "service": "EC2 - Other",
                "cost": 0.0004
            },
            {
                "service": "Amazon S3",
                "cost": 0.0003
            }
        ]
    }

    recommendations = generate_ai_recommendation(analysis)

    assert len(recommendations) > 0
    assert any("EC2" in recommendation for recommendation in recommendations)
