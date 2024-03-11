a = [1,2,3,4,5]
print(id(a))

from ctypes import c_int, addressof
a = 44

print(addressof(c_int(a)))

from ctypes import c_void_p, addressof
a = 44
print(addressof(c_void_p(a)))
