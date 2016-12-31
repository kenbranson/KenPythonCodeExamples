# Basically just a function that uses a "yield" command to return data to the caller, similar to an iterator but without defining a next() method.
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]