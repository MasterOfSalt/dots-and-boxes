def transform_90(coord,n):
    x,y,o = coord
    if o == "h":
        return y,(n-x),"v"
    if o == "v":
        return y,(n-x)-1,"h"


print(transform_90((0,0,"h"),6))
print(transform_90((0,1,"h"),6))
print(transform_90((0,2,"h"),6))

print(transform_90((1,0,"h"),6))
print(transform_90((1,1,"h"),6))
print(transform_90((1,2,"h"),6))

print(transform_90((0,0,"v"),6))
print(transform_90((1,0,"v"),6))
print(transform_90((2,0,"v"),6))

print(transform_90((0,1,"v"),6))
print(transform_90((1,1,"v"),6))
print(transform_90((2,1,"v"),6))
