# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
from audioop import add


def DNA_strand(dna):
    lis = list(dna)
    dict = {'A':'T','G':'C','T':'A','C':'G'}
    for i in range(len(dna)):
        val = dict[dna[i]]
        lis[i] = val
    return ''.join(lis)


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
