def fxn(nums) -> str:
    li, ans = [], []
    nums.sort()
    for i in range(len(nums)):
        try:
            if nums[i] + 1 == nums[i + 1]:
                li.append(nums[i])
                li.append(nums[i+1])
            else:
                if li:
                    li = list(set(li))
                    li.sort()
                    ans.append(li)
                    li = []
        except IndexError:
            if li:
                li = list(set(li))
                li.sort()
                ans.append(li)
    print(str(ans)[1:-1])

nums = [5,7,9,8,2,3,1,12,13]
fxn(nums)