from toy import lexer


def test_equal():
    result = lexer.lex("=")
    token = result.next()
    assert "=" == token.value
    assert "EQUAL" == token.name


def test_plus():
    result = lexer.lex("+")
    token = result.next()
    assert "+" == token.value
    assert "PLUS" == token.name


def test_minus():
    result = lexer.lex("-")
    token = result.next()
    assert "-" == token.value
    assert "MINUS" == token.name


def test_def():
    result = lexer.lex("def")
    token = result.next()
    assert "def" == token.value
    assert "DEF" == token.name


def test_lparen():
    result = lexer.lex("(")
    token = result.next()
    assert "(" == token.value
    assert "LPAREN" == token.name


def test_rparen():
    result = lexer.lex(")")
    token = result.next()
    assert ")" == token.value
    assert "RPAREN" == token.name


def test_number():
    result = lexer.lex("42")
    token = result.next()
    assert "42" == token.value
    assert "NUMBER" == token.name


def test_name():
    result = lexer.lex("age")
    token = result.next()
    assert "age" == token.value
    assert "NAME" == token.name
