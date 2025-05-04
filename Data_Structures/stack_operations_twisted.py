def text_editor(ops):
    stack = []
    mem_stack = []
    output = []

    for op in ops:
        op = op.split(" ")

        if op[0] == "1":
            stack.extend(list(op[1]))
            mem_stack.append(stack.copy())
        elif op[0] == "2":
            del stack[-int(op[1]):]
            mem_stack.append(stack.copy())
        elif op[0] == "3":
            output.append(stack[int(op[1]) - 1])
        elif op[0] == "4":
            mem_stack.pop()
            stack = mem_stack[-1].copy() if mem_stack else []

    for ch in output:
        print(ch)

if __name__ == "__main__":
    query = int(input().strip())
    ops = []
    for _ in range(query):
        ops.append(input().strip())

    text_editor(ops)
