def validate_dict(rules, dictio):
    for key, value in dictio.items():
        app = False
        for rule in rules:
            if key == rule[0]:
                app = True
        if not app:
            return False
    for key, prefix, middle, suffix in rules:
        if key not in dictio:
            return False
        value = dictio[key]
        if not value.startswith(prefix) or not value.endswith(suffix):
            return False
        middle_index = value.find(middle)
        if middle_index == -1 or middle_index == 0 or middle_index == len(value) - len(middle):
            return False
    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictio = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(validate_dict(rules, dictio))
