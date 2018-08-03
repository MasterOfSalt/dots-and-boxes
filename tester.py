

def transform_90_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return y,(n-x),"v"
    if o == "v":
        return y,(n-x)-1,"h"

def transform_horizontal_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return (n-x),y,o
    if o == "v":
        return (n-x)-1,y,o

def transform_vertical_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return x,(n-y-1),o
    if o == "v":
        return x,(n-x),o
def transform_180_nxn(coord,n):
    return transform_90_nxn(transform_90_nxn(coord,n),n)
def transform_270_nxn(coord,n):
    return transform_90_nxn(transform_180_nxn(coord,n),n)
print(transform_90_nxn((0,0,"h"),6))
print(transform_180_nxn((0,0,"h"),6))
print(transform_270_nxn((0,0,"h"),6))

# print(transform_90((0,2,"h"),6))
#
# print(transform_90((1,0,"h"),6))
# print(transform_90((1,1,"h"),6))
# print(transform_90((1,2,"h"),6))
#
# print(transform_90((0,0,"v"),6))
# print(transform_90((1,0,"v"),6))
# print(transform_90((2,0,"v"),6))
#
# print(transform_90((0,1,"v"),6))
# print(transform_90((1,1,"v"),6))
# print(transform_90((2,1,"v"),6))
