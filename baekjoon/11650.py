N = int(input())
array = []

for i in range(N):
    [a,b] = map(int, input().split())
    array.append([a,b])

copy_arr = sorted(array)

for i in range(N):
    print(copy_arr[i][0], copy_arr[i][1])
   

    