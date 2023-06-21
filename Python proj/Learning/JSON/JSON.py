import  json
input = '''
[
 { "id" : "01",
 "x":"2",
 "name" : "Chuck"
 },
  { "id" : "02",
 "x":"1287",
 "name" : "gigachad"
 }]
 '''

info = json.loads(input)
print('User count: ', len(info))

for item in info:
    print('Name', item['name'])
    print('Id',item['id'])
    print('Attribute', item['x'])
    