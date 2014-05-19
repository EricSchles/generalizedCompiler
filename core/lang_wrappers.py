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
