def main():
    # {Number of production rule: ({first sets}, {Follow up sets})}
    sets = {
        0: ({"FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}, {"$"}),
        1: ({"FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}, {"$"}),
        2: ({"FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}, {"$", "}"}),
        3: ({"ε"}, {"$", "}"}),
        4: ({"FLOATTYPE", "INT"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$"}),
        5: ({"ID"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$"}),
        6: ({"IF"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$"}),
        7: ({"FOR"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$"}),
        8: ({"{"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$"}),
        9: ({"INT"}, {"ID"}),
        10: ({"FLOATTYPE"}, {"ID"}),
        11: ({"ID"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$", "RPAREN", "SEMI"}),
        12: ({"IF"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$", "RPAREN", "SEMI"}),
        13: ({"FOR"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$", "RPAREN", "SEMI"}),
        14: ({"{"}, {"FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}", "$", "RPAREN", "SEMI"}),
        15: ({"(", "ID", "NUM", "FLOAT"}, {"RPAREN", "SEMI"}),
        16: ({"(", "ID", "NUM", "FLOAT"}, {"EQ", "LT", "RPAREN", "SEMI"}),
        17: ({"EQ"}, {"(", "ID", "NUM", "FLOAT"}),
        18: ({"ε"}, {"RPAREN", "SEMI"}),
        19: ({"(", "ID", "NUM", "FLOAT"}, {"LT", "EQ", "RPAREN", "SEMI"}),
        20: ({"LT"}, {"(", "ID", "NUM", "FLOAT"}),
        21: ({"ε"}, {"EQ", "RPAREN", "SEMI"}),
        22: ({"(", "ID", "NUM", "FLOAT"}, {"PLUS", "MINUS", "LT", "EQ", "RPAREN", "SEMI"}),
        23: ({"PLUS"}, {"(", "ID", "NUM", "FLOAT"}),
        24: ({"MINUS"}, {"(", "ID", "NUM", "FLOAT"}),
        25: ({"ε"}, {"LT", "EQ", "RPAREN", "SEMI"}),
        26: ({"(", "ID", "NUM", "FLOAT"}, {"MULT", "DIV", "PLUS", "MINUS", "LT", "EQ", "RPAREN", "SEMI"}),
        27: ({"MULT"}, {"(", "ID", "NUM", "FLOAT"}),
        28: ({"DIV"}, {"(", "ID", "NUM", "FLOAT"}),
        29: ({"ε"}, {"PLUS", "MINUS", "LT", "EQ", "RPAREN", "SEMI"}),
        30: ({"("}, {"MULT", "DIV", "PLUS", "MINUS", "LT", "EQ", "RPAREN", "SEMI"}),
        31: ({"ID"}, {"MULT", "DIV", "PLUS", "MINUS", "LT", "EQ", "RPAREN", "SEMI"}),
        32: ({"NUM"}, {"MULT", "DIV", "PLUS", "MINUS", "LT", "EQ", "RPAREN", "SEMI"}),
        33: ({"FLOAT"}, {"MULT", "DIV", "PLUS", "MINUS", "LT", "EQ", "RPAREN", "SEMI"}),
    }

    print("Rule Number | FIRST Sets             | FOLLOW Sets")
    print("-" * 60)

    for rule_number, (first_set, follow_set) in sets.items():
        first_formatted = ', '.join(sorted(s for s in first_set if s))
        follow_formatted = ', '.join(sorted(s for s in follow_set if s))
        print(f"{rule_number:12} | {first_formatted:24} | {follow_formatted}")

if __name__ == "__main__":
    main()

