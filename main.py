import mysql.connector as c
import datetime
import random

# from datetime import date
# from datetime import datetime
con = c.connect(host='localhost', database='bank_management_system', user='root')
if con.is_connected():
    print("Successfully connected.")

'''
def generateId():
    s = "*#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    si = ""
    for i in range(4):
        si += random.choice(s)
    return si
'''


def AC():
    while True:
        ac = input("Enter Account No: ")
        if ac.isnumeric():
            return ac
        else:
            print("Invalid account number. Please enter a number(0-9).")


def AM():
    while True:
        am = input("Enter Amount: ")
        if am.isnumeric():
            return am
        else:
            print("Invalid amount number. Please enter a number containing only (0-9).")


def NM(name):
    while True:
        n = input(f"Enter {name} Name: ")
        if n.isalpha():
            return n
        else:
            print("Invalid name. Please enter a name containing only alphabets.")


def DB():
    while True:
        db = input("Enter date of birth in the format DD/MM/YYYY: ")
        isValidDate = True
        try:
            date_of_birth = datetime.datetime.strptime(db, "%d/%m/%Y")
        except ValueError:
            isValidDate = False

        if isValidDate:
            return db
        else:
            print(
                "Invalid date of birth. Please enter a date which is in day/month/year format and containing only numbers and '/' symbol.")


def Pass():
    while True:
        ps = input("Enter a password: ")
        if len(ps) < 4 or len(ps) > 16:
            print("Invalid password. Password length should be (4-16)")
        else:
            return ps


def PHN():
    while True:
        p = input("Enter a Phone Number: ")
        if len(p) != 11:
            print("Invalid phone number. Please Enter a number containing 11 digits.")
        else:
            if p.isnumeric():
                return p
            else:
                print("Invalid phone number. Please Enter a number(0-9)")


def ADD(name):  # address or location
    s = "#&, 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        n = input(f"Enter {name}: ")
        for i in range(len(n)):
            if n[i] not in s:
                print(n[i])
                print(f"Invalid {name}.  Please enter {name} containing only [(0-9),(A-Z),(a-z),#,&,',' or " "].")
                break
        if i + 1 == len(n):
            break
    return n


def get_balance(ac):
    sql = "select Balance from amount where Account_No=%s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(sql, data)
    result = cur.fetchone()
    return result


def update_balance(bal, ac):
    sql = "update amount set Balance=%s where Account_No=%s"
    data = (bal, ac)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()


def openAcc():
    n = NM("User")
    # ac=generateId()
    ps = Pass()
    db = DB()
    ad = input("Enter Address: ")
    while True:
        ob = input("Enter Opening Balance: ")
        if ob.isnumeric():
            break
        else:
            print("Invalid balance.")
    while True:
        print("""
1. Admin
2. Officer
3. Customer
        """)
        ty = int(input("Choose account type: "))
        if ty == 1:
            ac_type = "Admin"
            break
        elif ty == 2:
            ac_type = "Officer"
            break
        elif ty == 3:
            ac_type = "Customer"
            break
        else:
            print("Sorry!!Wrong Input. Please try again.")
    p = PHN()
    data1 = (n, ps, db, ad, p, ob)
    sql1 = 'insert into account(Name,Account_Pass,DoB,Address,Phone_No,Opening_Balance) values(%s,%s,%s,%s,%s,%s)'
    cur = con.cursor()  # to process individual rows in database
    cur.execute(sql1, data1)
    con.commit()  # used to save changes invoked by a transaction to the database.
    sql = "select Account_NO from account where Name=%s AND Phone_No=%s"
    data = (n, p)
    cur = con.cursor()
    cur.execute(sql, data)
    result = cur.fetchone()
    ac = result[0]
    print(f"Congratulations! Dear Customer, your new account is created.Your account number is: {ac}")
    data2 = (n, ac, ob)
    data3 = (ac, ps, ac_type)
    sql2 = 'insert into amount values(%s,%s,%s)'
    sql3 = 'insert into log_info values(%s,%s,%s)'
    cur = con.cursor()
    cur.execute(sql2, data2)
    cur.execute(sql3, data3)
    con.commit()
    Officer()


