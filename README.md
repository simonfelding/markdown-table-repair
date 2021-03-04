# markdown-table-repair
Markdown tables are pretty fragile. This script can add the formalities to make a | seperated markdown table work.

Top row dictates size of table.


## example
this table is broken: 1. extra whitespace in Characteristics cell, 2. too few dashes in second row, 3. Respondents row has 4 cells instead of five:

```
| #Table 1. Characteristics of the sample |     |      |            |            |
|-------------------------------------|-----|------|------------|------------|
| Characteristic                             | n   | %    | weighted n | weighted % |
| Respondents                             | 123 | n/a  | 1.234.567  |
```

The script detects and removes the errors, outputting a markdown table suitable for sensitive stuff like https://github.com/Zettlr/Zettlr

```
| #Table 1. Characteristics of the sample |     |      |            |            |
|-----------------------------------------|-----|------|------------|------------|
| Characteristic                          | n   | %    | weighted n | weighted % |
| Respondents                             | 123 | n/a  | 1.234.567  | n/a        |
```

