#!/usr/bin/env python3

import aws_cdk as cdk

from fargate_cdk.fargate_cdk_stack import FargateCdkStack


app = cdk.App()
FargateCdkStack(app, "fargate-cdk")

app.synth()
