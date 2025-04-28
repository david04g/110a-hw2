def main():
    #{Number of production rule: ({first sets}, {Follow up sets})
sets = {
        0: ({"FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}, {"$"}),
        1: ({"FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}, {"$"}),
        2: ({"FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}, {"$", "}"}),
        3: ({}, {"$", "}"}),
        4: ({"FLOATTYPE", "INT"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}"}),
        5: ({"ID"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}"}),
        6: ({"IF"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}"}),
        7: ({"FOR"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}"}),
        8: ({"{"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{", "}"}),
        9: ({"INT"}, {"ID"}),
        10: ({"FLOATTYPE"}, {"ID"}),
        11: ({"ID"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}),
        12: ({"IF"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}),
        13: ({"FOR"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}),
        14: ({"{"}, {"$", "FLOATTYPE", "FOR", "ID", "IF", "INT", "{"}),
        15: ({"(", "FLOAT", "ID", "NUM"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        16: ({"(", "FLOAT", "ID", "NUM"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        17: ({"EQ"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        18: ({}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        19: ({"(", "FLOAT", "ID", "NUM"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        20: ({"LT"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        21: ({}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        22: ({"(", "FLOAT", "ID", "NUM"}, {"EQ", "LT", "RPAREN", "SEMI"}),
        23: ({"PLUS"}, {"EQ", "LT", "RPAREN", "SEMI"}),
        24: ({"MINUS"}, {"EQ", "LT", "RPAREN", "SEMI"}),
        25: ({}, {"EQ", "LT", "RPAREN", "SEMI"}),
        26: ({"(", "FLOAT", "ID", "NUM"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        27: ({"MULT"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        28: ({"DIV"}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        29: ({}, {"EQ", "LT", "MINUS", "PLUS", "RPAREN", "SEMI"}),
        30: ({"("}, {"DIV", "EQ", "LT", "MINUS", "MULT", "PLUS", "RPAREN", "SEMI"}),
        31: ({"ID"}, {"DIV", "EQ", "LT", "MINUS", "MULT", "PLUS", "RPAREN", "SEMI"}),
        32: ({"NUM"}, {"DIV", "EQ", "LT", "MINUS", "MULT", "PLUS", "RPAREN", "SEMI"}),
        33: ({"FLOAT"}, {"DIV", "EQ", "LT", "MINUS", "MULT", "PLUS", "RPAREN", "SEMI"}),
    }
    print("Rule Number | FIRST Sets    | FOLLOW Sets")
    print("-" * 50)

    for rule_number, (first_set, follow_set) in sets.items():
        first_formatted = ', '.join(sorted(s for s in first_set if s))
        follow_formatted = ', '.join(sorted(s for s in follow_set if s))
        print(f"{rule_number:12} | {first_formatted:15} | {follow_formatted}")

if __name__ == "__main__":
    main()

