# Python's `for` and `while` loops support an `else` clause that executes only if the loops terminates without hitting a `break` statement.

def contains (hay,needle):
    for item in hay:
        if item == needle:
            break
    else:
        raise ValueError("needle not found")
print(contains([23,"needle", 0xbadc0ffee], 'needle'))
