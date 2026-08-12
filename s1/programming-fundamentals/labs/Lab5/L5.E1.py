# Get user's input
user_input = input("").split(" ")

# Define initial values to be None
# will be initialized to the first valid number in the input
_min = None
_max = None

# loop through the input
for item in user_input:
    # if it's a extra whitespace, we can ignore that and exit early
    if item == "":
        continue

    # we parse it as a float first
    # because there might be a decimal point
    _parsed = float(item)

    # if the element _does not_ contain a decimal point,
    # we reinitialize it to be a int
    if "." not in item:
        _parsed = int(item)

    # if either of the state variables (_min and _max) are None
    # we should set them to the current number
    if _min is None or _max is None:
        _min = _parsed
        _max = _parsed
        # we can exit early here as we don't have to do any more comparisions.
        continue

    # at last, the comparisions
    if _parsed < _min:
        _min = _parsed
    elif _parsed > _max:
        _max = _parsed

print("Minimum =", _min)
print("Maximum =", _max)
