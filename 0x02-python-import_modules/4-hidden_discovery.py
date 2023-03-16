#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    x = dir(hidden_4)
    for names in x:
        if names[:2] != "__":
            print(names)
