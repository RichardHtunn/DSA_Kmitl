def generate_subsets(nums):

    nums = list(dict.fromkeys(nums))
    
    def recurse(index):
        if index < 0:
            return [[]]
        
        prev_subsets = recurse(index - 1)
        
        new_subsets = []
        for subset in prev_subsets:
            new_subset = subset + [nums[index]]
            if new_subset not in prev_subsets:
                new_subsets.append(new_subset)
                
        return prev_subsets + new_subsets

    return recurse(len(nums) - 1)

user_input = input("Enter number: ")
clean_input = user_input.replace('[', ' ').replace(']', ' ').replace(',', ' ')
parsed_input = [int(x) for x in clean_input.split()]
subsets = generate_subsets(parsed_input)
print(f"Subset: {subsets}")