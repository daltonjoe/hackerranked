def miniMaxSum(arr):
    
    arr.sort()
    min=arr[0]+arr[1]+arr[2]+arr[3]
    max=arr[1]+arr[2]+arr[3]+arr[4]

    print(min,max)

arr=[7 ,69 ,2 ,221 ,8974]
miniMaxSum(arr)
