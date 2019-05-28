# uw-mutmut-examples

This repository contains example code for the [UW fork of mutmut](https://github.com/kc7zep/uw-mutmut) for CSEP 590: Modern Testing and Debugging Spring 2019. 

## Installation

This depends on uw-mutmut:

```
git clone git@github.com:kc7zep/uw-mutmut.git
cd uw-mutmut
python setup.py install
```

## Running the examples

```
cd loop
mutmut run
```

### Exception handling examples

#### Raise -> pass

```
pip install pytest  # one time
cd exceptions/raise
mutmut run
mutmut show 7
```

#### Raise -> pass code and test fixed

```
cd exceptions/raise-fixed
mutmut run
mutmut show
```

#### Mutate exception catch, else, finally blocks

```
cd exceptions/tryblock
mutmut run
# except block -> pass
mutmut show 16 # or 18
# except block -> raise 
mutmut show 17 # or 19
# else block -> pass
mutmut show 20
# finally block -> pass
mutmut show 21
```

