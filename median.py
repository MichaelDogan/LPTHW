def median(lst):
    working_list = sorted(lst)
    if len(working_list) % 2 == 0:
        return ((working_list[len(working_list) / 2]) + (working_list[len(working_list) / 2 - 1])) / 2.0
    else:
        return working_list[len(working_list)/2]

 
my_list = [5,2,3,4,1]
my_other_list = [3,2,1,4]

print median(my_list)
print median(my_other_list)