def depoAmo():
    from datetime import date
    from datetime import datetime
    ac = AC()
    am = AM()
    result = get_balance(ac)
    update_balance(int(result[0]) + int(am), ac)
    print(f"Dear Customer,Deposited {am} Deposited Successfully")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")  # dd/mm/YY
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sql1 = "insert into tran_details values(%s,%s,%s)"
    si = f"{am} deposited at {current_time}"
    data1 = (ac, d1, si)
    cur = con.cursor()
    cur.execute(sql1, data1)
    con.commit()
    Officer()


def withAmo(ac):
    from datetime import date
    from datetime import datetime
    # ac = AC()
    am = AM()
    result = get_balance(ac)
    if int(result[0]) - int(am) < 0:
        print("Sorry! You have", result[0], "balance in your account. Try with some lower ammount.")
        tranAmo()
    update_balance(int(result[0]) - int(am), ac)
    print(f"Dear Customer, Withdrawn {am} BDT Successfully")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")  # dd/mm/YY
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sql1 = "insert into tran_details values(%s,%s,%s)"
    si = f"{am} withdrawed at {current_time}"
    data1 = (ac, d1, si)
    cur = con.cursor()
    cur.execute(sql1, data1)
    con.commit()
    customer(ac)


def tranAmo(ac):
    from datetime import date
    from datetime import datetime
    # ac=AC()
    am = AM()
    result = get_balance(ac)
    if int(result[0]) - int(am) < 0:
        print("Sorry! You have", result[0], "balance in your account. Try with some lower ammount to transfer.")
        tranAmo()
    nc = input("Enter the account number to transfer: ")
    update_balance(int(result[0]) - int(am), ac)
    result1 = get_balance(nc)
    update_balance(int(result1[0]) + int(am), nc)
    print(f"""Dear Customer,
TK {am} has been transferred from account number {ac}.
Balance Tk.{int(result[0]) - int(am)}""")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")  # dd/mm/YY
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sql1 = "insert into tran_details values(%s,%s,%s)"
    si = f"{am} transfered at {current_time}"
    data1 = (ac, d1, si)
    cur = con.cursor()
    cur.execute(sql1, data1)
    con.commit()
    customer(ac)


def balance():
    ac = AC()
    sql = "select balance from amount where Account_No=%s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(sql, data)
    result = []
    result = cur.fetchone()
    con.commit()
    print(f"Balance of Account No {ac} is: {result[0]}")
    Officer()


def displayCD():
    ac = AC()
    sql = "select * from account where Account_No=%s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(sql, data)
    result = cur.fetchone()
    con.commit()
    print("Account details are following below...")
    print("Name: ", result[0])
    print("Accout No:", result[1])
    print("Date of Birth:", result[2])
    print("Address:", result[3])
    print("Opening Balance:", result[4])
    print("Phone No:", result[5])
    Officer()


def closeAc():
    ac = AC()
    sql1 = "delete from account where Account_No=%s"
    sql2 = "delete from amount where Account_No=%s"
    sql3 = "delete from log_info where Account_No=%s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(sql1, data)
    cur.execute(sql2, data)
    cur.execute(sql3, data)
    con.commit()
    print("Account Successfully Deleted")
    Officer()


def transaction(ac):
    # ac=AC()
    sql = "select T_date,T_details from tran_details where User_id=%s order by T_date"
    data = (ac,)
    cur = con.cursor()
    cur.execute(sql, data)
    result = cur.fetchall()
    print("%-13s" % "Date", end="")
    print("Details", end="\n")
    for i in result:
        print("%-13s" % i[0], end="")
        print("%-13s" % i[1], end="\n")
    con.commit()
    customer(ac)


def createBr():
    n = NM("Branch")
    ad = ADD("location")
    s = "0123456789"
    while True:
        si = ""
        for i in range(2):
            si += random.choice(s)
        sql = "select count(B_id) from branch where B_id=%s"
        data = (si,)
        cur = con.cursor()
        cur.execute(sql, data)
        result = cur.fetchone()
        if result[0] != 0:
            continue
        else:
            break
    sql = "insert into branch values(%s,%s,%s)"
    data = (si, n, ad)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    print("Data inserted successfully", end="\n")
    admin()


