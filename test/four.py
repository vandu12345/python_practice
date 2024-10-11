
def odd_even(number):
    if number %2 ==0:
        return True
    
    return False



def sum_even(num):
    
    even_sum = 0
    
    for i in range(1, num+1):
        if odd_even(i):
            even_sum+=i
    
    return even_sum


even_sum = sum_even(10)

print(even_sum)