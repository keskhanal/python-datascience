"""Local vs global variables."""

counter = 0            # global

def show():
    print("reading the global:", counter)   # reading is fine

def local_only():
    counter = 100                            # creates a NEW local variable
    print("inside:", counter)

def really_global():
    global counter                           # now we mean the global one
    counter += 1

show()
local_only()
print("after local_only, global is still:", counter)

really_global()
print("after really_global:", counter)

# Prefer parameters and return values over `global` - they make the
# data flow obvious and the function easy to test.
def increment(value):
    return value + 1

counter = increment(counter)
print("preferred style:", counter)
