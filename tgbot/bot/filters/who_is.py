from config import ADMINS

def is_admin(id):
    # print(type(ADMINS), ADMINS)
    if str(id) in ADMINS:
        # print("admin")
        return True
    else:
        # print("not admin")
        return False