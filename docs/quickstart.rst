**********
Quickstart
**********

Installing from PyPi: ``pip install libcobblersignatures``

Running the CLI when installed: ``cobbler-manage-signatures``

What is this library for?
#########################

The purpose of this library is to manage and abstract the access on how we manage the data for our operating system
detection. Currently this is a JSON file which is saved to the hard drive.

To understand what this library does we need to go into detail about what Cobbler does with the provided data. Cobbler
has a functionality called ``import``, which means that you give the CLI or API an ISO image which then gets searched
through to save information about it in Cobbler. This means that Cobbler somehow needs to detect which operating
system and which version of it is inside the ISO image. This library provides the data to distinguish between these ISOs
from each other.

How to use it?
##############

In the CLI Section you can see the most basic usage of this library. To get the most of it, it's not recommended to
install this library directly but rather use it together with Cobbler who has a dependency on it. If you just want to
manipulate the ``signatures.json`` file, it's recommended to use a built package from your package manager (if
available).
