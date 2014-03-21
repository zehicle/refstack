TCUP Configuration
===========================

1. Install Docker using [Docker Instructions](https://www.docker.io/gettingstarted/#h_installation)

1. Get the code: `git clone http://github.com/stackforge/refstack`

1. enter RefStack: `cd refstack`

1. create/copy your OpenStack credentials into openrc.sh an file

1. Create the TCUP container: `docker build t-container`

1. Run the container: `docker run -v ``pwd``:/tcup:rw -i -t 32fe2d733d51 /bin/bash`

1. Inside the container run the following
   1. `source tcup/openrc.sh`
   1. `tcup/run_in_tcup.py`
