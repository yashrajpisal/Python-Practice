


Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 256
>>> y = 256
>>> print(id(x))
140730657387400
>>> print(id(y))
140730657387400
>>> x = 257
>>> y = 257
>>> print(id(x))
1299876654608
>>> print(id(y))
1299876652336
>>>

