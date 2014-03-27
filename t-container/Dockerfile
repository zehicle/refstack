# Docker Tempest in a Container (TCUP)
#
# Copyright (c) 2014 Alex Hirschfeld (d-qoi), no corporate affiliation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, `either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

FROM ubuntu 
RUN apt-get update

# Downloading tools
RUN apt-get install -y git wget unzip


#Downloading dependencies
RUN apt-get install -y python-pip libxml2-dev libxslt-dev lib32z1-dev python2.7-dev libssl-dev

#other dependencies
RUN apt-get install -y python-dev libxslt1-dev libsasl2-dev libsqlite3-dev libldap2-dev libffi-dev
RUN pip install ftp://xmlsoft.org/libxml2/python/libxml2-python-2.6.9.tar.gz

# Cloning RefStack to run the tests (we'll need to pull latest)
RUN git clone https://github.com/stackforge/refstack.git

# Version of TCUP 
# Changing REBUILDs the container from this point forward
ENV TCUP 0.1.0

# Get tempest code (one of two approaches)
# Option 1: Use the Source Code
# RUN git clone https://github.com/openstack/tempest
# Option 2: Use the Packaged Code
RUN wget https://github.com/openstack/tempest/archive/stable/havana.zip 
RUN unzip havana.zip 
RUN mv /tempest-stable-havana /tempest

#running setup
#RUN python /tempest/setup.py install

#making file to add exterior files
#RUN mkdir temp

#Tempest config creator
#ADD https://github.com/dlenwell/refstack/blob/master/refstack/common/tempest_config.py /temp/
#ADD http://9.30.139.135/openstack/tempest.conf /tempest/

#MORE DEPENDENCIES (for tempest config builder)
#ADD https://github.com/openstack/keystone/blob/master/requirements.txt /temp/
#ADD https://github.com/openstack/keystone/blob/master/test-requirements.txt /temp/

#using dependencies
# FAILING! > RUN pip install -r /tempest/requirements.txt
# FAILING! > RUN pip install -r /tempest/test-requirements.txt

#Get latest refstack
CMD cd refstack; git pull

