KEY
r = regularization constant
e = epochs
i = initialization 
o = ordering
a = alpha
b = beta
s = step cost

1. r = 1, e = 50, i = random, bias = random, o = random, a = 1, b = 1, s = a / (b + e)
    accuracy = 25.1000%
2. r = .01, e = 50, i = random, bias = random,  o = random, a = 1, b = 1, s = a / (b + e)
    accuracy = 75.6000%
3. r = .01, e = 50, i = random, bias = random,  o = random, a = 1000, b = 1000, s = a / (b + e)
    accuracy = 34.9000%
4. r = .001, e = 50, i = random, bias = random, o = random, a = 1, b = 1, s = a / (b + e)
    accuracy = 76.7000%
5. r = .001, e = 50, i = zeros, bias = random, o = random, a = 1, b = 1, s = a / (b + e)
    accuracy = 79.6000%, 78.9
6. r = .001, e = 75, i = zeros, bias = random, o = random, a = 1, b = 1, s = a / (b + e)
    accuracy = 76.8000%
7. r = .001, e = 50, i = zeros, bias = 0,  o = random, a = 1, b = 1, s = a / (b + e)
    accuracy = 78.3000%
8. r = .001, e = 50, i = zeros, bias = 0,  o = random, a = 1, b = 1, s = a / (b + e), NO GRAY VALUES
    accuracy = 82.0000%


