#Any pytest file should start with test_ or end with -test
#python method name should start with test
#Any code should be wrapped in method only
#Method name should have sense
# -k stands for method names execution, -v stands for more info metadata, -s stands for log in output
#you can run specific file with py,test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m smoke
#you can skip test with @pytest.mark.skip
#pytest.mark.xfail
#fixtures are used as setup and teardown mathods for test cases- coftest file to generalize fixture and make it available
# -to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
#When you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello Saumya")


@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])