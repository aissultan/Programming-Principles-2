def spy_game(nums):
    s = ""
    for i in nums:
        if(i == 0 or i == 7):
            s += str(i)
    if s.find("007") != -1:
        print("True")
    else:
        print("False")

a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# d = list(map(int, input().split()))
spy_game(a)
# spy_game(b)
# spy_game(c)
# spy_game(d)
# spy_game([1,2,4,0,0,7,5]) 
# spy_game([1,0,2,4,0,5,7]) 
# spy_game([1,7,2,0,4,5,0])