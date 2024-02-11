# #Approach 1
# def doubleL(n):
#     res = []
#     for i in range(n): res.append(i * 2)
#     return res

# for i in doubleL(5): 
#     print(i, end=' : ')

#Approach 2
# for x in [n * 2 for n in range(5)]:
#     print(x, end=' : ')

#Approach 3
def doubleG(n):
        for i in range(n):
            yield i * 2

for i in doubleG(5):
        print(i, end=' : ')