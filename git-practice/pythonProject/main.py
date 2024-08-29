def disemvowel(string_):
    strin= "aeiouAEIOU"
    for i in string_:
        if i in strin:
            string_=string_.replace(i, "")
    return string_


string_ = "Hello"
print(string_)

