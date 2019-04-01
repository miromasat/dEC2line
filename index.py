######################################################################################################################
#  Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.                                           #
#                                                                                                                    #
#  Licensed under the Amazon Software License (the "License"). You may not use this file except in compliance        #
#  with the License. A copy of the License is located at                                                             #
#                                                                                                                    #
#      http://aws.amazon.com/asl/                                                                                    #
#                                                                                                                    #
#  or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES #
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions    #
#  and limitations under the License.                                                                                #
######################################################################################################################

import boto3
import json
import re
import os
import sys

import lib.index as i

i.account_number    = None          #OPTIONAL, if not specified, account derived from EC2/Lambda
i.region_name       = 'eu-west-1'   #REQUIRED
i.tag_name          = None          #OPTIONAL
i.tag_value         = None          #OPTIONAL
i.instance_type     = None          #OPTIONAL
i.instance_arn      = None          #OPTIONAL
i.vpc_arn           = None          #OPTIONAL
i.subnet_arn        = None          #OPTIONAL
i.sns_email         = None          #OPTIONAL
i.sns_number        = None          #OPTIONAL
i.cpu_threshold     = 10            #OPTIONAL, if not specified, set to 10%
i.moreless          = 'less'        #OPTIONAL, if not specified, set to 'less'
i.sqs_arn           = None          #REQUIRED     
i.sqs_lenght        = 5             #OPTIONAL, if not specified, set to 5
i.sqs_cleanup       = True          #OPTIONAL, if not specified, set to True

def handler(event, context):
    i.account_number    = os.environ['sqs_cleanup']
    i.region_name       = os.environ['region_name']
    i.tag_name          = os.environ['tag_name']
    i.tag_value         = os.environ['tag_value']
    i.instance_type     = os.environ['instance_type']
    i.instance_arn      = os.environ['instance_arn']
    i.vpc_arn           = os.environ['vpc_arn']
    i.subnet_arn        = os.environ['subnet_arn']
    i.sns_email         = os.environ['sns_email']
    i.sns_number        = os.environ['sns_number']
    i.cpu_threshold     = os.environ['cpu_threshold']
    i.moreless          = os.environ['moreless']
    i.sqs_arn           = os.environ['moreless']
    i.sqs_lenght        = os.environ['sqs_lenght']
    i.sqs_cleanup       = os.environ['sqs_cleanup']
    
    print 'i.run()'
    i.run()


if __name__ == '__main__':
    print 'i.dryRun()'
    i.dryRun()