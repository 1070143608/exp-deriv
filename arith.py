

def build_expression(original_exp: any) -> list:
    """
    This method just supports plus or multiply operator
    :param origin_exp: a expression consists of str in which item is spilt by space.
                       Such as: 'a + b * x',
    :return: list -> complex prefix expression
    """
    return original_exp


def formulate_output(original_output: any):
    """
    formulate output
    :param original_output:
    :return: None
    """
    if isinstance(original_output, str) or isinstance(original_output, int):
        print(str(original_output), end=" ")
    else:
        print("(", end=" ")
        formulate_output(original_output[1])
        print(original_output[0], end=" ")
        formulate_output(original_output[2])
        print(")", end=" ")


class BaseAlgorithm:
    @staticmethod
    def is_constant(exp: any, variable: str) -> bool:
        """
        Determine if the expression is a constant
        :param exp: list or int or str
        :param variable: str
        :return: bool
        """
        if (isinstance(exp, int) or isinstance(exp, str)) and exp != variable:
            return True
        return False

    @staticmethod
    def is_same_variable(exp: any, variable: str) -> bool:
        """
        Determine if the expression is a variable
        :param exp: list or int or str
        :param variable: str
        :return: bool
        """
        if exp == variable:
            return True
        return False

    @staticmethod
    def is_sum(exp: any) -> bool:
        """
        Determine if the expression is a add operation
        :param exp: list or int or str
        :param variable: str
        :return: bool
        """
        if isinstance(exp, list) and len(exp) > 1 and exp[0] == "+":
            return True
        return False

    @staticmethod
    def make_sum(exp1: any, exp2: any) -> any:
        """
        add operation
        :param exp1:
        :param exp2:
        :return:
        """
        if exp1 == 0:
            return exp2
        elif exp2 == 0:
            return exp1
        elif isinstance(exp1, int) and isinstance(exp2, int):
            return exp1 + exp2
        else:
            return ["+", exp1, exp2]

    @staticmethod
    def is_product(exp: any) -> bool:
        """
        Determine if the expression is a multiply operation
        :param exp: list or int or str
        :param variable: str
        :return: bool
        """
        if len(exp) > 1 and exp[0] == "*":
            return True
        return False

    @staticmethod
    def make_product(exp1: any, exp2: any) -> any:
        """
        multiply operation
        :param exp1:
        :param exp2:
        :return:
        """
        if exp1 == 0 or exp2 == 0:
            return 0
        elif exp1 == 1:
            return exp2
        elif exp2 == 1:
            return exp1
        elif isinstance(exp1, int) and isinstance(exp2, int):
            return exp1 * exp2
        else:
            return ["*", exp1, exp2]

