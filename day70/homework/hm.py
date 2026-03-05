def abbrev_name(name):
    fir, sec = name.split(" ")
    return fir[0].upper() + "." + sec[0].upper()

print(abbrev_name("jhon Doe"))
