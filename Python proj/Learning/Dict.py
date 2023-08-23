filecount = {'jpg':10,'txt':14,'csv':2, 'py':2}
print(filecount)
print(filecount['txt'])
print('jpg' in filecount)

# dictionary are mutable
filecount['cfg'] = 8
print(filecount)

#iterating over dictionary
for extension in filecount:
    print(extension)
    
#retriving the values associated with keys
for ext, amount in filecount.items():
    print('using the .format method amount={} and extension is {}.'.format(amount,ext))
    
#returning just the keys or values
    
print(filecount.keys())
print(filecount.values())
#
for value in filecount.values():
    print(value)
for keys in filecount.keys():
    print(keys)
    
def allletters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    print(result)
allletters('all of these letterrrrrrs')

