def sum_of_numbers_divisible_by_3_or_5(limit):
    """Calculates the sum of all the multiples of 3 or 5 below the limit"""
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)
def sum_of_divisable_numbers(x,y,limit):
    p = (limit-1)//x
    q = (limit-1)//y
    z = (limit-1)//(x*y)
    sumx = x*(0.5*p*(p+1))
    sumy = y*(0.5*q*(q+1))
    sumz = x*y*(0.5*z*(z+1))
    return int(sumx+sumy-sumz)
limit = 1000
if limit > 100000:
    print(sum_of_divisable_numbers(3,5,limit))
else:
    print(sum_of_numbers_divisible_by_3_or_5(limit))

