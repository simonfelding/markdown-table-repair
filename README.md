# markdown-table-repair
Markdown tables are pretty fragile. This script can add the formalities to make a | seperated markdown table work.

Top row dictates size of table.


## example
This is a markdown table that is fine:

```
| #Table 1. Characteristics of the sample |     |      |            |            |
|-----------------------------------------|-----|------|------------|------------|
| Characteristic                          | n   | %    | weighted n | weighted % |
| Respondents                             | 123 | n/a  | 1.234.567  | n/a        |
```

this one is broken (extra whitespace in Characteristics cell):

```
| #Table 1. Characteristics of the sample |     |      |            |            |
|-----------------------------------------|-----|------|------------|------------|
| Characteristic                             | n   | %    | weighted n | weighted % |
| Respondents                             | 123 | n/a  | 1.234.567  | n/a        |
```


The script detects and removes the whitespace, outputting a markdown table suitable for sensitive stuff like https://github.com/Zettlr/Zettlr
