

super_lst = ['bob', 'sam', 'ralph', 'harry', 'ed', 'bob', 'sam', 'ralph', 'harry', 'ed', 'bob', 'sam', 'ralph', 'harry', 'ed']

lame_lst = []
for i in super_lst:
    if i not in lame_lst:
        lame_lst.append(i)

print(lame_lst)