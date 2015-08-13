# Factorials

### The Task
Write a function that returns the solution to N-factorial. 

### Definition
A factorial is defined as the product of a positive integer `x` and positive integers less than `x`. 

- `x-factorial` is written `x!` 
- `0! = 1` by definition.

### Examples
5! =  5* 4 * 3 * 2 * 1
10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
1! = 1
0! = 1

### Once you've solved it, here are some extra challenges:
- Use recursive function calls
- Don't use any recursive calls
- find out how to `import` Python's `math` library and check your `my_factorial()` function with:
```python
for i in range(10):
    assert math.factorial(i) == my_factorial(i)
```
