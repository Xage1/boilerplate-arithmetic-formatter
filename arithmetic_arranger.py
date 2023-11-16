def arithmetic_arranger(problems):
            if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = []
    for problem in problems:
        operands = problem.split()
        num1, operator, num2 = operands

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits"

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"

        width = max(len(num1), len(num2)) + 2
        line1 = num1.rjust(width)
        line2 = operator + num2.rjust(width - 1)
        dashes = '-' * width

        arranged_problems.extend([line1, line2, dashes])

    if display_answers:
        answers = []
        for problem in problems:
            operands = problem.split()
            num1, operator, num2 = operands
            result = str(eval(problem)).rjust(width)
            answers.append(result)
        arranged_problems.append("    ".join(answers))
    return arranged_problems
