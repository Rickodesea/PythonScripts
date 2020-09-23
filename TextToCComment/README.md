# TextToCComment.py
This converts a text into a C comment.

Requires the input text to be in a file.  The default file looked for is 'input.txt'.

[input]
```text
Let's convert this text into a C comment.
We can use line comment as well as block comment.
We can even center the text.
```

[console]
```bash
python TextToCComment.py
```

[output]
```C
//Let's convert this text into a C comment.        
//We can use line comment as well as block comment.
//We can even center the text.   
```

If you want a fancy commenting style then pass the 'line-fancy' value to the '-t' flag.
For more details on available flags, and thus more features, call `python TextToCComment.py -h`.

[output: '-t=line-fancy']
```C
/////////////////////////////////////////////////////////
//  Let's convert this text into a C comment.          //
//  We can use line comment as well as block comment.  //
//  We can even center the text.                       //
/////////////////////////////////////////////////////////
```

