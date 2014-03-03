#!/bin/bash
# docker run -v `pwd`:/refstack:ro -i -t 32fe2d733d51 /bin/bash
source /refstack/openrc.sh
tempest/run_tests.sh
