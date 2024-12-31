txtfile = []
errors = []

def Main():
    if lookahead in {'Clause_TK', 'F-loop_TK', 'W-loop_TK', 'Define_TK', 'ID_TK'}:
        syntax()
    elif lookahead in {'Int_TK', 'Float_TK', 'String_TK'}:
        assignment()

def if_syntax():
    if lookahead == "another_Clause_TK":
        match("another_Clause_TK")
        match("Open-Parantese_TK")
        cond()
        match("Close-Parantese_TK")
        match("Open-Bracket_TK")
        Main()
        match("Close-Bracket_TK")
        if_syntax()
        Main()
    elif lookahead == "end_TK":
        match("end_TK")
        match("Open-Bracket_TK")
        Main()
        match("Close-Bracket_TK")
    return

def syntax():
    if lookahead == "Clause_TK":
        match("Clause_TK")
        match("Open-Parantese_TK")
        cond()
        match("Close-Parantese_TK")
        match("Open-Bracket_TK")
        Main()
        match("Close-Bracket_TK")
        if_syntax()
        Main()
    elif lookahead == "F-loop_TK":
        match("F-loop_TK")
        match("Open-Parantese_TK")
        match("From_TK")
        if lookahead.isdigit():
            match(lookahead)
        else:
            error_handler(f"Expected digit after 'From_TK', found '{lookahead}'")
        match("To_TK")
        if lookahead.isdigit():
            match(lookahead)
        else:
            error_handler(f"Expected digit after 'To_TK', found '{lookahead}'")
        match("By_TK")
        cond()
        match("Close-Parantese_TK")
        match("Open-Bracket_TK")
        Main()
        match("Close-Bracket_TK")
        Main()
    elif lookahead == "W-loop_TK":
        match("W-loop_TK")
        match("Open-Parantese_TK")
        match('From_TK')
        if lookahead.isdigit():
            match(lookahead)
        else:
            error_handler(f"Expected digit after 'From_TK', found '{lookahead}'")
        match('To_TK')
        if lookahead.isdigit():
            match(lookahead)
        else:
            error_handler(f"Expected digit after 'From_TK', found '{lookahead}'")
        match('Close-Parantese_TK')
        match('Open-Bracket_TK')
        Main()
        match('Close-Bracket_TK')
        Main()

    elif lookahead == "Define_TK":
        match("Define_TK")
        match("ID_TK")
        match("Open-Parantese_TK")
        arg()
        match("Close-Parantese_TK")
        match("Open-Bracket_TK")
        Main()
        match("Close-Bracket_TK")
        Main()
    elif lookahead == "ID_TK":
        match("ID_TK")
        if lookahead == "Open-Parantese_TK":
            match("Open-Parantese_TK")
            argplus()
            match("Close-Parantese_TK")
            Main()
        elif lookahead in {"|Set|_TK", "|Div|_TK", "|Multi|_TK", "|Minus|_TK", "|Add|_TK"}:
            operator()

def stmnt():
    if lookahead == "ID_TK":
        match("ID_TK")
        if lookahead == '|Set|_TK':
            match("|Set|_TK")
        else:
            error_handler(f"Expected |set|_TK after Identifier, found '{lookahead}'")
        L()

def L():
    if lookahead == "ID_TK":
        match("ID_TK")
        Z()
    elif lookahead.isdigit():
        match(lookahead)
        Z()
    else:
        error_handler(f"Unexpected token '{lookahead}' in L")

def Y():
    if lookahead == "ID_TK":
        match("ID_TK")
    elif lookahead.isdigit():
        match(lookahead)
    else:
        error_handler(f"Unexpected token '{lookahead}' in Y")

def Z():
    if lookahead in {"|Set|_TK", "|Div|_TK", "|Multi|_TK", "|Minus|_TK", "|Add|_TK"}:
        operation()
        Y()
    return

def arg():
    if lookahead == "ID_TK":
        match("ID_TK")
        arg()
    elif lookahead.isdigit():
        match(lookahead)
        arg()
    return

def argplus():
    if lookahead == "ID_TK":
        match("ID_TK")
        argplus()
    elif lookahead.isdigit():
        match(lookahead)
        argplus()
    return

def comparison():
    if lookahead in {"Smaller_TK", "Bigger_TK", "|Value|_TK"}:
        match(lookahead)
    else:
        error_handler(f"Expected comparison operator, found '{lookahead}'")

def cond():
    if lookahead == "ID_TK" or lookahead.isdigit():
        match(lookahead)
        if lookahead in {"Smaller_TK", "Bigger_TK", "|Value|_TK"}:
            comparison()
            if lookahead == "ID_TK" or lookahead.isdigit():
                match(lookahead)
            else:
                error_handler(f"Expected identifier or number after comparison operator, found '{lookahead}'")
        else:
            error_handler(f"Expected comparison operator, found '{lookahead}'")
    elif lookahead in {"True_TK", "False_TK"}:
        match(lookahead)
    else:
        error_handler(f"Unexpected token '{lookahead}' in condition")

def operator():
    if lookahead in {"|Set|_TK", "|Div|_TK", "|Multi|_TK", "|Minus|_TK", "|Add|_TK"}:
        operation()
        Y()
    elif lookahead.isdigit():
        match(lookahead)
        operation()
        Y()
    else:
        error_handler(f"Unexpected token '{lookahead}' in operator")

def assignment():
    if lookahead in {"Int_TK", "Float_TK", "String_TK"}:
        match(lookahead)
        stmnt()
    else:
        error_handler(f"Unexpected token '{lookahead}' in assignment")

def operation():
    if lookahead in {"|Set|_TK", "|Div|_TK", "|Multi|_TK", "|Minus|_TK", "|Add|_TK"}:
        match(lookahead)
    else:
        error_handler(f"Expected operation, found '{lookahead}'")

def get_next_token():
    global index, lookahead
    if index < len(txtfile):
        lookahead = txtfile[index]
        index += 1
    else:
        lookahead = None

def match(expected_token):
    if lookahead == expected_token:
        get_next_token()
        return True
    else:
        error_message = f"Syntax Error: Expected '{expected_token}' but found '{lookahead}' at position {index - 1}"
        error_handler(error_message)
        return False

def error_handler(message):
    errors.append(message)

def process_file(filename):
    global txtfile, index, lookahead
    with open(filename, 'r') as file:
        content = file.read()
        txtfile = content.split()
    index = 0
    get_next_token()
    Main()
    if errors:
        print("\nErrors encountered during parsing:")
        for error in errors:
            print(error)
    else:
        print("Parsing completed successfully without errors.")
