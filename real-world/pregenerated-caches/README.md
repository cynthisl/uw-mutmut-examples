## Pregenerated mutmut cache files

This directory contains mutmut cache files from 'mutmut run' invocations on
the real world source code projects in the parent directory.  These caches
are provided as a time-saving for people interested in seeing the actual
mutation analysis results.

There are two ways to use these files:

1. For any of the projects, copy `<projectname>.mutmut-cache` to `../<projectname>/.mutmut-cache`.  Then, you can run `mutmut show` or  `mutmut apply` within the project as though you had
just run `mutmut run`, but without the time overhead of actually running the tests over
the mutations.

1. Open the cache file with a sqlite viewer such as https://inloop.github.io/sqlite-viewer/.
The `Mutant` table records the results of running the project test suite against each
mutation.
