def format_string(string, length):
    if len(string)>=length:
        return string
    else:
        adds = (length - len(string))//2
        string = " "*adds + string + " "*adds
        print(len(string))
        return string
        
        
print("~"+format_string("abaa", 15)+"~")