def show_br():
    sql = "select B_Name,B_loc from branch"
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print("%-17s" % "Branch Name", end="")
    print("Branch Location", end="\n")
    for i in result:
        print("%-17s" % i[0], end="")
        print("%-17s" % i[1], end="\n")  # right justified(17)
    con.commit()
    admin()


def cr_loan():
    ac = AC()
    print("""
1. Personal Loan
2. Auto Loan
3. Student Loan
4. Small Business Loan
5. Land Loan
        """)
    while True:
        n = int(input("Choose your option: "))
        if n == 1:
            l = "Personal Loan"
            break
        elif n == 2:
            l = "Auto Loan"
            break
        elif n == 3:
            l = "Student Loan"
            break
        elif n == 4:
            l = "Small Business Loan"
            break
        elif n == 5:
            l = "Land Loan"
            break
        else:
            print("Wrong Input. Please try again. Input must be in (1-5)")
    am = AM()
    while True:
        bid = input("Enter the Branch Id: ")
        sql = "select count(B_id) from branch where B_id=%s"
        data = (bid,)
        cur = con.cursor()
        cur.execute(sql, data)
        result = cur.fetchone()
        if result[0] == 0:
            print("Sorry! The branch id doesn't exist. Please enter the correct Branch Id.")
        else:
            break
    sql = "insert into loan(Loan_Type,Amount,B_Id,Account_No) values(%s,%s,%s,%s)"
    data = (l, am, bid, ac)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully")
    Officer()


def show_loan(ac):
    sql = "select Loan_Type,Amount from loan where Account_No=%s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(sql, data)
    result = cur.fetchall()
    print("%-17s" % "Loan Type", end="")
    print("Amount", end="\n")
    for i in result:
        print("%-17s" % i[0], end="")
        print("%-17s" % i[1], end="\n")  # right justified(17)
    con.commit()
    print("\n")
    customer(ac)


