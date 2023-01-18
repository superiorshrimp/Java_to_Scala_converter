import sys
from antlr4 import *
from JLexer import JLexer
from JParser import JParser
from JVisitor import JVisitor

#write fucntion which savessting to a file
def writeToFile(fileName, data):
    with open(fileName, 'w') as f:
        f.write(data)

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JParser(stream)
    tree = parser.compilationUnit()

    visitor = JVisitor()
    result = visitor.visitCompilationUnit(tree)
    writeToFile("result.scala", result)
    print(result)

if __name__ == '__main__':
    main(sys.argv)