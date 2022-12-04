a = '!announce @here <#123456789012345678>'
b = '!announce @everyone <#123456789012345678>'

alen = len(a)
blen = len(b)

print(a)
print(alen)

a_cut = a[10:]
b_cut = b[10:]

here_text = len('@here')+3
everyone_text = len('@everyone')+3
lenroomid = 18

print(a_cut)
print(b_cut)

print(lenroomid)

a_data = a_cut[here_text:]
b_data = b_cut[everyone_text:]

print(a_data)
print(b_data)

a_room = a_data[:lenroomid]
b_room = b_data[:lenroomid]

print(a_room)
print(b_room)
