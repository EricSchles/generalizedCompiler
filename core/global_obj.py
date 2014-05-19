class python_list_obj:
    def __init__(self,name):
        self.name = name
        self.obj = []
    def append(self,item):
        self.obj.append(item)
    def sort(self):
        self.obj.sort()
    def pop(self):
        return self.obj.pop()
    def remove(self,item):
        self.obj.remove(item)
    def reverse(self):
        self.obj.reverse()
    def count(self,item):
        return self.obj.count(item)
    def insert(self,index,item):
        self.obj.insert(index,item)
    def extend(self,iterator):
        self.obj.extend(iterator)
    def index(self,value,start,stop):
        return self.obj.index(value,start,stop)

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
