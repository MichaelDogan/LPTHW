def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
			
print remove_duplicates([4,5,5,4])