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

res_tuple_1 = sliced_tuple * 2
print(res_tuple_1)

# Methods
k8s_idx = res_tuple.index("K8s")
print(k8s_idx)

# Tuple unpacking 
ansible, terraform, jenkins, docker, k8s  = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s") # Tool set

print(ansible, terraform, jenkins, docker, k8s)

ansible, *tools, orchestrator = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s", "DevOps")
print(ansible, tools, orchestrator)