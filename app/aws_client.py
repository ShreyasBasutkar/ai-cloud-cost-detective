import boto3


def get_cost_explorer_client():
    """
    Create and return an AWS Cost Explorer client.
    """
    return boto3.client(
        "ce",
        region_name="us-east-1"
    )
