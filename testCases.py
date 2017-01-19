def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker','When user goes to home page, the page should be loaded'],
    ['Blocker', 'Valid user should be able to login'],
    ['Blocker', 'Invalid user should not be able to login'],
    ['Blocker', 'Invalid user with only username should not be able to login'],
    ['Blocker', 'Invalid user with only password should not be able to login'],
    ['Blocker', 'Invalid user without any credentials should not be able to login'],
]