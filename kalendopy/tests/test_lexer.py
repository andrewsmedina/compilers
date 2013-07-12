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
