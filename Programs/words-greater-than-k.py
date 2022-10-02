# Python program to find all string
# which are greater than given length k

# function find string greater than length k
def string_k(k, str):
	
	# create the empty string
	string = []
	
	# split the string where space is comes
	text = str.split(" ")
	
	# iterate the loop till every substring
	for x in text:
		
		# if length of current sub string
		# is greater than k then
		if len(x) > k:
			
			# append this sub string in
			# string list
			string.append(x)
			
	# return string list
	return string


k = int(input("Enter the minimum length of words"))
str = input("Enter a string")
print(string_k(k, str))
