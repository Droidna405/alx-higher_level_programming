#!/usr/bin/python
numbers = ", ".join("{:02d}".format(number) for number in range(100))
print(numbers)
