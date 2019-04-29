from compiler import MLexer


class MScanner:

    def __init__(self):

        # construct lexer
        self.lexer = MLexer()

    def tokenize(self, text):
        output = []
        self.lexer.input(text)

        while True:
            token = self.lexer.token()
            if not token:
                break
            token.columnno = token.lexpos - text.rfind('\n', 0, token.lexpos)
            output.append(token)

        return output
