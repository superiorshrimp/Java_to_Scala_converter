import inspect
# Generated from JParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JParser import JParser
else:
    from JParser import JParser

# This class defines a complete generic visitor for a parse tree produced by JParser.
# inspect.stack()[0][3] - getting method name from within the method
def print_methods(ctx, method_name):
    print("methods of " + method_name)
    print([method_name for method_name in dir(ctx) if callable(getattr(ctx, method_name)) and not '__' in method_name])

def print_attributes(ctx, method_name):
    print("attributes of " + method_name)
    print([attribute_name for attribute_name in dir(ctx) if not callable(getattr(ctx, attribute_name)) and not '__' in attribute_name])

def capitalize(s):
        return s[0].upper() + s[1:]

class JVisitor(ParseTreeVisitor):

    def __init__(self) -> None:
        super().__init__()
        depth = 0 # number of tabs to print

    def inc_depth():
        depth += 1

    def dec_depth():
        depth -= 1

    def visitTerminal(self, ctx): #EOF handle
        return '\n'

    # Visit a parse tree produced by JParser#compilationUnit.
    def visitCompilationUnit(self, ctx:JParser.CompilationUnitContext):
        s = ""
        for classDeclaration in ctx.classDeclaration(): #if czy none
            s += self.visit(classDeclaration)
        return s

    # Visit a parse tree produced by JParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JParser.ClassDeclarationContext):
        #print_methods(ctx, inspect.stack()[0][3])
        #print_attributes(ctx, inspect.stack()[0][3])
        return "object " + ctx.class_name.getText() + self.visit(ctx.classBody()) #ważne żebym dał funkcje nie atrybut


    # Visit a parse tree produced by JParser#identifier.
    def visitIdentifier(self, ctx:JParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#classBody.
    def visitClassBody(self, ctx:JParser.ClassBodyContext):
        s = "{\n"
        for classBodyDeclaration in ctx.classBodyDeclaration(): s += self.visit(classBodyDeclaration)
        return s + '\n}\n'


    # Visit a parse tree produced by JParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:JParser.ClassBodyDeclarationContext):
        if ctx.SEMI() is not None: return ""
        elif ctx.memberDeclaration() is not None: return self.visit(ctx.memberDeclaration())
        else: return self.visit(ctx.block())


    # Visit a parse tree produced by JParser#modifier.
    def visitModifier(self, ctx:JParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#classModifier.
    def visitClassModifier(self, ctx:JParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#variableModifier.
    def visitVariableModifier(self, ctx:JParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#methodModifier.
    def visitMethodModifier(self, ctx:JParser.MethodModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:JParser.MemberDeclarationContext):
        if ctx.methodDeclaration() is not None:
            return self.visit(ctx.methodDeclaration())#jak jest ?
        elif ctx.fieldDeclaration() is not None:
            return self.visit(ctx.fieldDeclaration())
        else: return self.visit(ctx.constructorDeclaration())


    # Visit a parse tree produced by JParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:JParser.MethodDeclarationContext):
        #print_attributes(ctx, inspect.stack()[0][3])
        #print_methods(ctx, inspect.stack()[0][3])

        if ctx.VOID() is not None: t = ': Unit = '
        else: t = ': {} = '.format(capitalize(ctx.method_declaration_type.getText()))
        s = "def " + ctx.method_declaration_method_name.getText() + self.visit(ctx.parameters()) + t + self.visit(ctx.methodBody())
        return s


    # Visit a parse tree produced by JParser#methodBody.
    def visitMethodBody(self, ctx:JParser.MethodBodyContext):
        if ctx.SEMI() is not None: return ""
        else: return self.visit(ctx.block())


    # Visit a parse tree produced by JParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:JParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#constructorBody.
    def visitConstructorBody(self, ctx:JParser.ConstructorBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:JParser.FieldDeclarationContext):
        #print_attributes(ctx, inspect.stack()[0][3])
        #print_methods(ctx, inspect.stack()[0][3])

        #print("TMP:",ctx.variableDeclarators().getText())



        type = ctx.type_().getText()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:JParser.VariableDeclaratorsContext):
        #get string with =, remove it and return tuple with value left of = and right of =
        def get_value(s):
            if '=' in s:
                s = s.split('=')
                return s[0], s[1]
            else: return s, None
        #print_attributes(ctx, inspect.stack()[0][3])
        #print_methods(ctx, inspect.stack()[0][3])
        #print("TMP:", ctx.var_dec_1.getText())
        #print("ASDASDASD", type(ctx.var_dec_2))
        variables_declarations = []
        for i in range(len(ctx.variableDeclarator())):
            variables_declarations.append(get_value(ctx.variableDeclarator()[i].getText()))
        return variables_declarations
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:JParser.VariableDeclaratorContext):
        #print_attributes(ctx, inspect.stack()[0][3])
        #print_methods(ctx, inspect.stack()[0][3])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:JParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#variableInitializer.
    def visitVariableInitializer(self, ctx:JParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:JParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#parameters.
    def visitParameters(self, ctx:JParser.ParametersContext): #TODO: dodać []
        def remove_suffix(s): #usuwa [] z typu, zwraca typ bez nich i ilość []
            i = 0
            while s[-1] == '[' or s[-1] == ']':
                i += 1
                s = s[:-1]
            return s, i//2

        result = '('
        for i in range(len(ctx.type_())):
            type, array_dims = remove_suffix(ctx.type_()[i].getText())
            arg_name = ctx.identifier()[i].getText()
            mainType = type
            if array_dims != 0:
                mainType = 'Array'
            result += arg_name + ': ' + capitalize(mainType)
            for _ in range(array_dims):
                result += f'[{capitalize(type)}]'
            result += ', '
        if len(ctx.type_()) != 0: result = result[:-2]
        return result + ')'


    # Visit a parse tree produced by JParser#literal.
    def visitLiteral(self, ctx:JParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:JParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#floatLiteral.
    def visitFloatLiteral(self, ctx:JParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#block.
    def visitBlock(self, ctx:JParser.BlockContext):
        s = '{\n'
        for blockStatement in ctx.blockStatement():
            s += self.visit(blockStatement)
        return s + '\n}'


    # Visit a parse tree produced by JParser#blockStatement.
    def visitBlockStatement(self, ctx:JParser.BlockStatementContext):
        if ctx.localTypeDeclaration() is not None: return self.visit(ctx.localTypeDeclaration())
        elif ctx.localVariableDeclaration() is not None: return self.visit(ctx.localVariableDeclaration())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:JParser.LocalVariableDeclarationContext):
        type = ctx.type_().getText()
        result = ""
        variables_declarated = self.visit(ctx.variableDeclarators())
        for var in variables_declarated:
            name = var[0]
            value = None
            if var[1] is None:
                value = '_'
            else:
                value = var[1]
            result += f"var {name}: {capitalize(type)} = {value}\n"
        return result
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#localTypeDeclaration.
    def visitLocalTypeDeclaration(self, ctx:JParser.LocalTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#statement.
    def visitStatement(self, ctx:JParser.StatementContext): #TODO
        # check if string has prefix "System.out.println"
        def is_print(s):
            return s[:18] == "System.out.println"

        def get_brackets_content(s):
            return s[s.find("(")+1:s.find(")")]

        if ctx.IF() is not None: return 'if'
        elif ctx.FOR() is not None: return 'for'
        elif ctx.DO() is not None: return 'do'
        elif ctx.WHILE() is not None: return 'while'
        elif ctx.RETURN() is not None: return 'return '
        elif ctx.BREAK() is not None: return 'break '
        elif ctx.CONTINUE() is not None: return 'continue '
        elif ctx.SWITCH() is not None: return 'switch'
        elif ctx.block() is not None: return self.visit(ctx.block())
        elif ctx.expression() is not None:
            if is_print(ctx.expression().getText()):
                return "println(" + get_brackets_content(ctx.expression().getText()) + ")\n"
            expression = ctx.expression().getText() + "\n"
            return expression
        else: return "" #SEMI


    # Visit a parse tree produced by JParser#parExpression.
    def visitParExpression(self, ctx:JParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:JParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#switchLabel.
    def visitSwitchLabel(self, ctx:JParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#expression.
    def visitExpression(self, ctx:JParser.ExpressionContext): #TODO
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#innerCreator.
    def visitInnerCreator(self, ctx:JParser.InnerCreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#classCreatorRest.
    def visitClassCreatorRest(self, ctx:JParser.ClassCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#creator.
    def visitCreator(self, ctx:JParser.CreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#createdName.
    def visitCreatedName(self, ctx:JParser.CreatedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#arrayCreatorRest.
    def visitArrayCreatorRest(self, ctx:JParser.ArrayCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#arguments.
    def visitArguments(self, ctx:JParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#primary.
    def visitPrimary(self, ctx:JParser.PrimaryContext):
        #print_methods(ctx, inspect.stack()[0][3])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#type.
    def visitType(self, ctx:JParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#classType.
    def visitClassType(self, ctx:JParser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#primitiveType.
    def visitPrimitiveType(self, ctx:JParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#forControl.
    def visitForControl(self, ctx:JParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#forInit.
    def visitForInit(self, ctx:JParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx:JParser.EnhancedForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JParser#expressionList.
    def visitExpressionList(self, ctx:JParser.ExpressionListContext):
        return self.visitChildren(ctx)



del JParser