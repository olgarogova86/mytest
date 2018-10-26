my_dict = dict()

my_dict["a"]="b"

key = "a"
val = "b"
if my_dict.get(key) is not None:
    my_dict[key] = list(my_dict[key]).append(val)

    print (str(my_dict["a"]))



list(map(print,("80X300X1000".split('X'))))

body = list(map(float, ("80X300X1000".split('X'))))
print(body)

print([0.0]*3)

import os
result = os.path.splitext("1.jpeg")
print(result[1][0:])
print ("1")
