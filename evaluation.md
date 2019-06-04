


## Evaluation of mutmut modifications implemented for UW CSE590 Spring 2019


## Objective

We wanted to understand the impact of the new mutations we implemented in the mutmut mutation testing tool.  To do this, we chose several publically available Python libraries which had test suites, and analyzed them with the new mutmut.  We counted the number of new mutations generated, and how many survived and how many were killed.  We also analyzed a few of the surviving mutations to determine whether they could lead to productive changes in the test code or the library code.


## Libraries analyzed


### Schema

https://github.com/keleshev/schema @ 38321194

This library validates Python data structures which have been read from common data file structured formats; for example: YAML; JSON. 

Running 'mutmut run' on this library took about 12 minutes on attu.cs.washington.edu, and 7 minutes on a Macbook Pro (3.3GHz i7).


### Mistune

https://github.com/lepture/mistune @ 449c2b52

This library is a pure Python implementation of a Markdown parser.

Running mutmut run on this library took 25 minutes on attu.cs.washington.edu, and 13 minutes on the MBP.


### Sortedcontainers

https://github.com/grantjenks/python-sortedcontainers.git @ d127cdde

This library is a pure Python implementation of several kinds of sorted container, including: dictionaries, lists, and sets.  DIctionaries are sorted by key, while lists and sets are sorted by value.  This library was chosen as a test case because it seemed well documented and well supported, and claimed 100% test coverage in its documentation.

Running 'mutmut run' on this library took ~5 hours on attu.cs.washington.edu, and 2.5 hours on the MBP. 


## Data Analysis Methodology

