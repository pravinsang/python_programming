# Higger order Function
def create_logger(prefix):
    def logger(message):
        print(f"{prefix} -> {message}")
    return logger

error_log = create_logger("Error")      #Closure
info_log = create_logger("Info")

error_log("You got a syntax error")
error_log("You missed the intendation")
info_log("Use comments in code")

