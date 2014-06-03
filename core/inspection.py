#check this after
def check_for_vars():
    vars = []
    for i in list(locals().iteritems()):
        isVar = False
        for part in list(i.iteritems()):
            if not "_" in part:
                isVar = True
        if isVar:
            vars.append(i)
