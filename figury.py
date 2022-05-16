n = int(input())
for i in range(n):
    print('*'*i)
print('-----------------')
for i in range(n):
    print('*'*i)
for i in range(n, 0, -1):
    print('*'*i)
print('\n', '--------------', '\n')
for i in range(n):
    print(' '*(n-i), '*'*i*2)
for i in range(n, 0, -1):
    print(' '*(n-i), '*'*i*2)
