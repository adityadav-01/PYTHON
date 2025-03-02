x=10
y=8
print(bin(x),bin(y))
print(x&y)
print(x&y ,bin(x&y))

#  binary value x = 10  =  0b1010   ; 
#               y = 8   =  0b1000

# and =  &  x=10=1010 or y=8=1000 ko truth table se compare krne pr =1000 yani 8
# or  =  |  x=10=1010 or y=8=1000 ko truth table se compare krne pr =1010 yani 10
# xor =  ^  x=10=1010 or y=8=1000 ko truth table se compare krne pr =0010 = 10  yani 2

print(bin(x&y),x&y)
print(bin(x|y),x|y)
print(bin(x^y),x^y)