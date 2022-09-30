# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
# def array_diff(a, b):
#     out = []
#     for number in a:
#         if number in b:
#             pass
#         else:
#             out.append(number)
#     return out


# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

# def count_bits(n):
#     binary = bin(n)
#     return sum([int(i) for i in str(binary) if i == '1'])

# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

# def duplicate_count(text):
#     count = 0
#     tex = [i.lower() for i in text]
#     tes = set(tex)
#     for i in tes:
#         if tex.count(i) > 1:
#             count += 1
#             for _ in range(tex.count(i)):
#                 tex.remove(i)
#         else:
#             pass
#     return count


#https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

# def find_outlier(integers):
#     even = [num for num in integers if int(num)%2 == 0]
#     odd = [num for num in integers if int(num)%2 != 0]
#     if len(odd) == 1:
#         return odd[0]
#     if len(even) == 1:
#         return even[0]



#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

# def duplicate_encode(word):
#     lis = list(word.upper())
#     res = ''
#     for i in lis:
#         if lis.count(i) == 1:
#             res += '('
#         else:
#             res += ')'
#     return res



#https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

# def alphabet_position(text):
#     alp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     tex = [i.upper() for i in text if i.upper() in alp]
#     ind = [str(alp.index(j) + 1) for j in tex]
#     return ' '.join(ind)


#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

# def persistence(n):
#     q = [int(i) for i in str(n)]
#     r = 1
#     count = 1
#     for k in q:
#         r *= k
#     while len(str(r)) >= 2:
#         n = r
#         r = 1
#         p = [int(j) for j in str(n)]
#         count += 1
#         for l in p:
#             r *= l
#     if len(str(n)) == 1:
#         return 0
#     else:
#         return count

#https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

# def is_valid_walk(walk):
#     if len(walk) == 10:
#         if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
#             return True
#         else:
#             return False
#     else:
#         return False


#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

# def unique_in_order(iterable):
#     res = []
#     inp = list(iterable)
#     for i in range(len(inp)):
#         if res == []:
#             res.append(inp[0])
#         elif inp[i] != res[-1]:
#             res.append(inp[i])
#         else:
#             pass
#     return res

#https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

# import re
# def to_camel_case(text):
#     sep = re.split(', |_|-|!|\+',text)
#     res = []
#     for i in sep:
#         if sep.index(i) == 0:
#             res.append(i)
#         else:
#             res.append(i.capitalize())
#     return ''.join(res)



#https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
# from dataclasses import replace
# import re


# def is_pangram(s):
#     ref = [i for i in 'abcdefghijklmnopqrstuvwxyz']
#     sep = re.split(', |_|-|!|\+',s)
#     stri = ''.join(sep)
#     joint = stri.replace(' ','')
#     pra = [i.lower() for i in joint]
#     prav = list(set(pra))
#     prav.sort()
#     prav = [k for k in prav if k.isalpha()]
#     return prav == ref

# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

# def narcissistic( value ):
#     sum = 0
#     for i in str(value):
#         i=int(i)
#         i = i**len(str(value))
#         sum += i
#     return sum == value



#https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

# def tribonacci(signature, n):
#     res = signature
#     for i in range(n-3):
#         res.append(sum(res[-3:]))   
#     return res

#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

# def dig_pow(n, p):
#     sum1 = 0
#     for i in str(n):
#         sum1 += int(i) ** p
#         p += 1 
#     p = sum1/n
#     if p-round(p) == 0:
#         return int(p)
#     else:
#         return -1


# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

# def solution(s):
#     u = []
#     if s != '':
#         for i in range(0,len(s),2):
#             u.append(s[i:i+2])
#         if len(u[-1]) == 1:
#             u[-1] = u[-1] + '_'
#         else:
#             pass
#         return u
#     else:
#         return []

# def comp(a,b):
#     a.sort()
#     a.sort()
#     c = [int(num**0.5) for num in b]
#     c = list(set(c))
#     a = list(set(a))
#     a.sort()
#     c.sort()
#     if c == a:
#         return True
#     else:
#         print(a)
#         print(c)
#         return False


# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

# f = comp(a,b)
# print(f)


# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
# apl = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


# def find_missing_letter(a):
#     n = len(a)

#     ind = apl.index(a[0])
#     r = apl[ind:ind+1+n]
#     ad = ""
#     for i in r:
#         if i not in a:
#             ad += i
#     return ad



# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
# def count_smileys(arr):
#     count = 0
#     for str in arr:
#         str_lis = list(str)
#         if str_lis[0] == ';' or str_lis[0] == ':':
#             if str_lis[1] == ')' or str_lis[1] == 'D':
#                 count += 1
#             elif str_lis[1] == '-' or str_lis[1] == '~':
#                 if str_lis[2] == ')' or str_lis[2] == 'D':
#                     count += 1
#     return count


# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python



def high(x):
    def index_maxi(arr,numb):
        for i in range(len(arr)) :
            if arr[i] == numb :
                return i

    def alph_value(alpha):
        alph = 'abcdefghijklmnopqrstuvwxyz'
        return alph.index(alpha)+1
    num_lis = []
    lis = x.split()
    for i in lis:
        sum = 0
        for j in i:
            sum += int(alph_value(j))
        num_lis.append(sum)
    maxi_num = max(num_lis)
    ind = index_maxi(num_lis,maxi_num)
    return lis[ind]

c =  high('man i need a taxi up to ubud')
print(c)

# alph = 'abcdefghijklmnopqrstuvwxyz'
# def alph_value(alpha):
#     alph = 'abcdefghijklmnopqrstuvwxyz'
#     return alph.index(alpha)+1

# for i in alph:
#     print(i)
#     b = alph_value(i)
#     print(b)