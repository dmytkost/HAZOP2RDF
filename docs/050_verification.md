\newpage

# Verification

The verification process aims to check the code with the intent of finding failures. To make the program perform well, it should not contain critical errors and bugs. We designed a test pattern to verify the results of the program execution. This pattern is simple and extendable and covers the main parts of the program.

In the tests' directory of the project a list of the following files can be found:

-   `test_cli.py` - test Command Line Interface initialisation
-   `test_cmd_importer.py` - test Importer interface
-   `test_cmd_exporter.py` - test Exporter interface

The prime objective of the pattern is consistency. It allows us to apply this pattern to every test we want to implement.

The pattern covers the following test cases:

-   execution errors
-   execution exceptions
-   output verification

The code coverage value varies around 94%. The value depends on the state of the Fuseki server. It increases if the Fuseki server is running and there is pre-uploaded data on the server.

The coverage report below shows the detailed information about the tests results.

```{.shell caption="Coverage report"}
---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
src/__init__.py                        0      0   100%
src/cli.py                            20      3    85%   34-35, 43
src/commands/__init__.py               0      0   100%
src/commands/cmd_exporter.py          50      6    88%   37, 43, 48-50, 65
src/commands/cmd_importer.py          66      2    97%   38, 80
src/excel_config/__init__.py           0      0   100%
src/excel_config/excel_config.py       3      0   100%
src/services/__init__.py               0      0   100%
src/services/svc_exporter.py          28      0   100%
src/services/svc_importer.py          66      0   100%
src/services/svc_triplestore.py       16      3    81%   37-40
----------------------------------------------------------------
TOTAL                                249     14    94%
```

The user can also generate a coverage report in HTML and easily discover the missing statements. See [Appendix](#appendix) section for HTML coverage report example.
