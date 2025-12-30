test_shit = 5

def test_func():
    global test_shit
    test_shit = test_shit
    print(test_shit+10)

test_func()
print(test_shit)