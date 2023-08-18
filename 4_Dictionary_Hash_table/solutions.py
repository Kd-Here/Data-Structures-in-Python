# create a dictionary for your user defined data structure Dictionary






def hash_function(key):
    count = 0
    for i in str(key):
        count += ord(i)
    print(count % 8)


hash_function("march 9")
hash_function("march 10")
hash_function("march 11")
hash_function("march 12")