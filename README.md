# List Operations: Access Control (Python)

## Purpose (On-the-Job Scenario)
You’ve been asked to help automate access control for a secure folder based on user roles and time of access.  
This script decides whether access is granted or denied using **conditional logic** in Python.

In this project, access decisions are based on:
- **Admin status** (`is_admin`: True/False)
- **Time of login** (`login_hour`: 0–23)
- **Security clearance level** (`security_level`: 1–5)

---

## Learning Objectives
By completing this challenge, I practiced:
- Writing **if/else** statements
- Writing **if/elif/else** statements
- Using **logical operators** (`and`, `or`)
- Using **comparison operators** (`==`, `>=`, `<=`)
- Testing different outcomes by changing variable values in the script

---

## Project Files
- `list_operations.py` → main script with all challenge steps
- `screenshots/` → testing proof (Spyder output screenshots)

---

## How to Run (Anaconda + Spyder)
1. Open **Anaconda Navigator**
2. Launch **Spyder IDE**
3. Create/open `list_operations.py`
4. Click **Run**
5. Change the variables (`is_admin`, `login_hour`, `security_level`) and run again to test different outputs

---

## Challenge Steps Completed

### Step 3: Basic If/Else Statement
**Goal:** Print access results based on admin status.

**Variables:**
- `is_admin` (True/False)

**Logic:**
- If `is_admin` is True → prints: **“Access Granted”**
- Else → prints: **“Access Denied”**

✅ **Tests to run:**
- `is_admin = True`
- `is_admin = False`

---

### Step 4: Add Login Time Context (0–23)
**Goal:** Use *two conditions* (admin + time).

**Variables:**
- `is_admin` (True/False)
- `login_hour` (0–23)

**Business Hours Rule:**
- Business hours are **8 through 18** (8am–6pm)

**Outputs:**
- Admin **AND** business hours → **“Admin access during business hours.”**
- Only one condition is true → **“Partial access – check restrictions.”**
- Neither is true → **“Access denied.”**

✅ **Tests to run:**
- `is_admin=True, login_hour=9` → Admin access during business hours
- `is_admin=True, login_hour=2` → Partial access
- `is_admin=False, login_hour=10` → Partial access
- `is_admin=False, login_hour=2` → Access denied

---

### Step 5: Security Level (Five Options)
**Goal:** Print a clearance message based on `security_level`.

**Variable:**
- `security_level` (1–5)

**Outputs:**
- Level 5 → **“Top Secret Clearance”**
- Level 4 → **“Secret Clearance”**
- Level 3 → **“Confidential Clearance”**
- Level 2 or below → **“Restricted Clearance”**
- Anything else → **“Invalid Level”**

✅ **Tests to run:**
- `security_level = 5`
- `security_level = 4`
- `security_level = 3`
- `security_level = 2`
- `security_level = 1`
- `security_level = 99` (or any non 1–5 number)

---

## Screenshots (Proof of Testing)
After each test, take a screenshot of the Spyder console output and save it in the `screenshots/` folder.

### Step 3
- `screenshots/step1_admin_true.png`
- `screenshots/step1_admin_false.png`

### Step 4
- `screenshots/step2_business_hours.png`
- `screenshots/step2_partial_access.png`
- `screenshots/step2_access_denied.png`

### Step 5
- `screenshots/step3_level5.png`
- `screenshots/step3_level4.png`
- `screenshots/step3_level3.png`
- `screenshots/step3_level2_or_below.png`
- `screenshots/step3_invalid.png`

---

## Super Simple Explanation (Explain Like I’m 5)
- `is_admin` is like a **VIP badge**.
  - If you have it (True), you can get in.
  - If you don’t (False), you can’t.

- `login_hour` is the **time on the clock**.
  - If it’s during business hours (8–18), that’s better access.

- `security_level` is like a **power level**.
  - 5 is the biggest power (Top Secret).
  - 1–2 is small power (Restricted).
  - Weird numbers mean “Invalid”.

---

## Author
David Macias
