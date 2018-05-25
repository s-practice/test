# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import, unicode_literals
import os
import boto3


PIPELINE_NAME = os.environ['PIPELINE_NAME']
AWS_REGION = "ap-northeast-1"

codepipeline = boto3.client('codepipeline', region_name=AWS_REGION)

get_pipeline_response = codepipeline.get_pipeline(
    name=PIPELINE_NAME
)

get-pipeline-state_response = codepipeline.get-pipeline-state(
    name=PIPELINE_NAME
)

if __name__ == '__main__':
    print('get_pipeline_response: ' + get_pipeline_response)
    print('-----------------')
    print('get-pipeline-state_response: ' + get-pipeline-state_response)
    print('-----------------')
    print('-----------------')
    print('-----------------')
