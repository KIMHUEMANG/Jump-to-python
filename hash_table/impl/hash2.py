
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_func(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_func(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_func(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '11111111111')
save_data('Wave', '11112231111')
save_data('Save', '11132323111')

print(read_data('Dave')) 