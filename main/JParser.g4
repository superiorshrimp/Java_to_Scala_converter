parser grammar JParser;

options { tokenVocab=JLexer; }

compilationUnit
    : (modifier_=modifier? classDeclaration)* EOF
    ;

classDeclaration
    : CLASS class_name=identifier classBody
    ;

identifier
    : IDENTIFIER
    ;

classBody
    : '{' classBodyDeclaration* '}'
    ;

classBodyDeclaration
    : ';'
    | modifier? memberDeclaration
    | STATIC? block
    ;

modifier
    : PUBLIC
    | PROTECTED
    | PRIVATE
    | classModifier
    | variableModifier
    | methodModifier
    ;

classModifier
    : STATIC
    ;

variableModifier
    : FINAL
    ;

methodModifier
    : STATIC
    ;

memberDeclaration
    : fieldDeclaration
    | methodDeclaration
    | constructorDeclaration
    ;

methodDeclaration
    : STATIC? (method_declaration_type=type | method_declaration_void=VOID) method_declaration_method_name=identifier parameters methodBody
    ;

methodBody
    : block
    | ';'
    ;

constructorDeclaration
    : identifier parameters constructorBody
    ;

constructorBody
    : block
    | ';'
    ;

fieldDeclaration
    : type variableDeclarators ';'
    ;

variableDeclarators
    : var_dec_1=variableDeclarator (',' var_dec_2=variableDeclarator)*
    ;

variableDeclarator
    : variableDeclaratorId ('=' variableInitializer)?
    ;

variableDeclaratorId
    : identifier ('[' ']')*
    ;

variableInitializer
    : arrayInitializer
    | expression
    ;

arrayInitializer
    : '{' (variableInitializer (',' variableInitializer)* (',')? )? '}'
    ;

parameters
    : '(' (type identifier ('[' ']')* (',' type identifier ('[' ']')*)* )? ')'
    ;

literal
    : integerLiteral
    | floatLiteral
    | CHAR_LITERAL
    | STRING_LITERAL
    | BOOL_LITERAL
    | NULL_LITERAL
    | TEXT_BLOCK
    ;

integerLiteral
    : DECIMAL_LITERAL
    | HEX_LITERAL
    | OCT_LITERAL
    | BINARY_LITERAL
    ;

floatLiteral
    : FLOAT_LITERAL
    | HEX_FLOAT_LITERAL
    ;

block
    : '{' blockStatement* '}'
    ;

blockStatement
    : localVariableDeclaration ';'
    | localTypeDeclaration
    | statement
    ;

localVariableDeclaration
    : type variableDeclarators
    ;

localTypeDeclaration
    : modifier
    ;

statement
    : IF parExpression statement (ELSE statement)?
    | FOR '(' forControl ')' statement
    | WHILE parExpression statement
    | DO statement WHILE parExpression ';'
    | RETURN expression? ';'
    | BREAK identifier? ';'
    | CONTINUE identifier? ';'
    | SWITCH parExpression '{' switchBlockStatementGroup* switchLabel* '}'
    | ';'
    | block
    | expression ';'
    ;

parExpression
    : '(' expression ')'
    ;

switchBlockStatementGroup
    : (switchLabel blockStatement)+
    ;

switchLabel
    : CASE expression ':' statement* (BREAK ';')?
    | DEFAULT ':' statement* (BREAK ';')?
    ;

expression
    : expression ('+' | '-' | '*' | '/' | '%' | '<' '<' | '>' '>' '>' | '>' '>' | '<=' | '>=' | '>' | '<' | '==' | '!=' | '&' | '^' | '|' | '&&' | '||' | '=' | '+=' | '-=' | '*=' | '/=' | '&=' | '|=' | '^=' | '>>=' | '>>>=' | '<<=' | '%=') expression
    | expression INSTANCEOF type
    | expression postfix=('++' | '--')
    | prefix=('+' | '-' | '++' | '--' | '~' | '!') expression
    | primary
    | methodCall
    | expression '.' (identifier | methodCall | THIS | NEW innerCreator)
    | NEW creator
    | '(' primitiveType ')' expression
    | expression '[' expression ']'
    ;

methodCall
    : identifier '(' expressionList? ')'
    | THIS '(' expressionList? ')'
    ;

innerCreator
    : identifier classCreatorRest
    ;

classCreatorRest
    : arguments classBody?
    ;

creator
    : createdName (arrayCreatorRest | classCreatorRest)
    ;

createdName
    : primitiveType
    | identifier ('.' identifier)*
    ;

arrayCreatorRest
    : '[' (']' ('[' ']')* arrayInitializer | expression ']' ('[' expression ']')* ('[' ']')*)
    ;

arguments
    : '(' expressionList? ')'
    ;

primary
    : literal
    | identifier
    | '(' expression ')'
    | THIS
    ;

type
    : (primitiveType | classType) ('[' ']')*
    ;

classType
    : identifier
    ;

primitiveType
    : BOOLEAN
    | CHAR
    | BYTE
    | SHORT
    | INT
    | LONG
    | FLOAT
    | DOUBLE
    ;

forControl
    : enhancedForControl
    | forInit? ';' expression? ';' expressionList?
    ;

forInit
    : localVariableDeclaration
    | expressionList
    ;

enhancedForControl
    : modifier* type variableDeclaratorId ':' expression
    ;

expressionList
    : expression (',' expression)*
    ;