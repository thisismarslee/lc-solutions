import sys

sys.dont_write_bytecode = True
from Solution import *
from Testcase import *


def testSolution(testCase):
    """
    :param testCase: testCase{nums, target, expected_output}
    :return: print result
    """
    testResult = []
    printWidth = 20  # 控制输出宽度
    for test in testCase:
        # 调用需测试的函数，执行前确认函数名
        output = Solution().f035_2(test[0], test[1])
        testResult.append([test[0], test[2], output, test[2] == output])

    # 打印表头
    print(
        f'{"nums":<{printWidth}s} {"expected_output":<{printWidth}s} {"output":<{printWidth}s}{"pass":<{printWidth}s}')

    # 循环输出测试结果
    for result in testResult:
        print(
            f'{str(result[0]):<{printWidth}s} {str(result[1]):<{printWidth}s} {str(result[2]):<{printWidth}s} {str(result[3]):<{printWidth}s}')


# execute test
def main():
    testSolution(Testcase.case035())  # 选择测试用例


if __name__ == "__main__":
    main()
