#!/usr/bin/env python
#
# Copyright (c) 2014 Dell Computer, Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

# This file creates and runs Tempest in a Docker Container
import os
import subprocess
import commands
import sys
import re

if __name__ == "__main__":

    # Confirm that they've sourced their openrc credentials already
    if not os.environ.get('OS_PASSWORD'):
        raise Exception('OS_PASSWORD Env Variable Missing: You may need to "source openrc.sh" first.')
    if not os.environ.get('OS_USERNAME'):
        raise Exception('OS_USERNAME Env Variable Missing: You need to "source openrc.sh" file first.')
    if not os.environ.get('OS_AUTH_URL'):
        raise Exception('OS_AUTH_URL Env Variable Missing: You need to "source openrc.sh" file first.')

    test_id = os.environ.get('TEST_ID')
    if not test_id:
        test_id = 1000

    api_addr = os.environ.get('API_SERVER_ADDRESS')
    if not api_addr:
        api_addr = "http://refstack.org/result"


    build_output = commands.getoutput("docker build t-container")
    image = re.search("Successfully built (.*)", build_output).group(1)
    print "TCUP Built Docker Image ID: "+image


    docker_run = "docker run -i -t "+image
    for e in os.environ:
      docker_run += ' -e '+e+'="'+os.environ[e]+'"'

    docker_run += " python refstack/tools/execute_test.py --callback ${api_addr} ${test_id}"
    print docker_run
    docker_output = commands.getoutput(docker_run)
    print docker_output
