# `list_operations.py` — Access Control Decision Script (Python)

## On-the-Job Scenario (What this project is pretending to solve)
You’ve been asked to help automate **access control** for a secure folder based on:
- a user’s **role** (admin or not)
- the **time** they try to log in
- their **security clearance level**

This project is a simple Python script that prints a message like **“Access Granted”** or **“Access Denied”** depending on those rules.

---

## What you will learn (Learning Objectives)
By completing this script, you practice:
- **`if` / `else`** (two choices)
- **`if` / `elif` / `else`** (many choices)
- **logical operators**: `and`, `or`
- **comparison operators**: `==`, `>=`, `<=`
- changing variables and re-running to test different outcomes

---

## How to run it (Spyder / Anaconda)
1. Open **Anaconda Navigator**
2. Launch **Spyder**
3. Open the file: `list_operations.py`
4. Click **Run**
5. Change the test values (`is_admin`, `login_hour`, `security_level`) and click **Run** again

---

## The code (final version)
> This version matches your Success Coach steps and behaves exactly as described.

```python
"""
list_operations.py
Access Control Decision Script (Success Coach Challenge)

Goal:
- Use if/else, and if/elif/else with logical conditions
- Decide access based on:
  1) admin status
  2) login hour (0-23)
  3) security level (1-5)
"""

# -------------------------
# Step 3: Basic If/Else
# -------------------------

is_admin = True  # Change to False to test the other path

if is_admin == True:
    print("Access Granted")
else:
    print("Access Denied")


# -------------------------
# Step 4: Add Time Context
# -------------------------

is_admin = True        # Change True/False to test
login_hour = 8         # Pick a number from 0 to 23

# Business hours are 8 through 18 (8am to 6pm)
in_business_hours = (login_hour >= 8 and login_hour <= 18)

if is_admin == True and in_business_hours:
    print("Admin access during business hours.")
elif is_admin == True or in_business_hours:
    print("Partial access – check restrictions.")
else:
    print("Access denied.")


# -------------------------
# Step 5: Security Levels 1–5
# -------------------------

security_level = 5  # Change this number to test: 5, 4, 3, 2, 1, or something else

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
```

---

## Step-by-step (Success Coach Requirements)

### Step 3 — Basic If/Else
**Requirement:**
- Create `is_admin` (True/False)
- If admin → print **Access Granted**
- Else → print **Access Denied**

**Where it happens in code:**
- `is_admin = True`
- the `if` block prints “Access Granted”
- the `else` block prints “Access Denied”

✅ Try these tests:
- `is_admin = True` → Access Granted
- `is_admin = False` → Access Denied

---

### Step 4 — Admin + Business Hours (8–18)
**Requirement:**
- Create `login_hour` (0–23)
- If admin AND time is between 8 and 18 → print “Admin access during business hours.”
- If only one is true → print “Partial access – check restrictions.”
- If neither is true → print “Access denied.”

**Where it happens in code:**
- `login_hour = 8`
- `in_business_hours = (login_hour >= 8 and login_hour <= 18)`
- the `if / elif / else` prints the correct message

✅ Try these tests:
- `is_admin=True, login_hour=9` → Admin access during business hours.
- `is_admin=True, login_hour=2` → Partial access – check restrictions.
- `is_admin=False, login_hour=10` → Partial access – check restrictions.
- `is_admin=False, login_hour=2` → Access denied.

---

### Step 5 — Five Options (Security Level 1–5)
**Requirement:**
- Create `security_level` (1–5)
- 5 → Top Secret
- 4 → Secret
- 3 → Confidential
- 2 or below → Restricted
- anything else → Invalid Level

✅ Try these tests:
- `security_level = 5` → Top Secret Clearance
- `security_level = 4` → Secret Clearance
- `security_level = 3` → Confidential Clearance
- `security_level = 2` → Restricted Clearance
- `security_level = 1` → Restricted Clearance
- `security_level = 99` → Invalid Level

---

## Simple explanation

### The script is like a door with rules:
- **`is_admin`** is like having a **special VIP badge**.
  - `True` means “Yes, I have the badge.”
  - `False` means “No, I don’t.”

- **`login_hour`** is like the **time on a clock** (0–23).
  - If it’s between **8 and 18**, that’s “business time.”

- **`security_level`** is like a **power level**.
  - 5 is the biggest power (Top Secret)
  - 4 is big power (Secret)
  - 3 is medium power (Confidential)
  - 1–2 is small power (Restricted)

The code just checks the rules and prints the right sentence.

---

## Every single line explained (line-by-line)

### Header / docstring
- `""" ... """`
  - This is a **label note** for humans. Python ignores it while running.
  - It tells what the file is and what the goal is.

### Step 3 lines
- `is_admin = True`
  - Create a variable named `is_admin`.
  - Store a **Boolean** value: `True` or `False`.

- `if is_admin == True:`
  - Ask the question: “Is `is_admin` True?”
  - If yes, run the next indented lines.

- `print("Access Granted")`
  - Print those words to the screen.

- `else:`
  - If the `if` question was **not** true, do this instead.

- `print("Access Denied")`
  - Print denial message.

### Step 4 lines
- `login_hour = 8`
  - Store the login time as a number (0–23).

- `in_business_hours = (login_hour >= 8 and login_hour <= 18)`
  - Make a helper variable.
  - `login_hour >= 8` means “8 or later”.
  - `login_hour <= 18` means “18 or earlier”.
  - `and` means **both must be true**.
  - Parentheses `(...)` keep it grouped as one clear check.

- `if is_admin == True and in_business_hours:`
  - “Is the person admin AND is it business hours?”
  - If yes → full admin business-hours message.

- `elif is_admin == True or in_business_hours:`
  - `elif` means “else if” (another option).
  - `or` means **at least one** must be true.
  - So if they’re admin OR it’s business hours → partial access.

- `else:`
  - If neither condition is true → deny.

### Step 5 lines
- `security_level = 5`
  - Set clearance level.

- `if security_level == 5:`
  - If it equals 5 → Top Secret.

- `elif security_level == 4:`
  - Else if equals 4 → Secret.

- `elif security_level == 3:`
  - Else if equals 3 → Confidential.

- `elif security_level <= 2:`
  - Else if 2 **or 1** (2 or below) → Restricted.

- `else:`
  - Anything weird (like 0, 6, 99, -1) → Invalid Level.

---

# Screenshots of my work
<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/62aa41f2-d044-48a4-92f9-cf8393991365" />

