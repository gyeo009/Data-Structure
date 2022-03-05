# 두 개의 프로그램은 같은 결과를 내지만, 아래 프로그램이 더 효율적이다. 
# 즉, 더 효율적인 자료구조를 가진다.

a1 = 1 # integer
a2 = 2
a3 = 3

a = a1 + a2 + a3
print(a)

a = [1,2,3]  # a: list
sum = 0
for val in a:
    sum += val
print(sum)