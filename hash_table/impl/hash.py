hash_table = list([i for i in range(10)])

def hash_func(key):
    return key % 5

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord() 문자의 아스키코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0])) # 65 68 84
print(ord(data1[0]), hash_func(ord(data1[0])))

storage_data('Andy', '0000000')
storage_data('Dave', '11111111')
storage_data('Trump', '666666')

print(get_data('Andy'))
