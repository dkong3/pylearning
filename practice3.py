

val = input("type some comma separated num: ")
list = val.split(",")
list[1] = int(list[1])
tuple = tuple(list)
# tuple[2] = int(tuple[2])
print('List: ', list)
print('Tuple: ', tuple)
print(list[0],list[1])
print(type(list[1]))
print(type(tuple[1]))
print(list[1]+tuple[1])

help(str.split())