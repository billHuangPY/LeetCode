class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit():
            return [int(expression)]

        ans = []
        for i in range(len(expression)):
            if not expression[i] in set(["+", "-", "*"]):
                continue

            ope = expression[i]
            OPT_1 = self.diffWaysToCompute(expression[:i])
            OPT_2 = self.diffWaysToCompute(expression[i + 1 :])
            for j in OPT_1:
                for k in OPT_2:
                    if ope == "+":
                        ans.append(j + k)
                    elif ope == "-":
                        ans.append(j - k)
                    else:
                        ans.append(j * k)
        return ans


class Solution2(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        def computeDaC(exp):
            if len(exp) == 3:
                return [str(eval("".join(exp)))]
            elif len(exp) == 1:
                return [exp[0]]

            ans, int_num = [], int(len(exp) / 2) + 1
            for i in range(1, int_num):
                OPT_a, OPT_b = computeDaC(exp[: i * 2 - 1]), computeDaC(
                    exp[i * 2 :]
                )
                for j in OPT_a:
                    for k in OPT_b:
                        ans.append(str(eval(j + exp[i * 2 - 1] + k)))
            return ans

        delimit = set(["+", "-", "*"])
        exp_list, curr_int = [], ""
        for ptr in range(len(expression) + 1):
            if ptr == len(expression):
                exp_list.append(curr_int)
            elif expression[ptr] in delimit:
                exp_list.append(curr_int)
                exp_list.append(expression[ptr])
                curr_int = ""
            else:
                curr_int += expression[ptr]

        return computeDaC(exp_list)
