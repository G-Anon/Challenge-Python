#!/usr/bin/env python3
def fact( n ):
    if n:
        return n * fact( n - 1 )
    else:
        return 1

print( fact( 100 ))
