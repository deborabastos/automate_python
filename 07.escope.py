# eggs = 200

# def spam():
# 	eggs = 99
# 	bacon()
# 	print(eggs)

# def bacon():
# 	ham = 101
# 	eggs = 0
# 	print(eggs)

# spam()
# print(eggs)

def spam():
	global eggs
	eggs = 'Hello'
	print(eggs)

eggs = 42
spam()
print(eggs)
