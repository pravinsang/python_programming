class PasswordVerify:
    def __init__(self):
        self.password = None

    def set_password(self):
        password = input('Set the password')
        self.password = password

    def verify_password(self):
        attempts = 3
        while attempts > 0:
            entered_password = input('Enter the password')
            if entered_password == self.password:
                print("Access Granted")
                return
            else:
                attempts -= 1
                print(f"Incorrect password. You have {attempts} chances left.")
        
        print("Access Denied")

user1 = PasswordVerify()
user1.set_password()
user1.verify_password()
