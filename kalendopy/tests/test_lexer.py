from toy import lexer


def test_equal():
    result = lexer.lex("=")
    token = result.next()
    assert "=" == token.value
    assert "EQUAL" == token.name
