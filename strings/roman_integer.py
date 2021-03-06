# dictionary {'I' : 1, 'V': 5}, 
# IV less < greater, subtract I
# VI greater > less, add I
class Solution:
	# @param A : string
	# @return an integer
	def romanToInt(self, A):
		roman = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
		num = 0
		for i in xrange(len(A)):
			if i < (len(A)-1) and roman[A[i]] < roman[A[i+1]]:
				num -= roman[A[i]]
			else:
				num += roman[A[i]]
		return num


"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14
Input : "XX"
Output : 20


Details - 

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1,000

Numbers are formed by combining symbols and adding the values, so II is two (two ones) and XIII is thirteen (a ten and three ones). Because each numeral has a fixed value rather than representing multiples of ten, one hundred and so on, according to position, there is no need for "place keeping" zeros, as in numbers like 207 or 1066; those numbers are written as CCVII (two hundreds, a five and two ones) and MLXVI (a thousand, a fifty, a ten, a five and a one).

Symbols are placed from left to right in order of value, starting with the largest. However, in a few specific cases,[2] to avoid four characters being repeated in succession (such as IIII or XXXX), subtractive notation is often used as follows:[3][4]

I placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)
X placed before L or C indicates ten less, so forty is XL (ten less than fifty) and ninety is XC (ten less than a hundred)
C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand)[5]


Approach

Work backwards
MCMLIV = 1954
V > I = 5-1
L < M = add L
M > C = 1000 - 10
M = 1000
"""
