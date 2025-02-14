#Access nested dictionary values.

family = {
    'me': {
        'name':'alex',
        'age':27
    },
    'dad':{
        'name':'andrew',
        'age':62
    },
    'mom':{
        'name':'nancy',
        'age':52
    }
}

print(family['mom']['name'])

for x, obj in family.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])