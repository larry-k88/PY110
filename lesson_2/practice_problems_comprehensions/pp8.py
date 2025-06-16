# Given the following data structure, write some code to return a list
# that contains the colors of the fruits and the sizes of the
# vegetables. The sizes should be uppercase, and the colors should be
# capitalized.

# Expected: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

output = [transform_item(food_details) for food_details in dict1.values()]

print(output)