List = open("list.txt")
List2 = (f'{s.strip()} time' for s in List)
for item in List2:
    open(f'TestFolder/{item}.py', 'w')
