# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
# def get_sum(a,b):
#     sum = 0
#     for i in range(a,b):
#         sum += i
#     return sum
# print(get_sum(-1,2))

# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
# def arithmetic(a, b, operator):
#     dict = {'add':'+','subtract':'-','multiply':'*','divide':'/'}
#     return eval(str(a) + str(dict[operator]) + str(b))


# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
# def maskify(cc):
#     lis = list(cc)
#     for i in range(len(lis)-4):
#         lis[i] = '#'
#     return ''.join(lis)

# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
# def friend(x):
#     return [i for i in x if len(i) == 4 ]



#https://www.codewars.com/kata/56582133c932d8239900002e/train/python
# def most_frequent_item_count(collection):
#     lis = []
#     uniq = set(collection)
#     print(uniq)
#     for i in uniq:
#         suma = 0
#         for j in collection:
#             if i == j:
#                 suma +=1
#         lis.append(suma)
#     return max(lis)
        

# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
# def stray(arr):
#     arr.sort()
#     return arr[-1] if arr.count(arr[0]) > 1 else arr[0]


# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
# def solution(text, ending):
#     return True if text[-len(ending):] == ending else False

