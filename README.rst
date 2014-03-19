RefStack/TCUP and Driver Test
=============================

This project support collection and publication of Community Test results for OpenStack.  There are multiple components of this effort:

* RefStack: Community-facing API for registration of interop-compliance endpoints and credentials for on-demand testing.
* TCUP: Portable, Containerized Tempest for Community running and reporting results to RefStack
* Driver Test

Participate
-----------------------------------------

* Mailing List: fits@openstack.org
* IRC: #refstack on Freenode
* Dev Meetings: https://wiki.openstack.org/wiki/Meetings#DefCore_.2F_RefStack_Development_Meeting


Test your Cloud and Share! > Running TCUP
-----------------------------------------

TCUP (Tempest in a Container to Upload from Probe) is a portable way for community members to quickly and consistently run Tempest against private and public clouds.

[[doc/tcup.md]]

Collecting the Results > Running RefStack 
-----------------------------------------

RefStack is a Web UI and API used to collect test results from TCUP and display results.  This information is used by the DefCore committee to help select must-pass capabilities.

[[doc/refstack.md]]

