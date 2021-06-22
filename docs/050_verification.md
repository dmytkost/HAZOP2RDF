# Verification

The important part of the project is verification. We designed a test pattern to verificate the results of the program execution. This pattern is simple and extendable and covers the main parts of the program.

In the tests' directory you can find a list of the following files:

* `test_cli.py` - test command line interface initialization
* `test_cmd_importer.py` - test importer interface
* `test_cmd_exporter.py` - test exporter interface

The prime objective of the pattern is consistency. It allows us to apply this pattern to every test we want to implement.

The pattern covers the following test cases:

* execution errors
* execution exceptions
* output verification

The code coverage value varies around 95±2%. The value depends on the state of the Fuseki server. It increases if the Fuseki server is running and there is pre-uploaded data on the server.

The coverage report below shows the detailed information about the tests results.

```
---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
src/__init__.py                       0      0   100%
src/cli.py                           20      3    85%   34-35, 43
src/commands/__init__.py              0      0   100%
src/commands/cmd_exporter.py         50      6    88%   37, 43, 48-50, 65
src/commands/cmd_importer.py         66      2    97%   38, 80
src/config/__init__.py                0      0   100%
src/config/config.py                  3      0   100%
src/services/__init__.py              0      0   100%
src/services/svc_exporter.py         28      0   100%
src/services/svc_importer.py         97      0   100%
src/services/svc_triplestore.py      16      3    81%   37-40
---------------------------------------------------------------
TOTAL                               280     14    95%
```

The user can although generate a coverage report in HTML format and easily discover the missing statements.

There are predefined commands in the Makefile for quick access.