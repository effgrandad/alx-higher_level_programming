#!/usr/bin/python3
if __name__ == "__main__":
    """print all hidden directories"""
    import hidden_4

    for j in dir(hidden_4):
        if j[:2] != "_":
            print(j)
