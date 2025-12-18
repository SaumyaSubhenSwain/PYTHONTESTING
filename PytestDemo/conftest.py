import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Saumya","Swain","rahulshetty.com"]

@pytest.fixture(params=[("chrome","Saumya", "Swain"), ("Firefox", "Swain"), ("IE","SSS") ])
def crossBrowser(request):
    return request.param