import ast
import dis
from math import log


def show_code(code):
    bytecode = dis.Bytecode(code)
    print("Code:")
    for instr in bytecode:
        print(instr.opname, instr.argrepr)


# Create an AST representing a simple addition operation
node = ast.parse("2 + 3 ** 2 + log(10) +", mode="eval")

# Compile the AST into a code object
compiled_code = compile(node, filename="<ast>", mode="eval")

# Show the code
show_code(compiled_code)

# Evaluate the code object in the Python interpreter
result = eval(compiled_code)

# Output: 5
print(result)
