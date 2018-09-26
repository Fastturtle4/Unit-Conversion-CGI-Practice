#!/usr/bin/python
#Paul Barrett

#Specify content type
print 'Content-type: text/html\n\n'
import cgi
import math
import cgitb
cgitb.enable()

#create instance of FieldStorage
form = cgi.FieldStorage()

try:
    #get data from fields
    distx = form["distx"].value
    disty = form["disty"].value
    anglea = form["anglea"].value
    
    unitx = form["unitx"].value
    unity = form["unity"].value
    unita = form["unita"].value
    
    unitanswer = form["unitanswer"].value

except KeyError:
    #empty or invalid field value
    print("Error! It seems you forgot to fill in a field or used the wrong input type. Please try again.")

convertLyRad = {
        #all dist to lightyears, and angles to radians
        "parsec": 3.26,
        "kilometer": 1.057*10**(-13),
        "xlarn": 20.7864,
        "lightyear": 1,
        "degree": 0.0174533,
        "xarnian": 1/100,
        "radian": 1
        }

convertToAny = {
        #lightyear/radian conversion to all other units
        "parsec": 0.3067,
        "kilometer": 9.461*10**12,
        "xlarn": 0.0481,
        "lightyear": 1,
        "degree": 57.2957549,
        "xarnian": 100,
        "radian": 1
        }

def convert(quantity, sourceparam, destparam):
    #Use conversion dictionaries to convert
    return quantity*convertLyRad[sourceparam]*convertToAny[destparam]	

def compute(dist1, dist2, angle):
    #Law of cosines
    answer = math.sqrt(dist1**2 + dist2**2 - 2*dist1*dist2*math.cos(angle))
    return answer

try:
    #compute answer and convert to specified units
    #all input first converted to lightyears and radians for computation and 
    #final answer is converted to desired unit then displayed
    d1 = convert(float(distx), unitx, "lightyear")
    d2 = convert(float(disty), unity, "lightyear")
    a1 = convert(float(anglea), unita, "radian")
    ans = compute(d1, d2, a1)
    ansInCorrectUnits = convert(ans, "lightyear", unitanswer)
    print("Your computed distance is ")
    print(ansInCorrectUnits)

except (KeyError, ValueError, TypeError):
    #incorrect/strange input
    print("Error! It seems you forgot to fill in a field or used the wrong input type. Please try again.")

