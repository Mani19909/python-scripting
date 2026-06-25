sample_str = "This is a sample string"
print(sample_str)

# How to access individual characters from a string
print(sample_str[8])

# slicing
sub_str = sample_str[2:7]
print(sub_str)

sub_str = sample_str[:]
print(sub_str)

sub_str = sample_str[1:]
print(sub_str)

sub_str = sample_str[:5]
print(sub_str)

sub_str = sample_str[::2]
print(sub_str)

# Reverse a string
sub_str = sample_str[::-1]
print(sub_str)

# Length of a string 
len_str = len(sample_str)
print(len_str)

# Method
sample_str = "hello"
print(sample_str.capitalize()) # "Hello"

# split(), join(), format(), count(), string()
sample_str = "This is a sample string"
str_split = sample_str.split()
print(str_split)
