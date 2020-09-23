import ast

def main():
	with open("test.py", "r") as source:
		tree = ast.parse(source.read())
	print(ast.dump(tree))
main()
