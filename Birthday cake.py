def years(years, width):
    center = int(width / 2)
    result = ' ' * center + str(years)
    return result


def layer_one(length, width, name):
    ch = name[0]
    for line in range(length):
        if line == 0:
            print(' ' * 2 + ch * width)
        else:
            print(' ' * 2 + '|' + '~' * (width - 2) + '|')


def layer_two(length_two, width, name):
    ch = name[0]
    for line in range(length_two):
        if line == 0:
            print(' ' * 1 + ch * width)
        else:
            print(' ' * 1 + '|' + '~' * (width - 2) + '|')


name = str(input('Name: '))
years_old = int(input('Years old: '))

length_first = 2
length_second = 3
width = 10

print(years(years_old, width))
layer_one(length_first, width - 2, name)
layer_two(length_second, width, name)
print('=' * (width + 2))
print(f'Happy Birthday,\n{name}!')

#Name: Mihaela
#Years old: 25
#     25
#  MMMMMMMM
#  |~~~~~~|
# MMMMMMMMMM
# |~~~~~~~~|
# |~~~~~~~~|
#============
#Happy Birthday,
#Mihaela!
