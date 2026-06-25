# There are 2 methods to create a tuple
# 1. ()
# 2. tuple()
# Behaviour: They're immutable

sample_tuple = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s") # Tool set

sample_ele = sample_tuple[1]
print(sample_ele)

sample_ele = sample_tuple[-1]
print(sample_ele)

# Slicing
sliced_tuple = sample_tuple[1:3]
print(sliced_tuple)

# sample_tuple[1] = "Shell"
# print(sample_tuple)

"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-scripting/03_tuples.py", line 18, in <module>
    sample_tuple[1] = "Shell"
    ~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""

# Operations
res_tuple = sample_tuple + sliced_tuple
print(res_tuple)