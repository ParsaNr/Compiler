txtfile = []
output = []
symbol_table = dict()

def Identifire(ch):
    flag = True
    end_pos = len(ch) - 1
    state = 1
    while (True):
        match (state):
            case 1:
                if (ch[0] == '_'):
                    state = 2
                else:
                    state = 4
            case 2:
                for i in range(1, end_pos - 1):
                    char = ch[i]
                    if ((char >= 'a' and char <= "z") or (char >= "A" and char <= "Z") or char == "_" or (char >= "1" and char <= "9")):
                        pass
                    else:
                        return None
                state = 3
            case 3:
                if (ch[end_pos] == "_"):
                    flag = False
                    return "ID"
                else:
                    state = 4
            case 4:
                return None

def clause(ch): 
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'c':
                    state = 2
                else:
                    flag = False
                    state = 8 #تله

            case 2:
                if ch[1] == 'l':
                    state = 3
                else:
                    flag = False
                    state = 8

            case 3:
                if ch[2] == 'a':
                    state = 4
                else:
                    flag = False
                    state = 8
        
            case 4:
                if ch[3] == 'u':
                    state = 5
                else:
                    flag = False
                    state = 8
            case 5:
                if ch[4] == 's':
                    state = 6
                else:
                    flag = False
                    state = 8
            case 6:
                if ch[5] == 'e':
                    state = 7
                else:
                    state = 8
            case 7:
                try:
                    if (ch[6] != " "):
                        return None
                except:
                    return "Clause"
            case 8:
                None

