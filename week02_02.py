# to_json decorator
import json
import functools

def to_json(func):
#    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapped

@to_json
def a():
    return None
@to_json
def b(x,y):
    return x*y
@to_json
def c(key, val):
    my_dict=dict()
    my_dict.update({key: val})
    return my_dict

res1=a()
res2=b(1,2)
res3=c("a",2)

print(type(res1))
print(type(res2))
print(type(res3))

print(a.__name__)