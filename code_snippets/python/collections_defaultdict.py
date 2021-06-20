from collections import defaultdict

classes = defaultdict(lambda: 'Outside')
classes['Math'] = 'B23'
classes['Physics'] = 'D24'
print(classes['Math'])
# B23

print(classes['English'])
# Outside