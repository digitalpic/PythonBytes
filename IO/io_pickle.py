import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to a file
f = open(shoplistfile, 'wb')
# Dump to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open (shoplistfile, 'rb')
# Load the obj from the file
storedlist = pickle.load(f)
print (storedlist)
