List = open("list.txt")
List2 = (s.strip() + ' time' for s in List)
for item in List2:
    open('%s.py' % (item,), 'w')
