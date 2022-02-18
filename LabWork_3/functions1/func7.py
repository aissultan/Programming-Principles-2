def has_33(nums):
    s = ""
    for i in nums:
        s += str(i)
    if (s.find("33") != -1):
        print("True")
    else:
        print("False")

a = list(map(int, input().split()))
has_33(a)
# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])
# has_33(list(map(int, input().split())))
