fruits = ["pineapple", "apple", "avacado", "orange"]
fruits.append("kiwi")
fruits.insert(1, "lemon")
fruits.remove("apple")
fruits.pop(2)
fruits[2] = "strawberry"
print(fruits)

Tuple = ("This", 'is', 'a', 'tuple')
print(Tuple)

# iterating over lists and tuples

animals = ['lion', 'zerbra', 'dolphion', 'monkey']
chars=0
for animal in animals:
    chars+=len(animal)
    
print("total characters: {}, average length: {}".format(chars, chars/len(animals)))


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([("llamma@urmama.com", "llamma lin")]))


def skip_elements(elements):
	# code goes here
	new_list = []
	for index, element in enumerate(elements): 
		if index % 2 == 0:
			new_list.append(element)

	
	return new_list
    
    
multipes = []
for x in range(1,11):
    multipes.append(x*7)
print(multipes)
#these are the same
multples = [x*7 for x in range (1,11)]
print(multples)

languages = ["python", 'pearl', 'ruby', 'go', 'java', 'c+', 'c']
lengths = [len(language) for language in languages]
print(lengths)

z= [x for x in range(0, 101) if x % 3 ==0]
print(z)