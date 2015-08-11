def is_even(integer):
    if integer % 2.0 == 0.0:
        return True
    else:
        return False
def purify(numbers):
    return filter(is_even,numbers)
	
my_list = [0,1,2,3,4,5,6,7,8,9,10]

print purify(my_list)