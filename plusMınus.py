def plusMinus(arr):
    positive=0
    negative=0
    zeros=0
    for i in range(0,len(arr)):
        if arr[i]>0:
            positive = positive + 1
        elif arr[i]<0:
            negative = negative + 1
        else:
            zeros = zeros + 1
    print(positive/len(arr))
    print(negative/len(arr))
    print(zeros/len(arr))
  





arr=[0, 0 ,-1, 1, 1]

plusMinus(arr)