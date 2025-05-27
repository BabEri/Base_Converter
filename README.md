A simple python code that converts numbers from a base to another. The programme can convert from base 2 to base 35. The numbers to be converted can be the normal integers from 0-9 (up to base 10) and includes alpha-numeric numbers 0-9, A_Z (for bases 11 to 35). The code is a class called Convert_Base which takes instances with 3 attributes; num: which is the number to be converted, sub: the base in which the number is to be converted from, and main: the desired base, the number is to be converted, the main has a default of 10. so for instance, if one desires to convert 14325 from base 6 to base 7 an instance will be created thus:
x = Convert_Base(14325, 6, 7)
print (x.solve())
the solve method gives the desired result, the repr method also gives the result but it is desirable to use the solve method first.
The Convert_Base class has 2 other methods, to_ten() and from_ten() which makes the code functional. The to_ten method converts, the instance to decimal, irrespective of the value of the attribute 'main'. it can be used thus (continue from the x instance above):
print(x.to_ten())
the from_ten method converts any decimal number to the desired base, using an attribute 'decimal_value/d_v', so if a user using the above x instance still desires to convert any decimal number to base 7, the user simply needs to use the from_ten method, i.e., should the user desire to cinvert 52382917 to base 7, the following should be computed:
print(x.from_ten(52382917)).
Please remember that the number to be converted can be integers (where the 'sub' is less than base 11) or string (compulsory if the base is more than base 10 *and* it contains an alphabet, e.g x = Convert_Base('1ABD6', 18, 3) to convert 1ABD6 from base 18 to base 3).
The code was written to minimize memory usage as little as possible. for further inquiries, you can contact me at fapetuseun@gmail.com
