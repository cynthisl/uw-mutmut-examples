# uw-mutmut-examples

This repository contains example code and project deliverables for the [UW fork of mutmut](https://github.com/kc7zep/uw-mutmut) for CSEP 590: Modern Testing and Debugging Spring 2019. 

## Credits
This project is a collaboration of:

* cynthisl@cs.washington.edu
* hgotur@cs.washington.edu
* nsds@cs.washington.edu

Our project is a set of small improvements to the Python mutation testing tool https://github.com/boxed/mutmut.  We owe a huge debt to mutmut's author for writing this tool and making it available on Github.  We intend to work with the author to give our changes back to the main mutmut project.

## Roadmap
* [This document](README.md) is the main project presentation given in class.
* https://github.com/kc7zep/uw-mutmut/tree/project is a hard fork of mutmut with a branch containing our improvements.
* Subdirectories [loop](loop/), [slice](slice/), and [exceptions](exceptions/) contain toy programs showing how each of the new mutations work.
* Subdirectory [real-world](real-world/) contains a script for running mutmut against three real-world Python projects.
* [evaluation.md](evaluation.md) analyzes the impact of our changes to mutmut on the projects in real-world.

## What is this?

We have made improvements to mutmut, an existing open source Python mutation framework. This will allow us to identify gaps in existing test coverage for Python-based programs and improve the health of our code.   We hope that the improvements we have made will be useful to both the mutmut developers and mutmut users.

The mutation code is located at [uw-mutmut](https://github.com/kc7zep/uw-mutmut) repository, which also contains user-facing documentation. This repository contains example code specific to our improvements and class-specific documentation.

## How did we pick this?

Mutmut was chosen because it looks easy to read, had a small existing codebase, and we could easily identify areas of improvement. Other Python frameworks considered were mutpy and cosmic_ray.

## What did we make better?

We considered improvements such as making the UI better and making the tool run faster, but we settled on two key functionality improvements:
* Adding more mutators to increase coverage
* Adding additional mutation functionality to help boost the feature set of mutmut

### New mutators

We primarily chose new mutators to add by looking at other mutation frameworks (PIT, mutpy, cosmic_ray, major, mujava) and picking a set of mutators that were prevalent and seemed likely to be useful. The list of new  mutators we added were:

* [Exceptions](exceptions/README.md)
  * Exception raise to pass
  * Try-except handler blocks to both pass and re-raise caught exceptions
  * Try-else and try-finally blocks to pass
* [Loops](loop/README.md)
  * For loops - run 0 and 1 times
  * While loops - run 0 and 1 times
  * List comprehension for loops - run 1 time
* [Slices](slice/README.md)
  * Add start/end to the operand if element is empty
  * Remove start/end sides of the operand
  * Different combinations of the above for both sides

### Other infrastructure improvements

Beyond adding more mutators, we also added a few functionality improvements to mutmut. One of the improvements was necessary to support the mutations we added, but it also helps extend mutmut to the posibility of more types of mutations. The other helps lay the groundwork for better analysis of the results of a mutation run, both for developers of mutmut and end users who are using mutmut on their own code. The infrastructure improvements we added were:

* Multiple mutations per operator 
  * This improvement was needed because our new mutators take the same node and mutate it multiple ways, but base mutmut could only make one mutation per node. 
  * To use, pass back the all mutations as values in a dict; they will be parsed out on checking the return type.
    * Ideally, the return type would be a custom class for mutations, but refactoring the existing mutations to use it is outside the scope of this class.
    * This couldn't be a list because type list is already in use.
* Tag mutations with mutation category names 
  * This makes it easier for a mutmut user to understand which kinds of mutations are productive for a particular code base and test suite.
  * To use, return the mutation as a tuple with `pack_mutator_tuple(mutation, name)`.

## Testing Infrastructure

There are two levels of testing we used to test mutmut. The first is the test suite in the mutmut repository. The architecture of the suite is that each file has a corresponding test file plus one additional test file specifically to test mutations. Inside each test file, test functions isolate individual functions in the corresponding module, run them, and assert that the output matches the expected output and any other post-conditions are met. These tests are essentially unit tests where each function is a "unit". Mutmut uses [pytest](https://docs.pytest.org/en/latest/) as its testing framework and  [tox](https://tox.readthedocs.io/en/latest/) to automate the process of setting up the environment and running the tests. As we added new mutators, we added tests for these mutators to the suite of unit tests and ran tox to validate the expected behavior and also give us confidence that we didn't regress other code. We also added tests for new functionality, like support for multiple mutations.

The second level of testing is this repository. We created several sample programs and tests that would allow us to test our mutators end-to-end. The sample programs each contain code that exercise the new mutators that we added. This allowed us to see the resulting output of mutmut and validate that our mutators not only mutated the code correctly, but also that the reporting of the number of mutations killed/survived was correct after our changes and that users would be able to show new mutations and properly see diffs.

## What were the hard parts?

We quickly discovered that some of the improvements we wanted to make would require larger changes to the architecture of mutmut, which is outside the scope of this class. For example, base mutmut only supports one mutation per operation, and we wanted to mutate the same operator multiple ways. Another quirk was that mutmut uses parso instead of the standard Python AST to parse the language, which was an additional layer of abstraction to learn. mutmut also produces unproductive mutants, such as `XX__main__XX` and `[x for x not in y]`, which will never fail and added noise during development.

Compared to other Python mutation tools, such as mutpy, mutmut's internal design is not sophisticated and lacks comments, so it was difficult to understand how mutmut worked without spending time in the debugger stepping through code.


## Installation

This depends on uw-mutmut:

```
git clone git@github.com:kc7zep/uw-mutmut.git
cd uw-mutmut
python setup.py install
```

## How to run

[User workflow](https://github.com/kc7zep/uw-mutmut/tree/project#workflow) is documented in the uw-mutmut readme. The process of generating the mutants is the same, our improvements just added more muants.

## Running the examples

Our examples depend on pytest

```
pip install pytest
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

