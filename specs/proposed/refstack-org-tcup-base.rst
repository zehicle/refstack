Base TCUP environment for refstack.org
==========================================

TCUP (Tempest in a Container, Upload from Probe) is a self-contained, universal Tempest environment that can be widely used by the community with minimal effort AND minimal support effort by the Refstack team.

Problem description
===================

For DefStack and the core definition, we need to collect lots and lots of test runs against deployed OpenStack clouds.  Many of these clouds are behind firewalls and not accessible by 3rd parties.  So we need to make it super easy to make running Tempest and result uploads as accessible as possible.

Community access is the goal of TCUP.  While the original and primary intent of Tempest was to test OpenStack code, having a large body of tests creates unique opportunities for us.  DefCore uses the tests as a way to define core capabilities.  

Installing and configuring Tempest presents a challenge for many in the community.  TCUP's job is to reduce that complexity to the smallest possible set.

Requirements:

* It should not matter which Linux distro they are using
* Users should not have to figure out which code to check out
* Users should not have to deal with packages or pips
* Users should not have to determine where to upload their results
* Users identities must be hidden unless they agree/ask to have them published
* When the test is complete, the test system dissolves

Anti-Requirements:

* Users should not need to checkout or clone any code
* Users should not have to edit configuration files

Proposed change
===============

TCUP should be designed in as simple a way as possible.

Running TCUP should only require Docker (.9+), a single tcup.py file with minimal dependencies, working OpenStack cloud credentials and an Internet connection.

Environment variables from the host (OS-*) will be passed into the container.  The container should not start unless critical OS_ variables are in place.

There should be a `--debug` mode to allow for user testing and debug.  The debug flag should NOT start tests automatically and should map the user pwd into /dev in the TCUP container.

There must be both a way to use local code (refstack) to run TCUP and also a simple file download approach.  These methods should be functionally identical.

While there may be broad uses of TCUP for test automation, it is not desirable to overload them at the expense of manual usability.  TCUP should be very simple of users in this pass.

Alternatives
------------

It would be possible to create a single-use VM for this testing.  That would require much more download time, build effort and maintenance.

It would be possible to setup a cloud-based process to run Tempest (this is a Refstack use case); however, this would not reach private clouds.  It also does not give the user control of the data.

Data model impact
-----------------

None.

REST API impact
---------------

None; however, TCUP will rely on a stable upload REST API.


Security impact
---------------

User passwords are passed into the container and should be redacted from log entries.

We should prompt the user (from the tcup.py) code to enter a password if none is provided in the environment.

Passwords must not be stored by TCUP!

Notifications impact
--------------------

None

Other end user impact
---------------------

TCUP is designed as a stand-alone capability.  It should not have interactions with other parts of the system.

Performance Impact
------------------

None.

Other deployer impact
---------------------

The community version of TCUP does NOT have to be coupled to other test running models.  

It is _not_ desirable to complicate TCUP to serve other uses.

Developer impact
----------------

None.  TCUP should use the standard API.

Implementation
==============

Assignee(s)
-----------

Primary assignee:
  robhirschfeld

Other contributors:
  praveen (test)
  alexhirschfeld (dev & test)
  dlenwell (review)
  rockyg (documentation) * these documents are ripe with raw material for docs :)

Work Items
----------

* build TCUP docker container (via Dockerfile)
* build tcup.py to build and launch docker
* document run process
* update configuration generator to use environment variables
* integrate run_test scripts into TCUP
* integrate upload target into TCUP

Dependencies
============

* run_test scripts must support environment variables
* upload API must function correctly

Testing
=======

Manual environment testing by Refstack and community.

Documentation Impact
====================

TCUP needs detailed community facing documentation and video tours.

References
==========

* http://docker.io