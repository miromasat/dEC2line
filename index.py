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

i.account_number = '09876543234'
i.region_name = 'eu-west-1'
i.tag_name = 'Name'
i.tag_value = 'ParallelCluster'
i.instance_type = None
i.instance_arn = None
i.vpc_arn = None
i.subnet_arn = None
i.sns_email = [ 'example@example.com' ]
i.sns_number = [ '+44 89743523647' ]
i.cpu_threshold = 25
i.moreless = 'less'
i.sqs_lenght = 5
i.sqs_cleanup = True

def handler(event, context):
    return True


if __name__ == '__main__':
    print 'i.dryRun()'
    i.dryRun()