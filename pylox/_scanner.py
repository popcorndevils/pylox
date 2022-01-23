from ._token import Token
from ._tokentype import TokenType

class Scanner:
    def __init__(self, source):
        self._source = source
        self._tokens = []
        self._src_len = len(source)
        self._start = 0
        self._current = 0
        self._line = 1

        self._scan_source()

    @property
    def is_end(self):
        return self._current >= self._src_len

    @property
    def tokens(self):
        return self._tokens

    def _scan_source(self):
        """
        Scan code and generate tokens.
        """
        while not self.is_end:
            self._start = self._current
            _token = self._get_next()

            if _token is not None:
                self._tokens.append(_token)

        self._tokens.append(Token(TokenType.EOF))

    def _advance(self):
        _output = self._source[self._current]
        self._current += 1
        return _output

    def _get_lexeme(self):
        return self._source[self._start: self._current]

    def _peek(self, skip = 0):
        return self._source[self._current + skip]

    def _get_string(self):
        while self._peek() != "\"":
            self._advance()

        self._advance()
        _value = self._source[self._start + 1: self._current - 1]
        return _value

    def _match(self, character, skip = 0):
        c = self._source[self._current + skip]
        if c == character:
            self._current += 1
            return True
        return False

    def _get_next(self):
        c = self._advance()
        if c == "\"":
            _value = self._get_string()
            _lexeme = self._get_lexeme()
            return Token(TokenType.STRING, _lexeme, _value)
        elif c == ";":
            return Token(TokenType.SEMICOLON, self._get_lexeme())
        elif c == "=":
            if self._match("="):
                return Token(TokenType.EQUAL_EQUAL, self._get_lexeme())
            return Token(TokenType.EQUAL, self._get_lexeme())
        elif c in Token.WHITE_SPACE:
            return None
        else:
            return Token(TokenType.BANG, self._get_lexeme())