def updateAc(ac):
    print("""
1. Name
2. Password
3. Date of Birth
4. Address
5. Phone No
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        # ac = AC()
        n = NM("your")
        sql1 = "update account set name=%s where Account_No=%s"
        sql2 = "update amount set name=%s where Account_No=%s"
        data = (n, ac)
        cur = con.cursor()
        cur.execute(sql1, data)
        cur.execute(sql2, data)
        con.commit()
        print("Name Updated Successfully.")
        print("\n")

    elif choice == '2':
        # ac=AC()
        cp = input("Enter your current password: ")
        np = input("Enter your new password: ")
        sql = "update account set Account_Pass=%s where Account_No=%s AND Account_Pass=%s"
        sql2 = "update log_info set Account_Pass=%s where Account_No=%s AND Account_Pass=%s"
        data = (np, ac, cp)
        cur = con.cursor()
        cur.execute(sql, data)
        cur.execute(sql2, data)
        con.commit()
        x = datetime.datetime.now()
        print(f"PIN for account no {ac} is set successfully at {x}. Please keep it secret & Never share PIN to anyone.")
        print("\n")

    elif choice == '3':
        # ac = AC()
        n = DB()
        sql1 = "update account set DoB=%s where Account_No=%s"
        data = (n, ac)
        cur = con.cursor()
        cur.execute(sql1, data)
        con.commit()
        print("Date of Birth Updated Successfullly.")
        print("\n")

    elif choice == '4':
        # ac = AC()
        n = input("Enter the new address: ")
        sql1 = "update account set Address=%s where Account_No=%s"
        data = (n, ac)
        cur = con.cursor()
        cur.execute(sql1, data)
        con.commit()
        print("Address Updated Successfullly.")
        print("\n")

    elif choice == '5':
        # ac = AC()
        n = PHN()
        sql1 = "update account set Phone_No=%s where Account_No=%s"
        data = (n, ac)
        cur = con.cursor()
        cur.execute(sql1, data)
        con.commit()
        print("Phone Number Updated Successfully.")
        print("\n")
    else:
        print("Invalid number. Please give an integer number(1-4).")
        updateAc()
    customer(ac)


def Officer():
    print("""
1. Create New Account
2. Deposit Amount
3. Balance Enquiry
4. Display Customer Details
5. Close an Account
6. Create Loan
7. Exit
    """)
    choice = input("Enter Task No: ")
    if choice == '1':
        openAcc()
    elif choice == '2':
        depoAmo()
    elif choice == '3':
        balance()
    elif choice == '4':
        displayCD()
    elif choice == '5':
        closeAc()
    elif choice == "6":
        cr_loan()
    elif choice == "7":
        print("Dear Customer, thank you for using our banking system. See you soon. Take care. Bye")
        return 0
    else:
        print("Wrong Choice...")
        Officer()


# Officer()

########################################################
def customer(Account_No):
    print("\t\t Welcome to ABC Bank")
    print("######################################\n\n")
    sql = "SELECT * FROM amount WHERE Account_No = %s"  # account no

    data = (Account_No,)
    cur = con.cursor()
    cur.execute(sql, data)
    result = cur.fetchone()
    print("Name: ", result[0], "\t\t Account No: ", result[1], "\nCurrent Balance: ", result[2])
    print("........................................................\n")
    # while True:
    print("""
1. Withdraw Amount
2. Transfer Amount
3. Loan Details
4. Transaction Details
5. Update Account
6. Exit
        """)
    choice = input("Enter Task No: ")
    if choice == '1':
        withAmo(Account_No)
    elif choice == '2':
        tranAmo(Account_No)
    elif choice == '3':
        sql = "select count(Account_No) from loan where Account_No=%s"
        data = (Account_No,)
        cur = con.cursor()
        cur.execute(sql, data)
        result = cur.fetchone()
        if result[0] != 0:
            show_loan(Account_No)
        else:
            print("Sorry! You have loan in our bank.")

    elif choice == '4':
        transaction(Account_No)
    elif choice == '5':
        updateAc(Account_No)
    elif choice == '6':
        print("Dear Customer, Thank you for using our banking system. See you soon. Take care. Bye")
        return 0
    else:
        print("Wrong input, Try again.")
        # customer(Account_No)


########################################################

def admin():
    print('''
    1. Create Branch
    2. Show Branches
    3. Approval request
    4. Exit
    ''')
    choice = input("Enter Task No: ")
    if choice == '1':
        createBr()
    elif choice == '2':
        show_br()
    elif choice == '3':
        print("we will work in this function in future")
        admin()
    elif choice == '4':
        print("Dear admin. Thank you to use our banking system. Take care. Bye")
        return 0
    else:
        print("Wrong input, Try again.")
        admin()


########################################################
def LogIn():
    print("\tWelcome to bank of ABC")
    print("====================================")
    print("\t\t Start Login\n")
    while True:
        Account_No = AC()  # input("Enter Your Account NO: ")
        sql = "select count(Account_No) from log_info where Account_No=%s"
        data = (Account_No,)
        cur = con.cursor()
        cur.execute(sql, data)
        result = cur.fetchone()
        if result[0] != 0:
            break
        else:
            print("Sorry! The account number doesn't exist. Please try again.")
    while True:
        Account_pass = Pass()
        sql = "select count(Account_Pass) from log_info where Account_Pass=%s"
        data = (Account_pass,)
        cur = con.cursor()
        cur.execute(sql, data)
        result = cur.fetchone()
        if result[0] != 0:
            break
        else:
            print("Sorry! The account password number doesn't match. Please try again.")

    sql = "SELECT account_type FROM log_info WHERE Account_No = %s and Account_pass = %s;"

    data = (Account_No, Account_pass)
    cur = con.cursor()
    cur.execute(sql, data)
    result = cur.fetchone()
    # print(result)
    if result[0] == 'Admin' or result[0] == 'admin':
        print("\n\n\t\tWelcome to Admin Section\n.........................................")
        admin()
    elif result[0] == 'Officer' or result[0] == 'officer':
        print("\n\n\t\tWelcome to Officer Section\n.........................................")
        Officer()
    elif result[0] == 'customer' or result[0] == 'Customer':
        customer(Account_No)
    else:
        print("Wrong input, Try again.")
        LogIn()


LogIn()
