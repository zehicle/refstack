#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2014 Dell Inc.
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

import os
import subprocess
import commands
import sys


# custom 
if os.environ.get('TCUP'):
    os.chdir('tcup') 
    from refstack.tools.tempest_tester import TempestTester

if __name__ == "__main__":

    # make sure that we have critical variables
    if not (os.environ.get('OS_AUTH_URL') and os.environ.get('OS_PASSWORD')):
        raise Exception("You need to 'source tcup/openrc.sh' file first.")

    # only act if inside a container
    if not os.environ.get('TCUP'):
        raise Exception('This script only runs within the TCUP container')

    # aggressive diagnostics for now, turn down later
    print "Provided URL respond?"
    print commands.getoutput("wget -S -q -o ../debug.html " + os.environ.get('OS_AUTH_URL'))
    print "Credentials Work?"
    print commands.getoutput("keystone catalog")


    #TODO(JMC): Consider using PIPE instead, ala 
    # http://stackoverflow.com/questions/13332268/python-subprocess-command-with-pipe
    test_id = "1000"
    TempestTester(test_id).execute_test()

