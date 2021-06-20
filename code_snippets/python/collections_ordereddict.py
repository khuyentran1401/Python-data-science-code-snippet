import collections

tasks = collections.OrderedDict(laundry=0.5, shopping=2, clean=2)
tasks['movie'] = 2
print(tasks)
# OrderedDict([('laundry', 0.5), ('shopping', 2), ('clean', 2), ('movie', 2)])

print(tasks.keys())
# odict_keys(['laundry', 'shopping', 'clean', 'movie'])