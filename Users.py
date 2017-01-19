from operator import itemgetter

users=[

    {"name": "invalid_user", "email": "ohnedich1991@gmail.com", "password": "123456"},
	{"name": "valid_user", "email": "abhijeet@gmail.com", "password": "password"},
	{"name": "user_blank", "email": "", "password": "qwert1235"},
	{"name": "pass_blank", "email": "jagga.dakuu01@gmail.com", "password": ""},
	{"name": "user_pass_blank", "email": "", "password": ""},
	{"name": "Admin2", "email": "admin@test.com", "password": "qwert1234"},
]

def get_user(name):
    try:

        #return (user for user in users if user["name"]==next(name))
        return (user for user in users if user["name"]==name).__next__()


    except:
        print("\n User %s is not defined in the parameters , enter a valid user" %name)

