# Data types list       mutable object can change its state or contents and immutable objects cannot.
#    (A) MUTABLE DATA TYPES                   (B)  IMMUTABLE DATA TYPES 
#     1.  List [sequence type]                 1.  int ~ Integers(ex: a=10)  [numeric type]                4. str ~ String [sequence type]
#     2.  Dictionary                           2.  Float(ex: a=2.5)          [numeric type]                5. Tuple        [sequence type]
#     3.  Byte Array                           3.  Complex (ex: a1+2j)       [numeric type]                6. Set

#  1.LIST:-     List is an ordered sequence of items . It is one of the most used datatype in python and is very flexible.   [] ex ~ a=[1 , 2.2 , ws]
L=['rohan',1.5]
print(L,type(L))

#  2.DICTIONARY :- Dictionary is an unordered collection of key-value pairs. In python , dictionaries are defined within braces {} with each item being a pair in the form key:value. ex ~  d={1:'value','key':2}
d={'course_name':'python',
   'course_duration':'2 Month'}
print(d,type(d))

#  3.BYTE ARRAY :- A byte array is an array of bytes. It is defined within braces [] with each item being a byte. ex ~ b=[1,2,3]
b=[1,2,3]
print(b,type(b))

#     1.INTEGERS
a=5
print(a,type(a))

#     2.FLOAT
a=5.5
print(a,type(a))

#    3.COMPLEX
a=2+5j
print(a,type(a))

#    4.STRING:-   A strring is a collection of one or more characters put in a single quote , double quote or triple quote . 
s= 'hello@123'
print(s,type(s))

#    5.TUPLE :- Tuple is an ordered sequence of items same as a list. It is defined within parentheses() where items are separated by commas.  ex ~ t=(5,'program', 1+3j)
t=(10,28,'rohan')
print(t,type(t))

#    6.SET :- A Set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).{}   ex ~ my_set={1,2,3}
s={10,20,30,20}
print(s,type(s))