#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# BMI Caluclator

import sys, math
def main():
    if len(sys.argv) < 3:
        print("Usage: bmi.py height(m) weight(kg)")
        print("Uses the metric system")
        return
    height = float(sys.argv[1])
    weight = float(sys.argv[2])
    bmi = weight / math.pow(height, 2)
    print(bmi)
    if bmi < 15:
        print("YOU SHOULD BE DEAD")
    elif bmi < 18.5:
        print("gain some weight")
    elif bmi < 25:
        print("yeah you're okay")
    elif bmi < 30:
        print("a bit fat")
    else:
        print("lose some weight fatty")
main()
