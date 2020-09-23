# TextToCString.py
This script converts any text into a 'C string literal'.  This string can be assigned to
any 'C code variable'.

Requires the input text to be in a file.  The default file looked for is 'input.txt'

For example:
[input]
```text
5 + 6 = %d
name = %s
List:\t"Mountain",\t"Sky"



```
[console]
```bash
python TextToCString.py
```

[output]
```C
"5 + 6 = %d\n"
"name = %s\n"
"List:\t\"Mountain\",\t\"Sky\"\n"
"\n"
"\n"
```

If you want all the text in a single literal just add the '-s' flag.
For more details on available flags, and thus more features, call `python TextToCString.py -h`.

[output: '-s']
```C
"5 + 6 = %d\nname = %s\nList:\t\"Mountain\",\t\"Sky\"\n\n\n"
```

