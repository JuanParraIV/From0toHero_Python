# Encapsulates login in function
name_of_units = "name"


def days_to_units(days, units):
    to_hours = 24
    to_minutes = 24 * 60
    to_seconds = 24 * 60 * 60

    if units == "hours":
        return print(f"{days} dias son {days * to_hours} {units}")
    if units == "minutes":
        return print(f"{days} dias son {days * to_minutes} {units}")
    if units == "seconds":
        return print(f"{days} dias son {days * to_seconds} {units}")


def scope_check(num_days):
    sur_name = "Parra"
    print(num_days)  # scoped variable for this function
    print(name_of_units)  # global scope variable passed as a parameter
    print(
        f"{sur_name=}"
    )  # scoped variable for this function initialized in scope_check function


days_to_units(30, "minutes")
scope_check(30)
