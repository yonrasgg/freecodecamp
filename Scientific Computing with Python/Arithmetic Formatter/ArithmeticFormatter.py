def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    results = ""
    for problem in problems:
        parts = problem.split()
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        result = str(eval(problem))
        width = max(len(parts[0]), len(parts[2])) + 2
        first += parts[0].rjust(width) + '    '
        second += parts[1] + parts[2].rjust(width - 1) + '    '
        lines += '-' * width + '    '
        if solve:
            results += result.rjust(width) + '    '

    arranged_problems = first.rstrip() + '\n' + second.rstrip() + '\n' + lines.rstrip()
    if solve:
        arranged_problems += '\n' + results.rstrip()
    return arranged_problems
            