def check_for_lists(code,file_obj):
    
    lists = []
    for line in code:
        if "[]" in line:
            list_name = line.split("=")[0].replace(" ","")
            lists.append(list_name)
    return lists

def check_for_dicts(code,file_obj):
    
    dicts = []
    for line in code:
        if "{}" in line:
            dict_name = line.split("=")[0].replace(" ","")
            dicts.append(dict_name)
    return dicts
