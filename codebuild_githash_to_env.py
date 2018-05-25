# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import, unicode_literals
import sys
import os
import boto3
import urllib.request, urllib.parse

PIPELINE_NAME = os.environ['PIPELINE_NAME']
AWS_REGION = "ap-northeast-1"


codepipeline = boto3.client('codepipeline', region_name=AWS_REGION)
response = codepipeline.get_pipeline(
    name=PIPELINE_NAME
)

if __name__ == '__main__':
    print(response)
