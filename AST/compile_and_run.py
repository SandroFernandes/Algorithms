import ast


def simple_expression():
    # Create an AST for a simple expression
    node = ast.Expression(ast.BinOp(ast.Num(5), ast.Add(), ast.Num(3)))

    # Fill in missing lineno and col_offset fields
    ast.fix_missing_locations(node)

    # Compile the AST into bytecode
    bytecode = compile(node, filename='<ast>', mode='eval')

    # Execute the bytecode
    result = eval(bytecode)

    # Outputs: 8
    return result


def function_example():
    # Create an AST for a simple function
    function = ast.FunctionDef(
        name='add',
        args=ast.arguments(
            posonlyargs=[],
            args=[
                ast.arg(arg='x', annotation=None),
                ast.arg(arg='y', annotation=None)
            ],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[
            ast.Return(
                value=ast.BinOp(
                    left=ast.Name(id='x', ctx=ast.Load()),
                    op=ast.Add(),
                    right=ast.Name(id='y', ctx=ast.Load())
                )
            )
        ],
        decorator_list=[],
        returns=None
    )

    # Create a module to contain the function
    module = ast.Module(body=[function], type_ignores=[])

    # Fill in missing lineno and col_offset fields
    ast.fix_missing_locations(module)

    # Compile the AST into bytecode
    bytecode = compile(module, filename='<ast>', mode='exec')

    # Execute the bytecode to define the function
    exec(bytecode, globals())


def loop_example():
    # Create an AST for a simple for loop
    loop = ast.For(
        target=ast.Name(id='i', ctx=ast.Store()),
        iter=ast.Call(
            func=ast.Name(id='range', ctx=ast.Load()),
            args=[ast.Num(15)],
            keywords=[]
        ),
        body=[ast.Expr(
            value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()),
                args=[ast.Name(id='i', ctx=ast.Load())],
                keywords=[]
            )
        )],
        orelse=[]
    )

    # Create a module to contain the loop
    module = ast.Module(body=[loop], type_ignores=[])

    # Fill in missing lineno and col_offset fields
    ast.fix_missing_locations(module)

    # Compile the AST into bytecode
    bytecode = compile(module, filename='<ast>', mode='exec')

    # Execute the bytecode
    exec(bytecode)


if __name__ == '__main__':
    simple_expression()
    function_example()
    loop_example()
