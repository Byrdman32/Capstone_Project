from lark import Lark

grammar = """
    ?start: expr

    ?expr: expr "AND" term  -> and_expr
         | expr "OR" term   -> or_expr
         | term

    ?term: field OP value   -> condition
         | "(" expr ")"

    field: CNAME
    
    value: NUMBER           -> number
         | ESCAPED_STRING   -> string

    OP: ">" | "<" | ">=" | "<=" | "=" | "!="

    %import common.CNAME
    %import common.NUMBER
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='start', parser='lalr')

def valid_expression(expr):
    # Check if the expression is valid
    try:
        parser.parse(expr)
        return True
    except Exception as e:
        print(f"Invalid expression: {expr} -> {e}")
        return False