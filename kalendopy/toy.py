from rply import LexerGenerator


lg = LexerGenerator()

lg.add("PLUS", r"\+")
lg.add("MINUS", r"-")
lg.add("EQUAL", r"\=")
lg.add("DEF", r"def")
lg.add("LPAREN", r"\(")
lg.add("RPAREN", r"\)")
lg.add("NUMBER", r"\d+")
lg.add("NAME", r"\w+")

lg.ignore(r"\s+")

lexer = lg.build()
