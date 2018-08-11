
def unescape(text):
    c = compile(text, "__no_file__", mode='eval')
    return eval(c)
