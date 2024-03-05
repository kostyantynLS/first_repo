#test module

def MyModule(str_name = "William") -> str:
    if str_name == "":
        return "nameless"
    if str_name.isnumeric():
        return "digitazer"
    if str_name.find(" ") != -1:
        return "longnamed"
    return str_name

if __name__ == "__main__":
    print('please import this module not direct run!')
    