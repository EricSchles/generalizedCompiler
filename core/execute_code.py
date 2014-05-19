from subprocess import call
import os
def run(files_to_run): 
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
