# Custom *M* language compiler

## Usage
```bash
$ pipenv install
$ pipenv run cli
```

## *M* language examples

### Constants
```python
b1 = true;            # boolean
b2 = false;           # boolean
i1 = 10;              # integer
f1 = 60.5;            # float
f2 = 60.;             # float
f3 = .5;              # float
f4 = 60.52E2;         # float
f4 = 60.52E-2;        # float
s1 = "Hello world";   # string
```

### Matrix initialization
```python
# 'zeros' and 'ones' accepts any number of arguments
A = zeros(5);         # create vector of size 5 filled with zeros
B = ones(7, 4);       # create 7x4 matrix filled with ones
C = zeros(1, 2, 3);   # create 1x2x3 matrix filled with zeros

# eye accepts exactly two arguments
D = eye(10, 8);      # create 10x8 matrix filled with ones on diagonal and zeros elsewhere

E = [1, 2, 3, 4]      # vector of size 4
F = [[1, 2, 3],       # matrix of size 2x3
     [4, 5, 6]]
```

### Scalars operations
```python
r = a + b             # addition
r = a - b             # subtraction
r = a * b             # multiplication
r = a / b             # division

r = -a                # negation

r += a                # assignment with addition
r -= a                # assignment with subtraction
r *= a                # assignment with multiplication
r /= a                # assignment with division

r = a > b             # comparison: greater
r = a < b             # comparison: lesser
r = a >= b            # comparison: greater or equal
r = a <= b            # comparison: lesser or equal
```

### Matrix operations
```python
R = A .+ B            # element wise addition
R = A .- B            # element wise subtraction
R = A .* B            # element wise multiplication
R = A ./ B            # element wise division
R = A'                # matrix transpositon

A[1,2] = B[3,4]       # metrix selectors
```

### Comparators
```python
r = A == B            # equality comparator
r = a == b       
       
r = A != B            # not equality comparator
r = a != b
```

### IF statement
```python
if (a > b)
    print "Yes";

if (a > b) {
    print "Yes";
}

if (a > b)
    print "Yes";
else
    print "No";

if (a > b) {
    print "Yes";
} else {
    print "No";
}
```

### Loops
```python
# while loops
while (a > b)
    b += 1;

while (a > b) {
    b += 1;
}

# for (range) loops
for i = 1:5
    print i;

for i = 1:5 {
    print i;
}

# break and continue keywords
while(a > b) {
    if (a > 10)
        break;
    if (a > 5)
        continue;
    a += 1;
}
```

### Built-in instructions
```python
print a, b, c;       # prints to stdout, acepts any amount of arguments 
return a;            # terminates program with given value as result
```
