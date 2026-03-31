# 🧪 Example Test Cases
**Software Testing Internship (QA) - STI/UFRN**  
*Sample test cases from internal university system testing (anonymized)*

---

## Test Case 1: User Login Functionality
| **ID** | **TC-001** |
|--------|------------|
| **Title** | Verify successful login with valid credentials |
| **Preconditions** | User account exists in system |
| **Steps** | 1. Navigate to login page<br>2. Enter valid username<br>3. Enter valid password<br>4. Click "Login" |
| **Expected Result** | User redirected to dashboard; welcome message displayed |
| **Status** | ✅ PASS |
| **Test Date** | 15/05/2012 |

---

## Test Case 2: Invalid Password Entry
| **ID** | **TC-002** |
|--------|------------|
| **Title** | Verify error message for incorrect password |
| **Preconditions** | User account exists |
| **Steps** | 1. Navigate to login page<br>2. Enter valid username<br>3. Enter invalid password<br>4. Click "Login" |
| **Expected Result** | Error: "Senha inválida. Tente novamente." (3 attempts max) |
| **Status** | ✅ PASS |
| **Test Date** | 15/05/2012 |

---

## Test Case 3: Usability - Form Validation
| **ID** | **TC-003** |
|--------|------------|
| **Title** | Verify real-time email validation |
| **Preconditions** | User on registration form |
| **Steps** | 1. Enter invalid email (no @ symbol)<br>2. Tab to next field |
| **Expected Result** | Red border + "Please enter valid email" message appears instantly |
| **Status** | ⚠️ FAIL |
| **Bug ID** | JRA-123 |
| **Test Date** | 20/06/2012 |

---

## Regression Test Suite Summary
Total Test Cases: 47
Passed: 42 ✅
Failed: 3 ⚠️
Blocked: 2 ⏸️
Execution Rate: 89%

**Note:** These examples reflect testing methodology used during STI-UFRN internship. Actual system names and data anonymized.
