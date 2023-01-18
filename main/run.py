from sys import argv
from os import system

def replace(a, b, path_from, path_to, insert=None):
    fin = open(path_from, "rt")
    fout = open(path_to, "wt")
    for line in fin:
        if insert is not None:
            fout.write(insert)
            insert = None
        fout.write(line.replace(a, b))
    fin.close()
    fout.close()

def main(argv):
    java_paths = ["./java_examples/j.java", "./java_examples/switch.java", "./java_examples/Calculator.java", "./java_examples/GuessingGame.java", "./java_examples/Hello.java", "./java_examples/Knight.java"]
    if len(argv) > 1:
        if len(argv) != 2:
            print("Usage: python p.py [java file path]")
            exit(1)
        java_paths = [argv[1]]

    system("antlr4 -Dlanguage=Python3 -no-listener -visitor JLexer.g4")
    system("antlr4 -Dlanguage=Python3 -no-listener -visitor JParser.g4")

    #replace("pass", "print(inspect.stack()[0][3])", "JParserListener.py", "replace.temp")
    #replace("JParserVisitor", "JVisitor", "JParserVisitor.py", "JVisitor.py", "import inspect\n")

    for java_path in java_paths:
        tmp = system("python main.py {}".format(java_path))
    
if __name__ == "__main__":
    main(argv)