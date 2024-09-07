def IsArmstrong(number):
    num_str=str(number)
    num_digits=len(num_str)
    armstrong_sum=sum(int(digits)**num_digits for digits in num_str)
    return armstrong_sum==number
Number=int(input("Enter any values: "))
if IsArmstrong(Number):
    print(f"{Number},is an Armstrong Number.")
else:
    print(f"{Number},is not an Armstrong Number.")