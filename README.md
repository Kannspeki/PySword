## PySword
### A simple Python Password Generator  

### Usage

```usage: pysword.py [-h] [-n] [-a] [-s] length```

positional arguments:  
  length        The length of the Password  

options:  
  -h, --help    show this help message and exit  
  -n, --number  Generate only Numbers  
  -a, --alpha   Generate only alphabetical characters  
  -s, --symbol  Generate only symbols  

### Examples
* A password with 5 characters made of numbers:
```pysword.py 5 -n```  
```48139```
* 5 characters made of numbers and symbols:
```pysword.py 5 -ns```   
```8#"<4``` 
* And to combine all three
```pysword.py 10 -nsa```  
```Z3U|T```



