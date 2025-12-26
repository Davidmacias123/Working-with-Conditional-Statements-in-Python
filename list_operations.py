"""
list_operations.py
Access Control Decision Script (Success Coach Challenge)
"""

is_admin = True

if is_admin == True:
    print("Access Granted")
else:
    print("Access Denied")

is_admin = True
login_hour = 8
in_business_hours = (login_hour >= 8 and login_hour <= 18)

if is_admin == True and in_business_hours:
    print("Admin access during business hours.")
elif is_admin == True or in_business_hours:
    print("Partial access – check restrictions.")
else:
    print("Access denied.")

security_level = 5

if security_level == 5:
    print("Top Secret Clearance")
elif security_level == 4:
    print("Secret Clearance")
elif security_level == 3:
    print("Confidential Clearance")
elif security_level <= 2:
    print("Restricted Clearance")
else:
    print("Invalid Level")
