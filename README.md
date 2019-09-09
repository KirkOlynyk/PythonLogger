# PythonLogger
Log python scripts using decorators

## Example

```
  from logger import Logger
  
  @trace('i')
  def f(i):
    return i
    
  f(3)
```
