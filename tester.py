def transform_horizontal_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return abs(n-x),y,o
    if o == "v":
        return abs(n-x-1),y,o

def transform_vertical_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return x,abs(n-y-1),o
    if o == "v":
        return x,abs(n-y),o

def transform_90_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return y,abs(n-x),"v"
    if o == "v":
        return y,abs(n-x-1),"h"

def transform_180_nxn(coord,n):
    return transform_90_nxn(transform_90_nxn(coord,n),n)
def transform_270_nxn(coord,n):
    return transform_90_nxn(transform_180_nxn(coord,n),n)

print(transform_vertical_nxn((0,0,"v"),5))
print(transform_vertical_nxn((0,5,"v"),5))
print(transform_vertical_nxn((1,2,"v"),5))
print(transform_vertical_nxn((1,3,"v"),5))
print(transform_vertical_nxn((1,0,"h"),5))
print(transform_vertical_nxn((1,4,"h"),5))
print(transform_vertical_nxn((4,1,"h"),5))
print(transform_vertical_nxn((4,3,"h"),5))


# print(transform_horizontal_nxn((0,0,"v"),4))
# print(transform_horizontal_nxn((3,0,"v"),4))
# print(transform_horizontal_nxn((0,3,"v"),4))
# print(transform_horizontal_nxn((3,3,"v"),4))
# print(transform_horizontal_nxn((1,2,"v"),4))
# print(transform_horizontal_nxn((2,2,"v"),4))
# print(transform_horizontal_nxn((0,0,"h"),4))
# print(transform_horizontal_nxn((4,0,"h"),4))
# print(transform_horizontal_nxn((1,2,"h"),4))
# print(transform_horizontal_nxn((3,2,"h"),4))
# print(transform_horizontal_nxn((2,0,"h"),4))
# print(transform_horizontal_nxn((2,0,"h"),4))
# print(transform_vertical_nxn((0,0,"v"),4))
# print(transform_vertical_nxn((0,4,"v"),4))
# print(transform_vertical_nxn((2,1,"v"),4))
# print(transform_vertical_nxn((2,3,"v"),4))
# print(transform_vertical_nxn((1,0,"h"),4))
# print(transform_vertical_nxn((1,3,"h"),4))
# print(transform_vertical_nxn((3,1,"h"),4))
# print(transform_vertical_nxn((3,2,"h"),4))
# print(transform_horizontal_nxn((0,0,"v"),5))
# print(transform_horizontal_nxn((4,0,"v"),5))
# print(transform_horizontal_nxn((0,3,"v"),5))
# print(transform_horizontal_nxn((4,3,"v"),5))
# print(transform_horizontal_nxn((1,1,"v"),5))
# print(transform_horizontal_nxn((3,1,"v"),5))
# print(transform_horizontal_nxn((2,1,"v"),5))
# print(transform_horizontal_nxn((2,1,"v"),5))
# print(transform_horizontal_nxn((0,0,"h"),5))
# print(transform_horizontal_nxn((5,0,"h"),5))
# print(transform_horizontal_nxn((1,1,"h"),5))
# print(transform_horizontal_nxn((4,1,"h"),5))
# print(transform_horizontal_nxn((2,2,"h"),5))
# print(transform_horizontal_nxn((3,2,"h"),5))














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
