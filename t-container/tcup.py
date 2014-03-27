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
import commands
import re

if __name__ == "__main__":

    # Confirm you've sourced their openrc credentials already
    for e in {'OS_PASSWORD', 'OS_USERNAME', 'OS_AUTH_URL'}:
        if not os.environ.get(e):   
            e + 'Env Variable Missing: You may need to "source openrc.sh".'
            raise Exception(exp)

    # build the container
    print "Downloading & Building T-CUP Image...(may take a long time)"
    docker_file_source = "t-container"
    print "\texecuting `docker build " + docker_file_source + "`"
    build_output = commands.getoutput("docker build " + docker_file_source)

    # provide friendly output progress message
    search_for = "Successfully built ([0-9a-f]{12})"
    image = re.search(search_for, build_output).group(1)
    print "\nT-CUP Built Docker Image ID: " + image

    # collect environment variables to pass, we don't want all of them
    e_vars = dict(os.environ)
    for e in {"LS_COLORS", "HOME", "PATH", "PWD", "OLDPWD", "LESSCLOSE", \
              "SSH_CONNECTION"}:
        try: 
            e_vars.pop(e, None)
        except: 
            pass

    # test specific configuration
    if not os.environ.get('TEST_ID'): 
        e_vars["test_id"] = "1000"  # TODO: generated good value!

    if not os.environ.get('API_SERVER_ADDRESS'): 
        e_vars["api_addr"] = "http://refstack.org/result"

    # create the docker run command line
    docker_run = "docker run -d -i"
    for e in e_vars: docker_run += ' -e "' + e + '=' + e_vars[e] + '"'
    docker_run += ' -t '+ image
    debug = 1
    if debug: 
            docker_run += " /bin/bash"
    else: 
        docker_run += " cd refstack; python refstack/tools/execute_test.py"
        docker_run += " --callback ${api_addr} ${test_id}"
    print "\texecuting: '" + docker_run + "'"
    
    # start the container and advise the user about how to attach
    docker_output = commands.getoutput(docker_run)
    print "\nYou can monitor the T-CUP results using (hint: press [enter])"
    print "\n\t'sudo docker attach " + docker_output[0:12] + "'"