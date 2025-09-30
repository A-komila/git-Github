# phase 1: from infix to postfix
# expr  term rest
# rest  + term { print(‘+’) } rest
# rest  - term { print(‘-’) } rest
# rest  ε
# term  0 { print(‘0’) }
# term  1 { print(‘1’) }
# …
# term  9 { print(‘9’) }




input_text = '1-5+9'
input_index = 0
lookahead = ''


def lexen():
    global input_index
    while True:
        if input_index < len(input_text):
            t = input_text[input_index]
            input_index += 1
            return t
        else:
            return 'EOF'


def match(token):
    global lookahead
    if (lookahead == token):
        lookahead = lexen()
    else:
        error()


def error():
    print('Syntax error')

def main():
    global lookahead
    # lookahead = lexen()
    # expr()
    # if lookahead != 'EOF':
    #     error()
    lookahead = lexen()
    expr()


def expr():
    # expr  term rest
    # rest  + term { print(‘+’) } rest
    # rest  - term { print(‘-’) } rest
    # rest  ε
    # term  0 { print(‘0’) }
    # term  1 { print(‘1’) }
    # …
    # term  9 { print(‘9’) }
    term()
    rest()


def rest():
    global lookahead
    if lookahead == '+':
        match('+')
        term()
        print('+', end=' ')
        rest()
    elif lookahead == '-':
        match('-')
        term()
        print('-', end=' ')
        rest()


def term():
    global lookahead
    if lookahead.isdigit():
        print(lookahead, end=' ')
        match(lookahead)
    else:
        error()

if __name__ == '__main__':
    main()
