TCUP Configuration
===========================

The following instructions are designs run RefStack/Tempest in a container with minimal setup on your system.

> These steps are _not_ do not install RefStack for contributions or development, they are intended for a user who wants to just run and report test results.

1. Install Docker using [[https://www.docker.io/gettingstarted/#h_installation]]

1. Get the code: `wget https://raw.githubusercontent.com/stackforge/refstack/master/t-container/tcup.py`
  1. note: you can also get the code by cloning the RefStack and running the code in `/t-container`

1. Set your environment variables to access the test target cloud
  1. generally, you will `source openrc.sh` to load the cloud credentials and URLs

1. Run TCUP: `sudo python tcup.py`
  1. If you want to watch the process, you will need to `docker attach [container id]`
  git clone http://github.com/stackforge/refstack


Notes:
1. Orphaned Containers: Over time, you may end up with [orphaned contaniers](http://jimhoskins.com/2013/07/27/remove-untagged-docker-images.html), use the following to clean them up
  1. `sudo docker rm $(docker ps -a -q)`
  1. `sudo docker rmi $(docker images | grep "^<none>" | awk "{print $3}")`