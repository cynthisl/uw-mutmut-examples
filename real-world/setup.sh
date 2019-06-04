#!/bin/bash
# Set up real world code sample projects so that
# anyone can run mutmut on them and hopefully get reproducible 
# results.
#
if [[ "$1" == "reinstall-mutmut" ]]; then
    if [[ -e ve/bin/activate ]]; then
        source ve/bin/activate
        pushd uw-mutmut
        python setup.py install
        popd
        deactivate
    else 
        echo "No virtualenv set up; mutmut not reinstalled"
    fi
    exit
fi

if [[ "$1" == "uninstall" ]]; then
    rm -rf schema mistune python-sortedcontainers
    rm -rf uw-mutmut 
    rm -rf ve
    exit
fi

if [[ "$1" == "checkout-tested-versions" ]]; then
    pushd mistune
    git checkout 449c2b529
    popd
    pushd schema
    git checkout 38321194c
    popd
    pushd python-sortedcontainers
    git checkout d127cdde
    popd
    exit
fi

if [[ "$1" != "" ]]; then
    cat <<EOF
Usage: $0 [help|reinstall-mutmut|uninstall|checkout-tested-versions]

$0: set up local system for running mutmut on real world code examples
- Clones uw-mutmut and several real world Python projects.
- Creates a virtualenv into which test prerequisites and the uw-mutmut
clone are installed.

$0 help: this help

$0 reinstall-mutmut: refreshes the existing virtualenv with any changes you
have made to the local uw-mutmut repo.

$0 uninstall: removes the virtualenv, uw-mutmut, and examples.

$0 checkout-tested-versions: checks out the version(s) of the sample repos
which were analyzed for this class.

EOF
    exit
fi

# Default setup path
# Get uw-mutmut
git clone https://github.com/kc7zep/uw-mutmut
pushd uw-mutmut
git checkout project
popd

# Get the example projects
git clone https://github.com/keleshev/schema
git clone https://github.com/lepture/mistune
git clone https://github.com/grantjenks/python-sortedcontainers

# Set up one common virtualenv for all test examples
# as there seems no compelling need for isolated venvs
#
virtualenv -p python3 ve
source ve/bin/activate
pip install pytest mock
pushd uw-mutmut
python setup.py install
popd
deactivate
