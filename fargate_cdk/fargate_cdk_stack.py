from constructs import Construct
from aws_cdk.core import (
    Stack,
    aws_ec2 as ec2,
    Tags,
)


class FargateCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC with CIDR block 10.0.0.0/16 0/16
        vpc = ec2.Vpc(
            self, "StgVpc",
            cidr="10.0.0.0/16",
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public-1a",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="public-1b",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="public-1c",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="public-1d",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
            ]
        )

        # add tags to the VPC
        Tags.of(vpc).add("Name", "StgVpc")
        Tags.of(vpc).add("Environment", "Staging")
        Tags.of(vpc).add("Owner", "Angel")
        
        # add tas to the subnets
        for subnet in vpc.public_subnets:
            Tags.of(subnet).add("Name", "StgPublicSubnet")
            Tags.of(subnet).add("Environment", "Staging")
            Tags.of(subnet).add("Owner", "Angel")