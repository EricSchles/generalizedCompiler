def parse(file_obj):
    with open(file_obj,"r") as code:
        for line in code:
            line = line.strip("\n") 
            if "#!?" in line and "end" in line:
                list_of_code.append(lang_obj)
                continue
            if "#!?" in line and "start" in line:
                lang_obj = []
            lang_obj.append(line)
    return list_of_code
