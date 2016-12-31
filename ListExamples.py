l = [1,2,3,4,5]
l.append(6)     # appends a single item

l2 = [7,8]
l.extend(l2)    # appends another list

l.insert(1,10)  # inserts into index 1, shifting 1 and all after it down.

l.index(10)   # returns the index value of the first item that matches the given value
l.count(10)   # Returns the number of matching items
l.remove(10)  # removes the first item in the list that matches the given value.  Error if none matches

l.pop()          # removes last item from list and returns it

l.sort()      # sorts list in place.  Can provide params to control sort comparison, direction

l.reverse()


# Passing a function to another function list sort(), filter(), map()
def f1(x):
    return x % 3 == 0 or x % 5 == 0   # True if x is divisible by 3 or 5

newl = filter(f1, l)   # only values from l where f1(l) returns true

def cube(x):
    return x^3

newl2 = map(cube, l)    # returns a new list containing cube(l) for each item in l

def times(a,b):
    return a * b

reduce(times, l)        # this will pass first 2 members of l as args to times(), then the results and the next item in l,
                        # etc. until all items in l have been processed

# List comprehensions: a shorthand way to create a new list
squares = [x**2 for x in range(10)]  # Basically, some expression for each x in some given list.  Very similar to simple
                                     # blocks in Gosu

# a more complex example of a list comprehension:
myTuples = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]