# 0x05. Python - Exceptions
- Errors and Exceptions
0. Safe list printing:
   a function that prints x elements of a list.
1. Safe printing of an integers list:
   a function that prints an integer with "{:d}".format().
2. Print and count integers:
   a function that prints the first x elements of a list and only integers.
3. Integers division with debug:
   a function that divides 2 integers and prints the result.
4. Divide a list:
   a function that divides element by element 2 lists.
5. Raise exception:
    a function that raises a type exception.
6. Raise a message:
   a function that raises a name exception with a message.
7. Safe integer print with error message:
   a function that prints an integer.
8. Safe function
   a function that executes a function safely.- 101-safe_function.py
9. ByteCode -> Python #4:
   The Python function def magic_calculation(a, b): that does exactly the same
   as the following Python bytecode:
      	  3           0 LOAD_CONST               1 (0)
              	      3 STORE_FAST               2 (result)

  	  4           6 SETUP_LOOP              94 (to 103)
             	      9 LOAD_GLOBAL              0 (range)
             	      12 LOAD_CONST               2 (1)
             	      15 LOAD_CONST               3 (3)
             	      18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             	      21 GET_ITER
       		  >>  22 FOR_ITER                77 (to 102)
             	  25 STORE_FAST               3 (i)

	5          28 SETUP_EXCEPT            49 (to 80)

  	  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

 	 7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE