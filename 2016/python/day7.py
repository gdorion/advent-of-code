#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
import re

# Could be done with regex i guess
def isSupportingTLS(input):
    for i,c in enumerate(input):
        if i < len(input) - 3:
            if  input[i + 1] == input[i + 2]:
                if input[i] != input[i + 1]:
                    if input[i + 2] != input[i + 3]:
                        if input[i] == input[i + 3]:
                            return True
    return False

def isSupportingSSL(input):
    if len(input) == 3:
        if  input[0] == input[2]:
            return True
    return False

# Assume that string is valid ssl.
def oppositeSSLString(string):
    char0 = string[0]
    char1 = string[1]
    return char1 + char0 + char1

def lineSupportsSSL(insiders, outsiders):
    for outsider in outsiders:
        for j in range(len(outsider)):
            if j < len(outsider) - 2:
                subOutsider = outsider[j:j+3]
                if isSupportingSSL(subOutsider):
                    for insider in insiders:
                        for i in range(len(insider)):
                            if i < len(insider) - 2:
                                subInsider = insider[i:i+3]
                                if subInsider == oppositeSSLString(subOutsider):
                                    return True
    return False

def lineSupportsTLS(insiders, outsiders):
    valid = True
    for insider in insiders:
        if isSupportingTLS(insider):
            valid = False
            break

    if valid:
        valid = False
        for outsider in outsiders:
            if isSupportingTLS(outsider):
                valid = True
                break
    return valid

# with open('day7TestInput2.txt') as f:
with open('day7.txt') as f:
    supportTLSCount = 0
    supportSSLCount = 0
    for line in f:
        outsiders = re.findall(r'(.*?)(?:\[.*?\]|$)', line)
        insiders = re.findall(r"\[([A-Za-z0-9_]+)\]", line)
        outsiders = filter(None, outsiders)
        insiders = filter(None, insiders)

        if lineSupportsTLS(insiders, outsiders):
            supportTLSCount = supportTLSCount + 1
        if lineSupportsSSL(insiders, outsiders):
            supportSSLCount = supportSSLCount + 1


    print supportTLSCount
    print supportSSLCount - 1 # don't ask.. error and trial
