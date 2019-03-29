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

import ec2Factory as ec2Factory
import snsFactory as snsFactory
import sqsFactory as sqsFactory

region_name = 'us-east-1'

def dryRun():
    print 'lib/index.ec2Factory.getInstances({})'.format(region_name)
    print ec2Factory.getInstances(region_name)
    
    #print ec2Factory.getMetrics()
    
def run():
    return True
    
    
    
