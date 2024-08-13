def check_numbers(nums):
    for x in nums:
        if x.isalpha() == False:
            if x == "0":
                print(5)
                return
            else:
                for y in nums[nums.find(x):]:
                    if y.isalpha():
                        print(2)
    print(1)
check_numbers("nrvous")
