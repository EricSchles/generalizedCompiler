from subprocess import call
from sys import argv
import os


list_of_arrays = {
    "python":"[]",
    "ruby":"[]"
    }

def java_start(f):
    #f is a file object
    f.write("public class tmp{\n")
    f.write("public static void main(String args[]){\n")

def java_end(f):
    f.write("}\n")
    f.write("}\n")

def cpp_start(f):
    f.write("#include <iostream>\n\n")
    f.write("using namespace std;\n\n")
    f.write("int main()\n{\n")

def cpp_end(f):
    f.write("return 0;\n")
    f.write("}")

file_obj =  argv[1]

list_of_code = []
with open(file_obj,"r") as code:
    for line in code:
        line = line.strip("\n") 
        if "#!?" in line and "end" in line:
            list_of_code.append(lang_obj)
            continue
        if "#!?" in line and "start" in line:
            lang_obj = []
        lang_obj.append(line)


os.mkdir("tmp")        
os.chdir("tmp")
files_to_run = []
for lang_obj in list_of_code:
    to_run = []
    list_of_lists = []
    first_line = lang_obj[0]
    lang = first_line.split("start")[1].lstrip(" ")
    if lang == "cpp":
        lang_file = "tmp.cpp"
    if lang == "java":
        lang_file = "tmp.java"
    if lang == "python":
        lang_file = "tmp.py"
    if lang == "ruby":
        lang_file = "tmp.rb"
    if lang == "perl":
        lang_file = "tmp.pl"

    lang_list = []
    for lang_check,lang_file_check in files_to_run:

        lang_list.append(lang_check)
    
    if lang in lang_list:
        count = lang_list.count(lang)
        if lang == "python":
            lang_file = "tmp"+str(count)+".py"
        if lang =="ruby":
            lang_file = "tmp"+str(count)+".rb"
        if lang == "perl":
            lang_file = "tmp"+str(count)+".pl"
        if lang == "java":
            lang_file = "tmp"+str(count)+".java"
        if lang == "cpp":
            lang_file = "tmp"+str(count)+".cpp"

    with open(lang_file,"w") as f:
        if lang == "java":
            java_start(f)
        if lang == "cpp":
            cpp_start(f)
        for i in xrange(1,len(lang_obj)):
            # array = list_of_arrays[lang]
            # if -1 != lang_obj[i].find(array):
            #     list_of_lists.append(lang_obj[i])
            lang_obj[i] += "\n"
            f.write(lang_obj[i])
        if lang == "java":
            java_end(f)
        if lang == "cpp":
            cpp_end(f)
    
    to_run.append(lang)
    to_run.append(lang_file)
    
    files_to_run.append(to_run)

for i in files_to_run:
    lang = i[0]
    lang_file = i[1]
  
    if lang == "java":
        lang_file_exe = lang_file.split(".")[0]
        lang_file_remove = lang_file_exe +".class"
        call(["javac",lang_file])
        call([lang,lang_file_exe])
        os.remove(lang_file)
        os.remove(lang_file_remove)
    elif lang == "cpp":
        lang_file_exe = lang_file.split(".")[0]
        call(["g++","-o",lang_file_exe,lang_file])
        call(["./"+lang_file_exe])
        os.remove(lang_file)
        os.remove(lang_file_exe)
    else:
        call([lang,lang_file])
        os.remove(lang_file)

os.chdir("../")
os.rmdir("tmp")

