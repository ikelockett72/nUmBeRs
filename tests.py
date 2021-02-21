try:
    assert type(int) == type(type(str))
except AssertionError:
    raise AssertionError("Something is wrong. Please check the code")
