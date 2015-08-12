# Roman Numerals Overview

Converting integers to and from Roman numerals: 
*Your task is to create a function that takes an integer `x` as input and produces as output a `string` that represents the number in roman numerals.*

## Overview
Roman numerals are a representation of positive whole numbers using letters.
In programming, we would say they represent positive integers as strings. 
The basic mapping is as follows:
I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000

## Rules for Roman Numerals:

1. Letters are repeated and their values summed to represent numbers between those steps:
III -> 3
CCC -> 300
MMM -> 3000 
2. If a letter of smaller value is placed _after_ another letter, add the smaller value:
VII -> 7
LXI -> 61
DCI -> 601
3. If a letter of smaller value is placed _before_ another letter, subtract the smaller value:
IV -> 4
XC -> 90
CM -> 900
    a. Only subtract powers of ten (I, X, or C, but not V or L)

        For 95, do NOT write VC (100 – 5).
        DO write XCV (XC + V or 90 + 5)

    b. Only subtract one number from another.

        For 13, do NOT write IIXV (15 – 1 - 1).
        DO write XIII (X + I + I + I or 10 + 3)

    c. Do not subtract a number from one that is more than 10 times greater (that is, you can subtract 1 from 10 [IX] but not 1 from 20—there is no such number as IXX.)

        For 99, do NOT write IC (C – I or 100 - 1).
        DO write XCIX (XC + IX or 90 + 9) 