def Int(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'i':
                    state = 2
                else:
                    return None

            case 2:
                if ch[1] == 'n':
                    state = 3
                else:
                    return None

            case 3:
                if ch[2] == 't':
                    state = 4
                else:
                    return None
            case 4:
                try:
                    if (ch[3] != " "):
                        return None
                except:
                    return "Int"

def value(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == '|':
                    state = 2
                else:
                    flag = False
                    state = 9
            case 2:
                if ch[1] == 'v':
                    state = 3
                else:
                    flag = False
                    state = 9

            case 3:
                if ch[2] == 'a':
                    state = 4
                else:
                    flag = False
                    state = 9

            case 4:
                if ch[3] == 'l':
                    state = 5
                else:
                    flag = False
                    state = 9
            case 5:
                if ch[4] == 'u':
                    state = 6
                else:
                    flag = False
                    state = 9
            case 6:
                if ch[5] == 'e':
                    state = 7
                else:
                    state = 9
            case 7:
                if ch[6] == '|':
                    state = 8
                else:
                    state = 9
            case 8:
                try:
                    if (ch[7] != " "):
                        return None
                except:
                    return "|Value|"
            case 9:
                None

def floop(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'f':
                    state = 2
                else:
                    flag = False
                    state = 8
            case 2:
                if ch[1] == '-':
                    state = 3
                else:
                    flag = False
                    state = 8
            case 3:
                if ch[2] == 'l':
                    state = 4
                else:
                    flag = False
                    state = 8
            case 4:
                if ch[3] == 'o':
                    state = 5
                else:
                    flag = False
                    state = 8
            case 5:
                if ch[4] == 'o':
                    state = 6
                else:
                    flag = False
                    state = 8
            case 6:
                if ch[5] == 'p':
                    state = 7
                else:
                    state = 8
            case 7:
                try:
                    if (ch[6] != " "):
                        return None
                except:
                    return "F-loop"
            case 8:
                None

def To(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 't':
                    state = 2
                else:
                    return None

            case 2:
                if ch[1] == 'o':
                    state = 3
                else:
                    return None

            case 3:
                try:
                    if (ch[2] != " "):
                        return None
                except:
                    return "To"

def end(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'e':
                    state = 2
                else:
                    return None

            case 2:
                if ch[1] == 'n':
                    state = 3
                else:
                    return None
            case 3:
                if ch[2] == 'd':
                    state = 4
                else:
                    return None

            case 4:
                try:
                    if (ch[3] != " "):
                        return None
                except:
                    return "end"

def another_Clause(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'a':
                    state = 2
                else:
                    flag = False
                    state = 16

            case 2:
                if ch[1] == 'n':
                    state = 3
                else:
                    flag = False
                    state = 16

            case 3:
                if ch[2] == 'o':
                    state = 4
                else:
                    flag = False
                    state = 16
        
            case 4:
                if ch[3] == 't':
                    state = 5
                else:
                    flag = False
                    state = 16
            case 5:
                if ch[4] == 'h':
                    state = 6
                else:
                    flag = False
                    state = 16
            case 6:
                if ch[5] == 'e':
                    state = 7
                else:
                    state = 16
            case 7:
                if ch[6] == 'r':
                    state = 8
                else:
                    state = 16
            case 8:
                if ch[7] == '_':
                    state = 9
                else:
                    state = 16
            case 9:
                if ch[8] == 'C':
                    state = 10
                else:
                    state = 16 
            case 10:
                if ch[9] == 'l':
                    state = 11
                else:
                    state = 16    
            case 11:
                if ch[10] == 'a':
                    state = 12
                else:
                    state = 16   
            case 12:
                if ch[11] == 'u':
                    state = 13
                else:
                    state = 16 
            case 13:
                if ch[12] == 's':
                    state = 14
                else:
                    state = 16 
            case 14:
                if ch[13] == 'e':
                    state = 15
                else:
                    state = 16 
            case 15:
                try:
                    if (ch[14] != " "):
                        return None
                except:
                    return "another_Clause_TK"
            case 16:
                return None

def by(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'b':
                    state = 2
                else:
                    return None

            case 2:
                if ch[1] == 'y':
                    state = 3
                else:
                    return None

            case 3:
                try:
                    if (ch[2] != " "):
                        return None
                except:
                    return "By"

def From(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'f':
                    state = 2
                else:
                    flag = False
                    state = 6

            case 2:
                if ch[1] == 'r':
                    state = 3
                else:
                    flag = False
                    state = 6
            case 3:
                if ch[2] == 'o':
                    state = 4
                else:
                    flag = False
                    state = 6

            case 4:
                if ch[3] == 'm':
                    state = 5
                else:
                    state = 6

            case 5:
                try:
                    if (ch[4] != " "):
                        return None
                except:
                    return "From"
            case 6:
                None

def wloop(ch):
    end_pos = len(ch) - 1
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'w':
                    state = 2
                else:
                    flag = False
                    state = 8

            case 2:
                if ch[1] == '-':
                    state = 3
                else:
                    flag = False
                    state = 8
            case 3:
                if ch[2] == 'l':
                    state = 4
                else:
                    flag = False
                    state = 8
            case 4:
                if ch[3] == 'o':
                    state = 5
                else:
                    flag = False
                    state = 8
            case 5:
                if ch[4] == 'o':
                    state = 6
                else:
                    flag = False
                    state = 8
            case 6:
                if ch[5] == 'p':
                    state = 7
                else:
                    state = 8

            case 7:
                try:
                    if (ch[6] != " "):
                        return None
                except:
                    return "W-loop"
            case 8:
                None

def define(ch):
    end_pos = len(ch) - 1
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'd':
                    state = 2
                else:
                    flag = False
                    state = 8

            case 2:
                if ch[1] == 'e':
                    state = 3
                else:
                    flag = False
                    state = 8

            case 3:
                if ch[2] == 'f':
                    state = 4
                else:
                    flag = False
                    state = 8
        
            case 4:
                if ch[3] == 'i':
                    state = 5
                else:
                    flag = False
                    state = 8
            case 5:
                if ch[4] == 'n':
                    state = 6
                else:
                    flag = False
                    state = 8

            case 6:
                if ch[5] == 'e':
                    state = 7
                else:
                    state = 8
            case 7:
                try:
                    if (ch[6] != " "):
                        return None
                except:
                    return "Define"
            case 8:
                None

def float(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'f':
                    state = 2
                else:
                    flag = False
                    state = 7

            case 2:
                if ch[1] == 'l':
                    state = 3
                else:
                    flag = False
                    state = 7

            case 3:
                if ch[2] == 'o':
                    state = 4
                else:
                    flag = False
                    state = 7
            case 4:
                if ch[3] == 'a':
                    state = 5
                else:
                    flag = False
                    state = 7
            case 5:
                if ch[4] == 't':
                    state = 6
                else:
                    state = 7
            case 6:
                try:
                    if (ch[5] != " "):
                        return None
                except:
                    return "Float"

            case 7:
                None

def With(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 'w':
                    state = 2
                else:
                    flag = False
                    state = 6

            case 2:
                if ch[1] == 'i':
                    state = 3
                else:
                    flag = False
                    state = 6
            case 3:
                if ch[2] == 't':
                    state = 4
                else:
                    flag = False
                    state = 6

            case 4:
                if ch[3] == 'h':
                    state = 5
                else:
                    state = 6

            case 5:
                try:
                    if (ch[4] != " "):
                        return None
                except:
                    return "With"
            case 6:
                None

def String(ch): 
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == 's':
                    state = 2
                else:
                    flag = False
                    state = 8 

            case 2:
                if ch[1] == 't':
                    state = 3
                else:
                    flag = False
                    state = 8

            case 3:
                if ch[2] == 'r':
                    state = 4
                else:
                    flag = False
                    state = 8
        
            case 4:
                if ch[3] == 'i':
                    state = 5
                else:
                    flag = False
                    state = 8
            case 5:
                if ch[4] == 'n':
                    state = 6
                else:
                    flag = False
                    state = 8
            case 6:
                if ch[5] == 'g':
                    state = 7
                else:
                    state = 8
            case 7:
                try:
                    if (ch[6] != " "):
                        return None
                except:
                    return "String"
            case 8:
                None

def subtraction(ch): 
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == '|':
                    state = 2
                else:
                    flag = False
                    state = 9

            case 2:
                if ch[1] == 'm':
                    state = 3
                else:
                    flag = False
                    state = 9

            case 3:
                if ch[2] == 'i':
                    state = 4
                else:
                    flag = False
                    state = 9
        
            case 4:
                if ch[3] == 'n':
                    state = 5
                else:
                    flag = False
                    state = 9
            case 5:
                if ch[4] == 'u':
                    state = 6
                else:
                    flag = False
                    state = 9
            case 6:
                if ch[5] == 's':
                    state = 7
                else:
                    state = 9
            case 7:
                if ch[6] == '|':
                    state = 8
                else:
                    state = 9
            case 8:
                try:
                    if (ch[7] != " "):
                        return None
                except:
                    return "|Minus|"
            case 9:
                None

def multiplication(ch): 
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == '|':
                    state = 2
                else:
                    flag = False
                    state = 9

            case 2:
                if ch[1] == 'm':
                    state = 3
                else:
                    flag = False
                    state = 9

            case 3:
                if ch[2] == 'u':
                    state = 4
                else:
                    flag = False
                    state = 9
        
            case 4:
                if ch[3] == 'l':
                    state = 5
                else:
                    flag = False
                    state = 9
            case 5:
                if ch[4] == 't':
                    state = 6
                else:
                    flag = False
                    state = 9
            case 6:
                if ch[5] == 'i':
                    state = 7
                else:
                    state = 9
            case 7:
                if ch[6] == '|':
                    state = 8
                else:
                    state = 9
            case 8:
                try:
                    if (ch[7] != " "):
                        return None
                except:
                    return "|Multi|"
            case 9:
                None

def division(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == '|':
                    state = 2
                else:
                    flag = False
                    state = 7

            case 2:
                if ch[1] == 'd':
                    state = 3
                else:
                    flag = False
                    state = 7

            case 3:
                if ch[2] == 'i':
                    state = 4
                else:
                    flag = False
                    state = 7
            case 4:
                if ch[3] == 'v':
                    state = 5
                else:
                    flag = False
                    state = 7
            case 5:
                if ch[4] == '|':
                    state = 6
                else:
                    state = 7
            case 6:
                try:
                    if (ch[5] != " "):
                        return None
                except:
                    return "|Div|"

            case 7:
                None

def Add(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == '|':
                    state = 2
                else:
                    flag = False
                    state = 7

            case 2:
                if ch[1] == 'a':
                    state = 3
                else:
                    flag = False
                    state = 7

            case 3:
                if ch[2] == 'd':
                    state = 4
                else:
                    flag = False
                    state = 7
            case 4:
                if ch[3] == 'd':
                    state = 5
                else:
                    flag = False
                    state = 7
            case 5:
                if ch[4] == '|':
                    state = 6
                else:
                    state = 7
            case 6:
                try:
                    if (ch[5] != " "):
                        return None
                except:
                    return "|Add|"

            case 7:
                None

def equ(ch):
    flag = True
    state = 1

    while flag:
        match state:
            case 1:
                if ch[0] == '|':
                    state = 2
                else:
                    flag = False
                    state = 7

            case 2:
                if ch[1] == 's':
                    state = 3
                else:
                    flag = False
                    state = 7

            case 3:
                if ch[2] == 'e':
                    state = 4
                else:
                    flag = False
                    state = 7
            case 4:
                if ch[3] == 't':
                    state = 5
                else:
                    flag = False
                    state = 7
            case 5:
                if ch[4] == '|':
                    state = 6
                else:
                    state = 7
            case 6:
                try:
                    if (ch[5] != " "):
                        return None
                except:
                    return "|Set|"

            case 7:
                None

def constNumber(ch):
    if ch.isdigit():  
        return ch 
    return None

def stringLiteral(ch):
    if len(ch) >= 2 and ((ch[0] == '"' and ch[-1] == '"') or (ch[0] == "'" and ch[-1] == "'")):
        return ch 
    return None 

def floatNumber(ch):
    state = 1
    has_dot = False 
    for char in ch:
        match state:
            case 1:
                if char.isdigit():  
                    state = 2
                else:
                    return None  
            case 2:
                if char.isdigit():
                    state = 2
                elif char == '.' and not has_dot:  
                    state = 3
                    has_dot = True
                else:
                    return None
            case 3:
                if char.isdigit():  
                    state = 3
                else:
                    return None
    return ch if has_dot else None

def Check(input):
    token = None
    state = 1
    found = False  
    while not found:
        match (state):
            case 1:
                token = Identifire(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 2:
                token = clause(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 3:
                token = Add(input)
                if token is not None:
                    found = True
                    return token
                state += 1  
            case 4:
                token = value(input)
                if token is not None:
                    found = True
                    return token
                state += 1 
            case 5:
                token = floop(input)
                if token is not None:
                    found = True
                    return token
                state += 1 
            case 6:
                token = wloop(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 7:
                token = define(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 8:
                token = With(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 9:
                if input == '<':
                    found = True
                    return 'Smaller'
                state += 1  
            case 10:
                if input == '>':
                    found = True
                    return 'Bigger'
                state += 1
            case 11:
                if input == ')':
                    found = True
                    return 'Close-Parantese'
                state += 1 
            case 12:
                if input == '(':
                    found = True
                    return 'Open-Parantese'
                state += 1 
            case 13:
                if input == '}':
                    found = True
                    return 'Close-Bracket'
                state += 1  
            case 14:
                if input == '{':
                    found = True
                    return 'Open-Bracket'
                state += 1    
            case 15:
                token = Int(input)
                if token is not None:
                    found = True
                    return token
                state += 1 
            case 16:
                token = float(input)
                if token is not None:
                    found = True
                    return token
                state += 1 
            case 17:
                token = String(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 18:
                token = division(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 19:
                token = equ(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 20:
                token = subtraction(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 21:
                token = multiplication(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 22:
                token = From(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 23:
                token = To(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 24:
                token = by(input)
                if token is not None:
                    found = True
                    return token
                state += 1
            case 25:
                if constNumber(input) is not None:
                    return input
                state += 1
            case 26:
                if floatNumber(input) is not None:
                    return "Float"
                state += 1
            case 27:
                if stringLiteral(input) is not None:
                    return "String"
                state += 1
            case 28:
                if end(input) is not None:
                    return "end"
                state += 1
            case 29:
                if another_Clause(input) is not None:
                    return "another_Clause"
                state += 1
            case 30:
                if input == 'true':
                    found = True
                    return 'True'
                state += 1  
            case 31:
                if input == 'false':
                    found = True
                    return 'False'
                state += 1 
            case 32:
                    return "Not Found"             

def process_file(filename):
    global txtfile
    txtfile = []
    with open(filename, 'r') as file:
        content = file.read()
        txtfile = content.split()

def find_not_found(tokens):
    print("---------------------------------------------------------------")
    for token in tokens:
        if "Not Found_TK" in token:
            word = token.split(",")[1].strip()
            word_index = txtfile.index(word) + 1 
            print(f"Word Number in File: {word_index}  --> Anonymous Word: {word}")
    print("---------------------------------------------------------------")

def token_maker():
    id_counter = 1
    tokens = []
    symbol_table = {}

    for word in txtfile:
        token = Check(word)
        if token == "ID":
            tokens.append(f"ID_TK")
            if word not in symbol_table:
                symbol_table[word] = id_counter
                id_counter += 1
        elif token.isdigit():
            tokens.append(token)

        elif token == "Float":
            tokens.append(f"{token}_TK ")

        elif token == "String":
            tokens.append(f"String_TK, {word}")

        elif token == "Not Found":
            tokens.append(f"NotFound_TK")

        else:
            tokens.append(f"{token}_TK")


    #find_not_found(tokens)
    return tokens

def save_output(output_filename, tokens):
    with open(output_filename, 'w') as output_file:
        for token in tokens:
            output_file.write(token + '\n')
