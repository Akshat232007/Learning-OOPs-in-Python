dict1 = {
    "A" : 12,
    "B" : 13
}

dict2 = {
    "B" : 12,
    "C" : 11
}

merge_dict = dict1 | dict2

print(merge_dict)


#Output : {'A': 12, 'B': 12, 'C': 11}

# Dictionary Union Operator (|)

# It is used to merge two dictionaries into a new dictionary.
# If the same key exists in both dictionaries,
# the value from the right-hand(down) dictionary overwrites
# the value from the left-hand(up) dictionary.


dict3 = {
    "B" : 12,
    "C" : 11
}

dict4 = {
    "A" : 12,
    "B" : 13
}

merge = dict3 | dict4

print(merge)

#output : {'B': 13, 'C': 11, 'A': 12}

dict5 = {
    "A": 12,
    "B": 13,
    "C" : 9
}

dict6 = {
    "B": 12,
    "C": 11
}

dict5 |= dict6

print(dict5)

#Output : {'A': 12, 'B': 12, 'C': 11}

# Dictionary Update Union Operator (|=)

# It is used to merge another dictionary into an existing dictionary.
# If duplicate keys exist, values from the right-hand dictionary
# overwrite the existing values.
# Unlike |, it updates the original dictionary instead of creating a new one.