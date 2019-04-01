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
import time

import ec2Factory as ec2Factory
import snsFactory as snsFactory
import sqsFactory as sqsFactory

region_name = 'us-east-1'

def dryRun():
    print 'current time='+str(time.time())
    print 'instances = lib/index.ec2Factory.getInstances({})'.format(region_name)
    instances = ec2Factory.getInstances(region_name)
    print 'exampleInstance = lib/index.ec2Factory.getMetrics.({})'.format(instances[1]['InstanceId'])
    #intNow, startTime, endTime, period, statistics, unit, metrics, outputName, instance
    exampleInstance = ec2Factory.getMetrics(
                                    int(time.time()*1000),
                                    1200*1000,
                                    0,
                                    60,
                                    'Average',
                                    {'CPUUtilization': 'Percent'},
                                    ['CPUUtilization'],
                                    'textfile',
                                    instances[0],
                    ) 
    print exampleInstance
    
def run():
    return True
    
    
    
