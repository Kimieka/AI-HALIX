def explain_instruction(instr):

    explanations = {

        "LOAD":"Loads a value into a register",

        "ADD":"Adds two registers together",

        "STORE":"Stores register value into memory",

        "READ":"Reads value from memory",

        "JMP":"Jumps to a new instruction location"

    }

    op = instr.split()[0]

    if op in explanations:
        return explanations[op]

    return "Unknown instruction"
