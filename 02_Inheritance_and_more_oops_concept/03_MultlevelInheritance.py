class A:
    a = 1

class B(A):
    b = 2

class C(B):
    c = 3
    
d = A()

print(A.a) #prints the a attribnute
#print(A.b) #Shows an errror beccausa employee does nt have b attribute

e = B() 
print(e.a , e.b)

f = C()
print(f.a, f.b, f.c)