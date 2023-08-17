#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    "Print all the hidden names in module hidden_4"

    import hidden_4

    attribute_names = dir(hidden_4)
    for name in attribute_names:
        if name[:2] != "__":
            print(name)
