import TokenMaker
import SyntaxAnalyzer

TokenMaker.process_file("input.txt")
tokens = TokenMaker.token_maker()
TokenMaker.save_output("output.txt", tokens)

SyntaxAnalyzer.process_file("output.txt")
SyntaxAnalyzer.Main()
