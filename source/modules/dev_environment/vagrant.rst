.. _vagrant-notes:

********************************
Setting up Python via a Linux VM
********************************

One of the challenges we face as developers on a team, or as students in a classroom, is getting everyone quickly up and running with a full fledged, feature rich, functional, consistent, and homogeneous Python development environment.

Python is robust platform-independent programming language, and a full fledged development environment can be set up on any platform. However, there are still system differences, particularly between Windows and the \*nix family of Operating Systems.

Also -- particularly if you are working on a web service of some sort, the odds are good that it will be deployed on a Linux system. In this case, developing on Linux makes things easier.

So if you want an already setup environment in which to do your python programming that matches the environment used by the instructors and other students well (and many professional python developers too), a virtual machine running Linux can provide you that environment, regardless of the host operating system.

We recommend `VirtualBox <https://www.virtualbox.org/>`_ for providing the VM, and `Vagrant <https://www.vagrantup.com/>`_ for deploying a pre-configured system.

VirtualBox and Vagrant allow us to quickly build a virtual machine with everything we'll need.

Complete instructions and installation resources can be found here:

https://github.com/rriehle/uwpce-vagrant
