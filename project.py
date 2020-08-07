from lolcode_parser import build_parser, parse_LOLcode
from symbol_table import SymbolTable
from lmaocode_compiler import compile_ROFLcode_from_LMAOcode
from interpreter import interpret

def convert_compiled_code_to_str(compiled_code):
    lines = ''
    for row in compiled_code:
        line = ''
        for elem in row:
            line += str(elem) + ' '
        line += '\n'
        lines += line
    return lines

def generate_LMAOcode_from_LOLcode(lolcode_str):
    parse_tree = parse_LOLcode(lolcode_str)
    print("Parse Tree:")
    print(parse_tree)
    print()

    symbol_table = SymbolTable()
    compiled_code = []
    parse_tree.compile(symbol_table, compiled_code)
    
    lmaocode_str = convert_compiled_code_to_str(compiled_code)
    return lmaocode_str

def generate_ROFLcode_from_LOLcode(lolcode_str):
    lmaocode_str = generate_LMAOcode_from_LOLcode(lolcode_str)
    return compile_ROFLcode_from_LMAOcode(lmaocode_str)

SEED = 0
STANDARD_INPUT = "abcdef"

lolcode_str = r"""
HAI 1.450
VISIBLE WHATEVR
HOW IZ I factorial YR arg ITZ A NUMBR MKAY
	O RLY? SAEM arg AN 1
	YA RLY
		FOUND YR 1
	NO WAI
		FOUND YR PRODUKT OF arg AN I IZ factorial YR DIFF OF arg AN 1 MKAY
	OIC
IF U SAY SO ITZ A NUMBR
VISIBLE I IZ factorial YR 3 MKAY
VISIBLE WHATEVR
KTHXBYE
"""
lmaocode = generate_LMAOcode_from_LOLcode(lolcode_str)
print("Generated LMAOcode:")
print(lmaocode)
executed_lmao_output = interpret(lmaocode, 'LMAOcode', seed=SEED, standard_input=STANDARD_INPUT)
expected_output = "49\n5\n97\n"
print(expected_output == executed_lmao_output)
print(""
      ""
      ""
      "")
roflcode = generate_ROFLcode_from_LOLcode(lolcode_str)
print("Generated ROFLcode:")
print(roflcode)
executed_rofl_output = interpret(roflcode, 'ROFLcode', seed=SEED, standard_input=STANDARD_INPUT)
print(expected_output == executed_rofl_output)
print(executed_rofl_output)

