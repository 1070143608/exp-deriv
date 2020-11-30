from arith import BaseAlgorithm, build_expression, formulate_output


def derivative(exp: any, variable: str):
    """
    Resolving derivative for a exp.
    We just provide two kinds of algorithm of derivative: plus and multiply.
    Plus expression just consists of two parameter and a operator, such as ["+", "a", "b"] equals to "a + b"
    Multiply expression just consists in two parameter and a operator, such as ["*", "a", "b"] equals to "a * b"
    :param exp: list or str
    :param variable: str
    :return: list or str or int
    """
    if BaseAlgorithm.is_constant(exp, variable):
        return 0
    elif BaseAlgorithm.is_same_variable(exp, variable):
        return 1
    elif BaseAlgorithm.is_sum(exp):
        return BaseAlgorithm.make_sum(
            derivative(exp[1], variable),
            derivative(exp[2], variable)
        )
    elif BaseAlgorithm.is_product(exp):
        return BaseAlgorithm.make_sum(
            BaseAlgorithm.make_product(exp[1], derivative(exp[2], variable)),
            BaseAlgorithm.make_product(derivative(exp[1], variable), exp[2])
        )
    else:
        raise Exception(f"unknown expression operator: {exp}")


if __name__ == "__main__":
    res = derivative(build_expression(["*", "x", ["+", ["*", "x", "x"], "x"]]), "x")
    formulate_output(res)
    print()
    formulate_output(["*", "x", ["+", ["*", "x", "x"], "x"]])
