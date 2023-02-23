print('Test Txt')


def run_test_func():
    return 'Test func ran'


def run_default_func():
    return 'Default ran'


def run_test_func_two():
    return 'Func two ran'


def switch_case(switch):
    switch_obj = {
        'test': run_test_func,
        'test2': run_test_func_two,
        'default': run_default_func
    }

    try:
        return switch_obj[switch]()
    except Exception as e:
        return switch_obj['default']()


print(switch_case('taco'))
