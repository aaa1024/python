#"ab"是地址（address）簿(book)的缩写
ab={
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@thotmainl.com'
}

print("Swaroop's address is",ab['Swaroop'])

#删除一对键值-值配对
del ab['Spammer']

print('\nThere are {} contact in the address_book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))

#添加一对键值-直配对
ab['Guido']='guido@python.org'

if'Guido'in ab:
    print("\nGuido's address is",ab['Guido'])

