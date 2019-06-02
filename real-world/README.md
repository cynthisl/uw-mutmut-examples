## Real world Python projects

This directory contains a script for installing uw-mutmut and several real-world Python
projects, on which the modified mutmut can be run to observe the number of killed and
surviviving mutations in each project.

Usage:

The setup.sh script clones Github repos for uw-mutmut and each of the real-world
projects to be tested, creates a Python3 virtualenv in the current directory, 
and installs testing prerequisites and the local copy of the uw-mutmut project
branch into the virtualenv.

Once setup.sh is run one time, you may try out mutmut on the sample projects with
any of the following command sequences:

```
$ source ve/bin/activate

# Then any of the following:
$ cd mistune
# Estimated runtime about 25 minutes
$ mutmut run --paths-to-mutate=mistune.py

# or

$ cd schema
# Estimated runtime about 10 minutes
$ mutmut run --paths-to-mutate=schema.py

# or

$ cd python-sortedcontainers
# Estimated runtime about 6 hours
$ mutmut run --paths-to-mutate=sortedcontainers
```

setup.sh has a couple of command options to:

* reinstall mutmut in the virtualenv after making local changes
* uninstall the virtualenv and the local git repos.

