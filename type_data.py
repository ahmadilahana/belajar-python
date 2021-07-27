#integer
data_integer = 11
print(type(data_integer))
print(data_integer, "type:", type(data_integer))

#float
data_float = 1.2
print(type(data_float))
print(data_float, "type:", type(data_float))

#string
data_string = "hello world"
print(type(data_string))
print(data_string, "type:", type(data_string))

#boolean
data_boolean = True
print(type(data_boolean))
print(data_boolean, "type:", type(data_boolean))

#complex
data_complex = complex(5,6)
print(type(data_complex))
print(data_complex, "type:", type(data_complex))

#type data from bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print(type(data_c_double))
print(data_c_double, "type:", type(data_c_double))