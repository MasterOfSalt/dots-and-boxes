def transform_90(coord,n):
    x,y,o = coord
    if o == "h":
        return y,(n-x),"v"
    if o == "v":
        return y,(n-x)-1,"h"
