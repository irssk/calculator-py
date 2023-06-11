
def keys_to_string(obj: dict):
    i = 0

    string = ""

    keys = obj.keys()
    keys_len = len(keys)

    for key in keys:
        i = i + 1

        if key == "label":
            continue

        if keys_len == i:
            string += f"{key}"
            continue

        string += f"{key}, "

    return string