For each library, mutmut run was executed.  The resulting .mutmut-cache file was read into a web-client-based database viewer, [https://inloop.github.io/sqlite-viewer/](https://inloop.github.io/sqlite-viewer/), and the SQL query:


```
select status, mutation_name, count(id) count from Mutant group by status, mutation_name
```


was run.  The resulting table was copied into Google Sheets, and a pivot table was created, showing aggregate counts for each mutation type by test run status.  


## Results


### Quantitative Summary


<table>
  <tr>
   <td>Name
   </td>
   <td>Mutant type
   </td>
   <td>Survived
   </td>
   <td>Timed Out
   </td>
   <td>Killed
   </td>
   <td>Suspicious
   </td>
   <td>Total generated
   </td>
   <td>% Survived
   </td>
  </tr>
  <tr>
   <td>schema
   </td>
   <td>Pre-existing
   </td>
   <td>64
   </td>
   <td>0
   </td>
   <td>311
   </td>
   <td>7
   </td>
   <td>382
   </td>
   <td>16.75%
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>New
   </td>
   <td>12
   </td>
   <td>0
   </td>
   <td>71
   </td>
   <td>2
   </td>
   <td>85
   </td>
   <td>14.12%
   </td>
  </tr>
  <tr>
   <td>mistune
   </td>
   <td>Pre-existing
   </td>
   <td>493
   </td>
   <td>1
   </td>
   <td>472
   </td>
   <td>0
   </td>
   <td>966
   </td>
   <td>51.04%
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>New
   </td>
   <td>41
   </td>
   <td>2
   </td>
   <td>21
   </td>
   <td>0
   </td>
   <td>64
   </td>
   <td>64.06%
   </td>
  </tr>
  <tr>
   <td>sortedcontainers
   </td>
   <td>Pre-existing
   </td>
   <td>239
   </td>
   <td>13
   </td>
   <td>1094
   </td>
   <td>0
   </td>
   <td>1346
   </td>
   <td>17.76%
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>New
   </td>
   <td>63
   </td>
   <td>3
   </td>
   <td>96
   </td>
   <td>0
   </td>
   <td>162
   </td>
   <td>38.89%
   </td>
  </tr>
</table>



### Newly added mutations for schema:


<table>
  <tr>
   <td><em>SUM of count</em>
   </td>
   <td><em>status</em>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><em>mutation_name</em>
   </td>
   <td>bad_survived
   </td>
   <td>ok_killed
   </td>
   <td>ok_suspicious
   </td>
   <td>Grand Total
   </td>
   <td>% Survived
   </td>
  </tr>
  <tr>
   <td>comp_for
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
14</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
15</p>

   </td>
   <td><p style="text-align: right">
6.67%</p>

   </td>
  </tr>
  <tr>
   <td>else-pass
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
33.33%</p>

   </td>
  </tr>
  <tr>
   <td>except-pass
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
9</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
30.77%</p>

   </td>
  </tr>
  <tr>
   <td>except-raise
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
10</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
15.38%</p>

   </td>
  </tr>
  <tr>
   <td>for_stmt_zero_loop
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
10</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
10</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>loop_one_iteration
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
10</p>

   </td>
   <td><p style="text-align: right">
10%</p>

   </td>
  </tr>
  <tr>
   <td>raise_stmt
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
18</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
22</p>

   </td>
   <td><p style="text-align: right">
18.18%</p>

   </td>
  </tr>
  <tr>
   <td><strong>Grand Total</strong>
   </td>
   <td><p style="text-align: right">
<strong>13</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>71</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>2</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>86</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>15.12%</strong></p>

   </td>
  </tr>
</table>



### Newly added mutations for mistune:


<table>
  <tr>
   <td><em>SUM of count</em>
   </td>
   <td><em>status</em>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><em>mutation_name</em>
   </td>
   <td>bad_survived
   </td>
   <td>bad_timeout
   </td>
   <td>ok_killed
   </td>
   <td>Grand Total
   </td>
   <td>% Survived
   </td>
  </tr>
  <tr>
   <td>for_stmt_zero_loop
   </td>
   <td><p style="text-align: right">
10</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
14</p>

   </td>
   <td><p style="text-align: right">
71.43%</p>

   </td>
  </tr>
  <tr>
   <td>loop_one_iteration
   </td>
   <td><p style="text-align: right">
18</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
24</p>

   </td>
   <td><p style="text-align: right">
75%</p>

   </td>
  </tr>
  <tr>
   <td>raise_stmt
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
100%</p>

   </td>
  </tr>
  <tr>
   <td>while_stmt_zero_loop
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
10</p>

   </td>
   <td><p style="text-align: right">
40%</p>

   </td>
  </tr>
  <tr>
   <td>x[:b] => x[:]
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>x[:b] => x[1:b]
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>x[a:] => x[:]
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
100%</p>

   </td>
  </tr>
  <tr>
   <td>x[a:] => x[a:-1]
   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
50%</p>

   </td>
  </tr>
  <tr>
   <td><strong>Grand Total</strong>
   </td>
   <td><p style="text-align: right">
<strong>41</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>2</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>21</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>64</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>64.06%</strong></p>

   </td>
  </tr>
</table>



### Newly added mutations for sortedcontainers:


<table>
  <tr>
   <td><em>SUM of count</em>
   </td>
   <td><em>status</em>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><em>mutation_name</em>
   </td>
   <td>bad_survived
   </td>
   <td>bad_timeout
   </td>
   <td>ok_killed
   </td>
   <td>Grand Total
   </td>
   <td>% Survived
   </td>
  </tr>
  <tr>
   <td>comp_for
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
16</p>

   </td>
   <td><p style="text-align: right">
25%</p>

   </td>
  </tr>
  <tr>
   <td>except-pass
   </td>
   <td><p style="text-align: right">
5</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
83.33%</p>

   </td>
  </tr>
  <tr>
   <td>except-raise
   </td>
   <td><p style="text-align: right">
5</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
83.33%</p>

   </td>
  </tr>
  <tr>
   <td>finally-pass
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>for_stmt_zero_loop
   </td>
   <td><p style="text-align: right">
18</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
24</p>

   </td>
   <td><p style="text-align: right">
75%</p>

   </td>
  </tr>
  <tr>
   <td>loop_one_iteration
   </td>
   <td><p style="text-align: right">
20</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
16</p>

   </td>
   <td><p style="text-align: right">
36</p>

   </td>
   <td><p style="text-align: right">
55.56%</p>

   </td>
  </tr>
  <tr>
   <td>raise_stmt
   </td>
   <td><p style="text-align: right">
11</p>

   </td>
   <td>
   </td>
   <td><p style="text-align: right">
20</p>

   </td>
   <td><p style="text-align: right">
31</p>

   </td>
   <td><p style="text-align: right">
35.48%</p>

   </td>
  </tr>
  <tr>
   <td>while_stmt_zero_loop
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>x[:b] => x[:]
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>x[:b] => x[1:b]
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>x[a:] => x[:]
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
0%</p>

   </td>
  </tr>
  <tr>
   <td>x[a:] => x[a:-1]
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
       0%</p>

   </td>
  </tr>
  <tr>
   <td>x[a:b] => x[:]
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
25%</p>

   </td>
  </tr>
  <tr>
   <td>x[a:b] => x[:b]
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
25%</p>

   </td>
  </tr>
  <tr>
   <td>x[a:b] => x[a:]
   </td>
   <td>
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
25%</p>

   </td>
  </tr>
  <tr>
   <td><strong>Grand Total</strong>
   </td>
   <td><p style="text-align: right">
<strong>63</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>3</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>96</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>162</strong></p>

   </td>
   <td><p style="text-align: right">
<strong>40.74%</strong></p>

   </td>
  </tr>
</table>



## Discussion 

The value of the new mutations we added depends highly on the code being analyzed. In our examples, because the schema library deals with validating types, it does not perform any slicing in the code, which means we have no slice mutants for this library. 


### Exception Mutations

Analyzing the surviving exception mutations found several different causes for surviving mutants.  Some of the surviving mutants were productive; some not productive.  No particular kind of exception mutant was clearly in one or the other class.

For exception mutations, it was found that 'raise => pass' was the most productive mutation for the libraries tested; when raise mutations survived, they tended to result in productive test cases. 

The Pythonic idiom for using try/except to handle multiple Python version import libraries led to a class of unproductive except->pass and except->raise mutations, as discussed below.  However, the unproductivity is due to context; there were other cases where except->pass did lead to a productive mutation.


#### Productive mutants which could result in additional test cases:

schema:

* 144: (try-except => pass)
* 176 (try-else=> pass)

mistune:

* 256, 646 (raise => pass)

python-sortedcontainers:

* 132, 381, 518, 562, 592, 891, 905, 1059, 1079, 1096, 1407 (raise => pass)


#### Unproductive mutants

schema:

* 174: (try-except=> pass) In this case, 'return False' was replaced by pass, which resulted in an empty return, which in Python is the same as 'return None'.  To a caller, 'return None' and 'return False' are semantically equivalent in Boolean comparison.

* 220: (try-except => pass).  In this case, the original code was a block containing 'pass', while the mutation was a single statement 'pass'.  These are semantically equivalent, however mutmut's code to check for equivalent mutants treats block indents as significant, so did not detect these as equivalent.

A very common unproductive pattern was mutated Python import blocks; for example:


```
 try:
     from collections.abc import Sequence, MutableSequence
-except ImportError:
-    from collections import Sequence, MutableSequence
+except ImportError: pass
```


This is the standard idiom when writing code which needs to run under multiple versions of Python.  While not always found in small programs, it's often found in libraries which are expected to support both Python 2.x and Python 3.x -- which is pretty common given Python's revision history.

This mutation is unproductive because people rarely write unit tests for library import errors.  A large professionally-developed-and-maintained library might include such tests; I'd expect most small developers or hobbyists to not have these kinds of tests.   On the other hand, the Python tox library tool does make it easy to maintain separate test run environments per-Python version, so it's not impossible to add these tests -- just unlikely.

Mutations resulting from import blocks included:

* schema: 1, 2

* sortedcollections: 3, 4, 7, 8, 9, 10, 1217, 1218, 1346, 1347


### Loop Mutations

The majority of surviving loop mutations were productive as they showed areas where the tests weren’t exercising a loop with multiple elements. Killing them would be to construct a test case object with multiple items in the array, but how easy that is is highly dependent on the codebase; for example, some of the surviving mutations from mistune had nested loops, which may be tricker to make a case for.

Example of a productive mutant:

Schema: mutation 107


```
-        flags_list = [Regex.NAMES[i] for i, f in enumerate("{0:09b}".format(flags)) if f != "0"]  # Name for each bit
+        flags_list = [Regex.NAMES[i] for i, f in []]  # Name for each bit
```


 

This tells us that none of the existing test cases involve testing regex flags, and they should be added for more complete testing.

