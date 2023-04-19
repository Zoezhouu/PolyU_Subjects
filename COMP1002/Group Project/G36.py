import smtplib
from email.mime.text import MIMEText
import calendar


# reference code
def print_format(content):
    """
    code adapted from COMP1002 lab9 
    date: 2021/11/14
    author: Dr. Kevin YUEN
    input: the content needed to format
    this function format the additional information provided to the user
    first finding the length of string in the first line
    and then adjust the length of space for string through reading file.
    these length is in accordance with the longest string inside a column
    """
    sizes = [len(a) for a in content[0].split(",")]  # finding the original length of words in the first line
    for cell in content:
        i = 0
        table = cell.split(",")
        for j in table:
            if len(j) > sizes[i]:
                sizes[i] = len(j)  # adjusting the word length to suit the longest word in the column
                i += 1
    for vac in content:
        n = 0
        vac_info = vac.strip().split(",")  # removing the newline brought by the original txt file
        for notes in vac_info:
            print("{0:{1}}".format(notes, sizes[n] + 2), end=" ")  # formatted printing with the space adjusted above
            n += 1
        print()  # keep formatting


def hksar_vac_info():
    """
    this function provides the user with the recognized vaccines by HKSAR Government
    help the user to identify the name of their vaccines
    also help the administrator to unify the vaccine name input by the student/staff
    which is easy for later analysis
    first open the file contain this information
    and use format function defined above to format the printing
    generate a list of vaccination for later check
    to make sure the user input the correct name of vaccine
    """
    info = open("HKSAR_Vac_Info.txt", "r")
    contents = info.readlines()
    print_format(contents)  # format the information by using the function defined above
    print('''\n*: Sinopharm Changchun/lanzhou/Chengdu Institute of Biological Product are responsible for the
    portion of vial filling and packing works for Sinopharm Beijing Institute of Biological Product.
    Vaccines provided by these manufacturers are the same as Sinopharm Beijing Institute of Biological Product.''')
    print("\nSource: https://www.coronavirus.gov.hk/pdf/list_of_recognised_covid19_vaccines.pdf")
    vaccine_list = list()
    for content in contents[1:]:
        content = content.strip().split(",")[1]
        # remove the newline after at each line in the file and split in terms of comma
        vaccine_list.append(content)  # generate a list of names of vaccination for later search and check
    return vaccine_list


def faculty_info():
    """
    this function provide the user with the PolyU faculties' and departments full name and their abbreviations
    advising the user to input the abbreviations of their faculties and departments
    still using the formatting function defined above
    """
    infile = open("polyu_faculty.txt", "r")
    fac = infile.readlines()
    print_format(fac)  # format printing
    print("if you are in 'others' faculty mentioned in table, please type 'NA'")  # mention special case
    infile.close()



def dept(faculty):
    """
    input: faculty user inputted before
    this function provide user with the department in each faculty and their abbreviations
    advising the user to input the abbreviations of their faculties and departments
    display the department information inside the chosen faculty
    still using the format function defined above
    """
    if faculty == "FAST":
        infile = open("FAST.txt", "r")
        fast = infile.readlines()
        print_format(fast)  # format printing
        infile.close()
    elif faculty == "FB":
        infile = open("FB.txt", "r")
        fb = infile.readlines()
        print_format(fb)
        infile.close()
    elif faculty == "FCE":
        infile = open("FCE.txt", "r")
        fce = infile.readlines()
        print_format(fce)
        infile.close()
    elif faculty == "FENG":
        infile = open("FENG.txt", "r")
        feng = infile.readlines()
        print_format(feng)
        infile.close()
    elif faculty == "FH":
        infile = open("FH.txt", "r")
        fh = infile.readlines()
        print_format(fh)
        infile.close()
    elif faculty == "FHSS":
        infile = open("FHSS.txt", "r")
        fhss = infile.readlines()
        print_format(fhss)
        infile.close()
    elif faculty == "NA":
        infile = open("NA.txt", "r")
        others = infile.readlines()
        print_format(others)
        infile.close()

# print(email_sending.__doc__)
def registration_id():
    """
    a part of registration function later
    this function allow user to input their student/staff id
    and check if this id already exist or not
    because we do not know what other type of students or staffs' id number look like
    here we assume all the input is valid except empty one
    :return: student/staff id input
    """
    f1 = open("student_info.txt", "r")
    lines = f1.readlines()
    ids = list()
    for line in lines:
        ids.append(line.split(",")[0])  # generate the list of id numbers already exist in the file
    while True:
        id_number = input("\nPlease input your student/staff ID:")
        if id_number.lower() in ids:  # unify the input, lower the alphabet in the id numbers, in order to compare
            print("The ID is already existed.")
        elif bool(id_number) is False:  # check if the input is empty
            print("not allow empty id")
        else:
            f1.close()
            return id_number.lower()  # unify the input, easy for later use


def registration_position():
    """
    a part of registration function later
    this function allows user to input their own position in PolyU
    whether they are student or staff
    check if the input is valid or not
    only 'student' and 'staff' are allowed as input
    give user opportunity to re-enter their information
    :return: position of user
    """
    while True:
        position = input("staff or student: ")
        if position == "student" or position == "staff":  # check the validity of the input
            # make sure it is 'student' or 'staff'
            return position
        else:
            print("\ninvalid input")
            print("can only input 'student' or 'staff' ")  # for user to re-input their information


def registration_department():
    """
    a part of registration function later
    this function allow user to input their department by input their faculty at first
    and display the department inside the faculty they choose
    and check if the user input valid name
    :return: department of the user
    """
    f = open("polyu_faculty.txt", "r")
    lines = f.readlines()
    faculty_name = list()
    for line in lines[1:]:
        line = line.strip().split(",")
        faculty_name.append(line[1])  # generate a list of faculty names to check the validity of user input
    print("You may refer to the table below to find your faculty abbr. in PolyU")
    while True:
        faculty_info()  # display the information of faculties inside PolyU
        faculty = input("Please input the abbreviation of your faculty: ")
        faculty = faculty.upper()  # unify the user input
        if faculty not in faculty_name:  # check if the input is valid
            print("\nnot valid faculty abbr")
            print("please check your spelling and input again")
        else:
            break
    if faculty == "SHTM":
        department = "SHTM"  # special case inside PolyU, faculty name is the department name
        return department  # return faculty name as department name directly
    elif faculty == "SD":
        department = "SD"
        return department
    else:
        f1 = open(faculty + ".txt", "r")
        cells = f1.readlines()
        department_name = list()
        for cell in cells[1:]:
            cell = cell.strip().split(",")
            # generate a list of department name inside chosen faculty to check validity
            department_name.append(cell[1])
        print("You may refer to the information below to find your department abbr. in PolyU according to your faculty")
        while True:
            # display the department full name and abbreviation inside the chosen faculty for user to refer
            dept(faculty)
            department = input("Please input the abbreviation of your department: ")
            department = department.upper()  # unify the user input
            if department not in department_name:  # check if the user input is valid or not
                print("\ninvalid input")
                print("please check your spelling")
            else:
                f.close()
                f1.close()
                return department


def registration_vaccine_status():
    """
    a part of registration function later
    ask the user if he or she receive full course of covid-19 vaccine
    check the validity of the input
    only 'Yes' or 'No' is allowed
    :return: vaccination status of user
    """
    while True:
        print("\nPlease indicate vaccination status")
        print("If you have received full course of covid-19 vaccine, please type 'Yes',")
        print("if not, please type 'No'")
        vac_status = input("Please indicate your vaccination status:")
        vac_status = vac_status.capitalize()  # unify the user input
        if vac_status == "Yes" or vac_status == "No":  # check the validity of user input
            return vac_status  # if valid, return directly
        else:
            print("\ninvalid input")  # if not, prompt user the error information and ask them to input again
            print("Only allow 'Yes' or 'No'")


def password():
    """
    a part of registration function later
    ask user to input their own password
    and confirm the password they input
    :return: password set up by the user
    """
    while True:
        pwd = input("\nPlease input your password: ")
        pwd2 = input("Please input your password again: ")  # confirm the password
        if pwd != pwd2:  # check if two passwords are same
            print("Not same password")  # if not, ask user to input again
            print("Please try it again")
        else:  # if they are same, return the password
            return pwd


def registration_name():
    """
    a part of registration function later
    ask user to input surname first
    and then input firstname
    in order to unify the input name
    :return: name of user
    """
    surname = input("\nPlease input surname: ")
    firstname = input("Please input first name: ")
    name = surname.upper() + " " + firstname  # combine the input name, with surname in upper case
    # easy for view
    return name


def registration():
    """
    ask user to input their basic information:
    student/staff ID
    student/staff name
    position
    department
    vaccination status
    through the functions defined above
    use a function called registration_confirm defined later to ask the user to confirm their input
    and ask them to change their information if anything is wrong
    prompt user with a successful information if they finish input
    :return:
    """
    stinfo = open("student_info.txt", "a")
    # accept the return from other functions
    id_number = registration_id()
    # enter name
    name = registration_name()
    # enter position
    position = registration_position()
    # enter department
    department = registration_department()
    # enter vaccination status
    vac_status = registration_vaccine_status()
    pwd = password()
    # registration confirm function to confirm the input of user
    id_number, name, position, department, vac_status = registration_confirm(id_number, name, position, department,
                                                                             vac_status)
    # write user input into file and using comma to separate them
    stinfo.write("{},".format(id_number.lower()))
    stinfo.write("{},".format(name))
    stinfo.write("{},".format(position.lower()))
    stinfo.write("{},".format(department.upper()))
    stinfo.write("{},".format(vac_status))
    stinfo.write("{} {}".format(pwd, "\n"))
    stinfo.close()
    print("You have successfully input your information, thanks for using our system")


def registration_confirm(id_number, name, position, department, vac_status):
    """
    a part of registration function above
    first print the information they input
    ask the user to input 'right' or 'wrong' when they found their information is right or wrong
    check the validity of user input
    only 'right' or 'wrong' is allowed
    ask the user to modify the part of information if they type 'wrong'
    after their modification
    display the information again to see if there is still anything wrong
    :return:id_number, name, position, department, vac_status
    """
    while True:
        print("\nPlease confirm your information")
        length = len("Student/Staff Name:")
        print("If any information is wrong, please type 'wrong'")
        print("If information is correct, please type 'right'")
        # format printing of information user input
        print("Student/Staff ID: {0:>{1}}".format(id_number, length - len("Student/Staff ID:") + len(id_number)))
        print("Student/Staff Name: {0:>{1}}".format(name, len(name)))
        print("position: {0:>{1}}".format(position, length - len("position:") + len(position)))
        print("department: {0:>{1}}".format(department, length - len("department:") + len(department)))
        print("vaccination status: {0:>{1}}".format(vac_status, len(vac_status)))
        confirm = input("\nPlease indicate whether your information is right or wrong: ")
        if confirm.lower() == "wrong":  # unify user input
            while True:  # display the information could be modified
                print("\nPlease select the information you want to amend")
                print("Please select the number of your option")
                print("1. student/staff ID")
                print("2. student/staff name")
                print("3. position")
                print("4. department")
                print("5. vaccination status")
                # let user quit the program if they mistakenly type wrong
                print("6. If everything is right, please type '6' to quit")
                amend = input("Please input your option: ")
                # call function defined before to ask the user to re-enter their information
                if amend == "1":
                    id_number = registration_id()
                    break  # jump out of loop to let the user confirm their information again
                # re-enter name
                elif amend == "2":
                    name = registration_name()
                    break
                # re-enter position
                elif amend == "3":
                    position = registration_position()
                    break
                # re-enter department
                elif amend == "4":
                    department = registration_department()
                    break
                # re-enter vaccination status
                elif amend == "5":
                    vac_status = registration_vaccine_status()
                    break
                # quit
                elif amend == "6":
                    break
                else:  # check the validity of user input
                    print("\ninvalid input")
                    print("only '1' '2' '3' '4' '5' or '6' is allowed")
                    print("please try again")
        elif confirm.lower() == "right":  # return the information if everything is correct
            return id_number, name, position, department, vac_status
        else:  # check the validity of user input
            print("\nnot a valid input")
            print("only right or wrong is allowed")

# print(email_sending.__doc__)
def email_sending(mail_receiver):
    """
    This was adpated from a post from xinran on 200220 to CSDN
    forum here: https://blog.csdn.net/weixin_42568012/article/details/104428927

    This function is designated to send reminding email to person who received CoronaVac vaccination and have passed
    180 days of their last dose.
    This function receive a variable called mail_receiver to get the email address of suitable student/staff,
    which is generated by a function called compare defined later
    this function use smtplib and email packages of python
    both of them are standard packages of python and do not need extra installation
    we use the SMTP service provided by gmail
    MIMEText module is used to send plain text
    :param mail_receiver: email address return from compare()
    """
    mail_host = "smtp.gmail.com"  # third party gmail SMTP service
    mail_sender = "1002gp36@gmail.com"
    password_mail = "comp1002a+"
    content = '''
Dear PolyU Student/Staff,
\nThanks for your effort in fighting COVID-19 by receiving COVID-19 Vaccination in time.
We noticed that you have received two dose of CoronaVac(Sinovac) 180 days ago.
According to the instruction given by Centre for Health Protection of  HKSAR Government, 
"for individuals who have received two does CoronaVac(Sinovac) vaccine
an additional Comirnaty(BioNTech) vaccine may provide a better immune response".
We highly recommend you to get a 3rd vaccination of Comirnaty(BioNTech) vaccine but personal preference is respected.
You could also choose to receive CoronaVac(Sinovac) vaccine as your additional vaccine.
\nFor more information, please visit https://www.covidvaccine.gov.hk/en/programme
\nThanks for your patience.
\nBest Regards.
        '''
    # creating an object
    message = MIMEText(content, "plain", "utf-8")
    message[
        "Subject"] = "Reminder of 3rd COVID-19 Vaccine for student/staff received two does of CoronaVac(Sinovac) " \
                     "Vaccine "  # title of email
    message["From"] = "PolyU Vaccine Tracking System"  # name of sender
    message["To"] = mail_receiver
    try:
        # creating an SMTP object
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # connect to smtp server
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_sender, password_mail)
        # using sendmail method to send email
        smtpObj.sendmail(mail_sender, mail_receiver, message.as_string())
        print("successful")
    except smtplib.SMTPException as e:
        print("error", e)


def compare():
    """
    in this function, we use datetime module,
    which is also a standard python package that does not need installation.
    this function add 180 days to the date input by the user and compare to the date of today
    to see if the date of today is later than the date of completing vaccination
    if it is later, check whether the person received CoronaVac vaccine and see if he or she has already
    received the third dose of vaccination
    finally return the email address of student/staff fulfills all the conditions
    """
    import datetime
    infile = open("vac_rec.txt", "r")
    times = infile.readlines()
    flag = len(times)
    for time in times:
        vaccine_time = time.split(",")[3]
        type_vaccine = time.split(",")[2]
        third_vaccine = time.strip().split(",")[4]
        # combine the student/staff id and the email domain name of polyu
        mail = time.split(",")[0] + "@connect.polyu.hk"
        # construct a datetime object from string that could be used to do calculation
        vaccine_time = datetime.datetime.strptime(vaccine_time.strip(), "%Y/%m/%d")
        # extract the date portion of datetime
        vaccine_time = vaccine_time.date()
        # obtain the date of today
        now_time = datetime.datetime.now().date()
        # add 180 to the date of completing vaccination
        re_time = vaccine_time + datetime.timedelta(180)
        # compare these two dates, check email type and vaccination status of third dose
        if now_time >= re_time and type_vaccine == "CoronaVac" and third_vaccine == "No":
            email_sending(mail)  # call email_sending function to send email reminder
        else:
            flag -= 1
    if flag == 0:
        print("No student/staff fulfills requirements")


def input_year():
    """
    this function allow user to input year of their vaccination
    since most covid-19 vaccination come in to the market in 2020
    we define the range of year to be no earlier than 2020
    and check if the user input numbers at first
    :return: year of user input
    """
    while True:
        year = input("Please input year of last dose of vaccination format(20yy)：")
        if year.isnumeric() is False:  # check if user input numbers
            print("invalid input")
            print("Only integer number is allowed")
        elif len(year) > 4:
            print("invalid input")
            print("only allow year in four digits")
        else:
            if int(year) < 2020 or int(year) > 9999:  # check the whether the year is earlier than 2020
                print("invalid input")
                print("Please check it again")
            else:
                return year


def input_month():
    """
    this function allows the user to input the month of their completing vaccine date
    check whether the user input number at first
    we define the range of input to be 1-12
    and check whether the user input is within this range
    :return: month input by user
    """
    while True:
        month = input("Please input month of last dose of vaccination (format MM): ")
        if month.isnumeric() is False:  # check whether the input is number or not
            print("Only integer number is allowed")
        elif len(month) != 2:
            print("only allow month in two digits")
        else:
            if int(month) > 12 or int(month) < 1:  # check whether the user input valid month
                print("invalid input")
                print("Please check your input")
            elif int(month) < 10 and len(month) > 1:
                # truncate the user input to keep formatting
                return month[1]
            else:
                return month
                


def input_day(year, month):
    """
    input: year and month
    this function allows user to input the exact day of completing vaccine
    in this function, we use calendar package
    this is also a python standard library which does not need extra installation
    check the whether the input day is a number at first
    and use function in calendar to display the month calendar according to the year and month input by the user
    check if the day is valid according to several conditions
    :return: day
    """
    print("Please refer to the calendar below")
    # set sunday as the starting day in the calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    # set year and month of the calendar
    monthcalendar = c.formatmonth(int(year), int(month))
    print(monthcalendar)  # display calendar
    while True:
        day = input("Please input day of last dose of vaccination (format: DD): ")
        if day.isnumeric() is False:  # check whether the input is number
            print("Only number is allowed")
        elif len(day) != 2:
            print("only allow input in two digits")
        else:
            # these months have 31 days, so the max value of day is 31
            if month == "1" or month == "3" or month == "5" or month == "7" or month == "8" or month == "10" or month == "12":
                if int(day) > 31:
                    print("invalid input")
                    print("please check your input")
                else:
                    # truncate the day input
                    if int(day) < 10 and len(day) > 1:
                        return day[1]
                    else:
                        return day
            # February has 29 days in leap years and 28 days in normal years
            elif month == "2" and int(year) % 4 == 0:
                if int(day) > 29:
                    print("invalid input")
                    print("Please check your input")
                else:
                    if int(day) < 10 and len(day) > 1:
                        return day[1]
                    else:
                        return day
            elif month == "2" and int(year) % 4 != 0:
                if int(day) > 28:
                    print("invalid input")
                    print("Please check your input")
                else:
                    if int(day) < 10 and len(day) > 1:
                        return day[1]
                    else:
                        return day
            else:
                if int(day) > 30:
                    print("invalid input")
                    print("Please check your input again")
                else:
                    if int(day) < 10 and len(day) == 2:
                        return day[1]
                    else:
                        return day

def vaccine_name_input(id_number):
    """
    input: id_number of user
    obtain a list of recognized vaccine list first to check the validity of user input
    ask the user to choose the reason if their input is not within the list
    if the user choose 'vaccine not within list'
    prompt user with notice and change their vaccination status in personal informaiton to 'No'
    and terminate the function
    if it is other reason
    ask user to check their input
    :return: vaccination name user input
    """
    print(
        "\nyou could refer to the recognized vaccination list provided by HKSAR Government for inputting vaccine name")
    while True:
        # obtain list of vaccination
        vaclist = hksar_vac_info()
        typevac = input("\nPlease input the name of vaccination: ")
        # check if the user input is within the list
        if typevac in vaclist:
            return typevac
        else:
            print("\nIf your vaccination is not within the recognized list, please type '1'")
            print("If not, type anything to pass")
            situation = input("Please type your option: ")
            # if not within, provide the user with notice
            if situation == "1":
                print("\nplease check the list and receive the recognized vaccination")
                print("your vaccination status will be automatically changed to 'no'")
                print("please contact administrator when you finish vaccination")
                # change vaccination status in personal information to 'No'
                change_vaccine_status(id_number)
                # terminate the function
                return 1
            # ask the user to check their spelling
            else:
                print("\nplease check your spelling")


def third_dose():
    """
    this function ask the user their vaccination status for whom receive CoronaVac vaccine
    the value return in this function will determine whether to send email reminder to the user
    check the validity of user input
    only allow 'Yes' or 'No'
    :return: the vaccination status of third dose
    """
    print("\nPlease indicate your vaccination status of third dose: ")
    while True:
        print("Input 'Yes' if you have already receive third dose of vaccination")
        print("Input 'No' if you haven't receive third dose of vaccination")
        third = input("Please indicate your status: ")
        # unify the user input
        third = third.capitalize()
        # check validity
        if third == "Yes" or third == "No":
            return third
        else:
            print("Invalid input")
            print("Only yes or no is allowed")


def write_vaccine_info(id_number, stuname, exist_id_list):
    """
    this function is a part of student_staff_login function
    this function call several functions for user to input their information and call function
    called vaccine_info_confirm to confirm the information they input
    it will first check if the id_number of user is in the file
    and ask the user to continue inputting his or her information if not in
    write the information into the file after confirm, separate them using comma
    """
    # check if the id number of user is in the file
    if id_number in exist_id_list:
        print("You have already submitted your vaccination")
        print("Please do not resubmit")
        # terminate the function if it already existed in the file
        return
    else:
        print("\nPlease input detailed vaccination information")
        vac_rec = open("vac_rec.txt", "a")
        # call vaccine_name_input function to input vaccine name
        typevac = vaccine_name_input(id_number)
        # if returning of vaccine_name_input is 1, which the user's vaccine is not recognized by HKSAR Government
        # the function will terminate
        if typevac == 1:
            return
        # if the return of vaccine_name_input is CoronaVac, ask the user to specify their status of third dose of
        # vaccination
        elif typevac == "CoronaVac":
            year = input_year()
            month = input_month()
            day = input_day(year, month)
            thirddose = third_dose()
            typevac, year, month, day, thirddose = vaccine_info_confirm(typevac, year, month, day, id_number, thirddose)
            vac_rec.write("{},".format(id_number))
            vac_rec.write("{},".format(stuname))
            vac_rec.write("{},".format(typevac))
            vac_rec.write("{}/{}/{},".format(year, month, day))
            vac_rec.write("{} {}".format(thirddose, "\n"))
            vac_rec.close()
            print("You have successfully input your information, thanks for using our system")
        # if returning value is not CoronaVac, set the status of third vaccination to NA, short for Not Applicable
        else:
            year = input_year()
            month = input_month()
            day = input_day(year, month)
            thirdose = "NA"
            typevac, year, month, day, thirddose = vaccine_info_confirm(typevac, year, month, day, id_number, thirdose)
            vac_rec.write("{},".format(id_number))
            vac_rec.write("{},".format(stuname))
            vac_rec.write("{},".format(typevac))
            vac_rec.write("{}/{}/{},".format(year, month, day))
            vac_rec.write("{} {}".format(thirddose, "\n"))
            vac_rec.close()
            print("You have successfully input your information, thanks for using our system")


def vaccine_info_confirm(typevac, year, month, day, id_number, thirddose):
    """
    ask user to confirm the vaccination information they input
    format the printing of vaccination information at first
    ask user to input 'right' or 'wrong'
    check their input at first
    ask the user the part of information he or she wants to change
    then display the information again to see if there is any other errors in the information
    """
    while True:
        print("\nPlease confirm your input")
        # format the information
        length = len("Month of last dose of vaccination: ")
        print("If any information is wrong, please type 'wrong'")
        print("If information is correct, please type 'right'")
        print("Type of your vaccination: {0:>{1}}".format(typevac,
                                                          length - len("Type of your vaccination:") + len(typevac)))
        print("Year of last dose of vaccination: {0:>{1}}".format(year,
                                                                  length - len(
                                                                      "Year of last dose of vaccination:") + len(
                                                                      year)))
        print("Month of last dose of vaccination: {0:>{1}}".format(month, len(month) + 1))
        print("Day of last dose of vaccination: {0:>{1}}".format(day,
                                                                 length - len("Day of last dose of vaccination:") + len(
                                                                     day)))
        print("Vaccination status of third dose: {0:>{1}}".format(thirddose,
                                                                  length - len("Vaccination status of third dose:")
                                                                  + len(thirddose)))
        print("Last infomation only applicable to student/staff receiving two dose of CoronaVac(Sinovac) vaccine")
        print("If you do not receive CoronaVac(Sinovac) vaccine, please ignore this information")
        confirm = input("\nPlease indicate whether your information is right or wrong: ")
        # check information
        if confirm.lower() == "wrong":
            # option to modify
            while True:
                print("\nPlease select the information you want to amend")
                print("1. Type of your vaccination")
                print("2. Year of last dose of vaccination")
                print("3. Month of last dose of vaccination")
                print("4. Day of last dose of vaccination")
                print("5. Vaccination status of third dose")
                print("This option only applicable to student/staff receiving two dose of CoronaVac(Sinovac) vaccine")
                print("If you do not receive CoronaVac(Sinovac) vaccine, please ignore this information")
                print("6. If everything is right, please type '6' to pass")
                # ask which part the user wants to amend
                amend = input("\nPlease input your option: ")
                # if the user change name of vaccination to other vaccination except CoronaVac
                # change information of third dose to NA
                if amend == "1":
                    typevac = vaccine_name_input(id_number)
                    if typevac != "CoronaVac":
                        thirddose = "NA"
                    break
                elif amend == "2":
                    year = input_year()
                    break
                elif amend == "3":
                    month = input_month()
                    break
                elif amend == "4":
                    day = input_day(year, month)
                    break
                # check if the name of vaccination is CoronaVac
                elif amend == "5":
                    if typevac == "CoronaVac":
                        thirddose = third_dose()
                    # if not, not allow the user to amend information in this part
                    else:
                        print("Please ignore this information since you do not receive CoronaVac(Sinovac) vaccine")
                        thirddose = "NA"
                    break
                elif amend == "6":
                    break
                else:
                    print("invalid input")
                    print("Please check your spelling")
        elif confirm.lower() == "right":
            return typevac, year, month, day, thirddose
        else:
            print("invalid input")
            print("only 'right or 'wrong' are allowed")
            print('please check your spelling again')


def exist_id():
    """
    this is a part of write_vaccine_info function
    generate a list of id number already in the vaccine record file
    :return: id number list
    """
    id_list = list()
    with open("vac_rec.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            id_list.append(line.split(",")[0])
        return id_list


def student_staff_login():
    """
    this function allow student and staff to login
    everytime the user has three times to try
    after login successfully and their vaccination status is 'Yes'
    ask them to input their vaccination information
    if their vaccination status is 'No'
    terminate the function
    """
    idn = list()
    psd = list()
    status = list()
    name = list()
    count = 1
    exist_id_list = exist_id()
    with open('student_info.txt', 'r') as f:
        info = f.readlines()
        # check if the file is empty
        if info:
            for lines in info:
                # read information from the file
                idn.append(lines.strip().split(',')[0])
                psd.append(lines.strip().split(',')[5])
                status.append(lines.strip().split(',')[4])
                name.append(lines.strip().split(',')[1])
            while True:
                # count the number of login
                count += 1
                # terminate the function if the user failed three times
                if count > 4:
                    print("Login failed more than three times, you are unable to login")
                    break
                id_number = input("\nPlease input id_number: ")
                password_login = input("Please input password: ")
                # unify the input for verification
                id_number = id_number.lower()
                # convert to boolean value to see if the input is empty
                id_b = bool(id_number)
                pw_b = bool(password_login)
                # check username and password
                if id_number in idn and password_login == psd[idn.index(id_number)]:
                    # check vaccination status
                    if status[idn.index(id_number)] == "Yes":
                        # if Yes, input vaccination information
                        student_name = name[idn.index(id_number)]
                        write_vaccine_info(id_number, student_name, exist_id_list)
                        break
                    else:
                        # if no, terminate the function
                        print("\nYou have not yet completed COVID-19 vaccination.")
                        print("You cannot input your vaccination information.")
                        print("You may receive vaccine later and contact administrator to update your information.")
                        print("Thanks for using our system.")
                        break
                # check if empty
                elif id_b is False or pw_b is False:
                    print("\nID number and password cannot be empty, Please enter ID number and password again")
                # ask the user to input again
                else:
                    print("id number or password is wrong")
                    print("Please input id_number and password again")
        else:
            print("File is empty, please input your information first")


def administrator_login():
    """
    this function allow administrator to login
    check if the input is empty at first
    everytime the user has three attempts
    if all failed, he or she is not allowed to login
    after login successful
    :return: administrator login successful
    """
    name = list()
    psd = list()
    count = 1
    with open('admin_info.txt', 'r') as f:
        info = f.readlines()
        # read information from the file
        for lines in info:
            name.append(lines.strip('\n').split(',')[0])
            psd.append(lines.strip('\n').split(',')[2])
    while True:
        # count the times the user attempts
        if count > 4:
            print("Login failed more than three times, you are unable to login")
            break
        id_number = input("\nPlease input admin_id: ")
        password = input("Please input password: ")
        # convert the user input to boolean value
        id_b = bool(id_number)
        pw_b = bool(password)
        count = count + 1
        # check the user input
        if id_number in name and password in psd:
            return "Administrator Login Successfully"
        # check if the user input is empty
        elif id_b is False or pw_b is False:
            print("ID number and password cannot be empty, Please enter ID number and password again")
        else:
            print("Please input id_number and password again")

def change_vaccine_status(id_number):
    """
    this is a part of vaccine_info_input function
    to change the vaccine status of user if their vaccine is not within the list
    :return:
    """
    f = open("student_info.txt")
    # read file
    lines = f.readlines()
    # check if the file is empty
    if lines:
        info = dict()
        for line in lines:
            line = line.strip().split(",")
            info[line[0]] = line[1:]
        # check the status if vaccine not within the list
        info[id_number][3] = "No"
        keys = list(info.keys())
        f1 = open("student_info.txt", "w")
        # write information to the file
        for key in keys:
            f1.writelines(
                "{0},{1},{2},{3},{4},{5}{6}".format(key, info[key][0], info[key][1], info[key][2], info[key][3],
                                                    info[key][4], "\n"))
        f.close()
        f1.close()
    else:
        print("file is empty")


def write_vaccine_file(keys, ori_info):
    """
    a part of update_vaccine_info function
    write the updated content to the file
    """
    f1 = open("vac_rec.txt", "w")
    for key in keys:
        f1.writelines("{},{},{},{},{}{}".format(key, ori_info[key][0], ori_info[key][1], ori_info[key][2],
                                                ori_info[key][3], "\n"))
    f1.close()


def read_vaccine_file():
    """
    a part of update_vaccine_info function
    read the information from the vaccine record function
    :return: the original information and the keys in the dictionary
    """
    f = open("vac_rec.txt", "r")
    # read information
    lines = f.readlines()
    ori_info = dict()
    # store the information into the list
    # use the student/staff id as key
    for line in lines:
        line = line.strip().split(",")
        ori_info[line[0]] = line[1:]
    keys = list(ori_info.keys())
    f.close()
    return ori_info, keys


def update_vaccine_info():
    """
    this function allow administrator to update the information in the file
    this function called several other functions:
    write_vaccine_file() to write updated information
    read_vaccine_file() to read the updated file
    update_vaccine_option_one(keys, ori_info) to update type of vaccination
    update_vaccine_option_two(keys, ori_info) to update the date of completing vaccine
    update_vaccine_option_three(keys, ori_info) to update the vaccination status of third dose of vaccination
    third function will only be executed if the type of vaccination is CoronaVac
    this function provides four choice to update:
    1. Type of Vaccination
    2. Date of Completion
    3. Vaccination status of third vaccination
    4. quit
    if the the user does not want to use the function again, he or she could type 4 to quit
    """
    while True:
        print("\nInformation available to update: ")
        print("1. Type of Vaccination")
        print("2. Date of Completion")
        print("3. Vaccination status of third vaccination")
        print("4. quit")
        up_info = input("Please input the number of option you want to update: ")
        # update the type of vaccination
        if up_info == "1":
            ori_info, keys = read_vaccine_file()
            ori_info = update_vaccine_option_one(keys, ori_info)
            # write the update information
            write_vaccine_file(keys, ori_info)
        # update the date of completion
        elif up_info == "2":
            ori_info, keys = read_vaccine_file()
            ori_info = update_vaccine_option_two(keys, ori_info)
            write_vaccine_file(keys, ori_info)
        # update the vaccination status
        elif up_info == "3":
            ori_info, keys = read_vaccine_file()
            ori_info = update_vaccine_option_three(keys, ori_info)
            write_vaccine_file(keys, ori_info)
        # quit the function
        elif up_info == "4":
            break
        else:
            print("invalid input")
            print("only '1' or '2' or '3' or '4' is allowed")

# update vaccination name
def update_vaccine_option_one(keys, ori_info):
    """
    part of the update_vaccine_info function
    allows the user to update vaccination name
    input: keys list and dictionary of original information with id number as keys
    check if the id number is in the file
    :return: updated dictionary ori_info
    """
    while True:
        id_number = input("Please input student/staff id: ")
        # check if the id number is in the list
        if id_number in keys:
            # ask user to input information
            new_type = vaccine_name_input(id_number)
            ori_info[id_number][1] = new_type
            # correct 3rd vaccination information
            if new_type == "CoronaVac":
                print("Vaccination of 3rd covid-19 vaccine should also be updated")
                ori_info_cv = update_vaccine_option_three(keys, ori_info)
                return ori_info_cv
            else:
                ori_info[id_number][3] = "NA"
                return ori_info
        else:
            print("id number not exist")

# update vaccination date
def update_vaccine_option_two(keys, ori_info):
    """
    part of the update_vaccine_info function
    allows the user to update the date of completing last dose of vaccination
    input: list of keys and dictionary of original information
    check if the id number is in the file
    ask the user to input the new year month and day of their date of their vaccination
    by calling the predefined functions:
    input_year(), input_month(), input_date()
    :return the updated dictionary ori_info
    """
    while True:
        id_number = input("Please input student/staff id: ")
        # check if the id_number is within the keys
        if id_number in keys:
            # ask the user to input the new information
            year = input_year()
            month = input_month()
            day = input_day(year, month)
            date = "{}/{}/{}".format(year, month, day)
            ori_info[id_number][2] = date
            return ori_info
        else:
            print("id number not exist")

# update information of 3rd vaccination
def update_vaccine_option_three(keys, ori_info):
    """
    part of the update_vaccine_info function
    allows the user to update the status of the third dose
    will only executed when the name of vaccination is CoronaVac
    input: list of keys and dictionary of original information
    check if the id number is in the file
    ask the user to input the new status of third dose
    by calling previously defined function third_dose()
    if they received CoronaVac vaccine
    otherwise set the vaccination status to NA
    :return the updated dictionary ori_info
    """
    while True:
        id_number = input("Please input student/staff id: ")
        # check the existence of id number
        if id_number in keys:
            # check the type of vaccination
            if ori_info[id_number][1] == "CoronaVac":
                # call third_dose function if vaccination is CoronaVac
                thirddose = third_dose()
                # update information
                ori_info[id_number][3] = thirddose
                return ori_info
            else:
                # set the status of third dose of vaccination to NA
                # dose not allow the update
                thirddose = "NA"
                ori_info[id_number][3] = thirddose
                print("update not available to person does not receive CoronaVac Vaccine")
                return ori_info
        else:
            print("id number not exist")


def update_personal_info():
    """
    this function allow the administrator to update the personal information of student/staff
    this function has 3 functions:
    because the the id number and name are written automatically into the vaccine record file
    we assume it is correct
    1. update Student/Staff Department
    2. update Student/Staff Vaccination Status
    3. quit
    if the user does not want to use anymore, type 3 to quit
    """
    f = open("student_info.txt")
    lines = f.readlines()
    # read information from the file first
    if lines:
        info = dict()
        for line in lines:
            line = line.strip().split(",")
            # uses id number as keys
            info[line[0]] = line[1:]
        # obtain the key list
        keys = list(info.keys())
        while True:
            print("\nInformation available to update: ")
            print("1. Student/Staff Department")  # here we assume the student/staff ID/Name to be correct
            print("2. Student/Staff Vaccination Status")
            print("3. quit")
            # user input their option
            choice = input("\nPlease select your option by typing the number: ")
            if choice == "1":
                # update student/staff department
                info = update_personal_option_one(keys, info)

            elif choice == "2":
                # update student/staff vaccination status
                info = update_personal_option_two(keys, info)
            elif choice == "3":
                break
            else:
                print("invalid input")
                print("only '1' '2' or '3' is allowed")
        # write the updated information to the file
        f1 = open("student_info.txt", "w")
        for key in keys:
            f1.writelines(
                "{0},{1},{2},{3},{4},{5}{6}".format(key, info[key][0], info[key][1], info[key][2], info[key][3],
                                                    info[key][4], "\n"))
        f1.close()
    else:
        print("file is empty")


def update_personal_option_one(keys, info):
    """
        this is a part of update_personal_info function
        input: dictionary of personal information and keys in the dictionary
        allows the user to update their department
        asks the user to input their id number
        and check if it exists
        then call predefined function registration_department() to input department information
        return the updated dictionary info
    """
    while True:
        id_number = input("Please input student/staff id: ")
        # check the existence of the id number
        if id_number in keys:
            # update new information
            department = registration_department()
            info[id_number][2] = department
            return info
        else:
            print("\nid_number not exist")
            print("spelling may be wrong")
            print("student/staff information not input")


def update_personal_option_two(keys, info):
    """
        this is a part of update_personal_info function
        allows the user to update their department
        asks the user to input their id number
        and check if it exists
        then call predefined function registration_vaccine_status() to input department information
    :param keys: keys in the dictionary
    :param info: dictionary of personal information
    :return: updated dictionary info
    """
    while True:
        id_number = input("Please input student/staff id: ")
        # check the existence of id number
        if id_number in keys:
            # update vaccination status
            status = registration_vaccine_status()
            info[id_number][3] = status
            return info
        else:
            print("id_number not exist")
            print("spelling may be wrong")
            print("student/staff information not input")


def personal_info_retrieval_format_head():
    """
    this function formats the head of retrieval personal information
    to form them in a row and in appropriate space
    """
    head1 = "student/staff ID"
    head2 = "student/staff Name"
    head3 = "position"
    head4 = "department"
    head5 = "Vaccination status"
    l1 = len(head1) + 2
    l2 = len(head2) + 2
    l3 = len(head3) + 2
    l4 = len(head4) + 2
    l5 = len(head5) + 2
    print()
    # format print
    # give each string appropriate space
    print("{0:{1}}".format(head1, l1), end="")
    print("{0:{1}}".format(head2, l2), end="")
    print("{0:{1}}".format(head3, l3), end="")
    print("{0:{1}}".format(head4, l4), end="")
    print("{0:{1}}".format(head5, l5))


def personal_info_retrieval_format(key, content):
    """
    this function formats the display of personal information retrieved
    :param key: id number used to search the information
    :param content: information need to format
    """
    head1 = "student/staff ID"
    head2 = "student/staff Name"
    head3 = "position"
    head4 = "department"
    head5 = "Vaccination status"
    # obtain the length of each header
    l1 = len(head1) + 2
    l2 = len(head2) + 2
    l3 = len(head3) + 2
    l4 = len(head4) + 2
    l5 = len(head5) + 2
    # format the display of information
    print("{0:<{1}}".format(key, l1), end="")
    print("{0:<{1}}".format(content[0], l2), end="")
    print("{0:<{1}}".format(content[1], l3), end="")
    print("{0:<{1}}".format(content[2], l4), end="")
    print("{0:<{1}}".format(content[3], l5))


def personal_info_retrieval():
    """
    this function allows the administrator to retrieve student/staff information
    administrator could retrieve information through:
    1. student/staff id
    2. student/staff name
    3. department
    4. position
    5. Mass search through vaccination status
    6. quit
    if the user does not want to use it, he or she can type 5 to quit
    """
    f = open("student_info.txt", "r")
    # read files
    # store the value read in a list
    lines = f.readlines()
    retrieval_info = dict()
    for line in lines:
        line = line.strip().split(",")
        # store the value in a dictionary
        # use the student/staff id as key
        retrieval_info[line[0]] = line[1:]
    # get keys in the list
    keys = list(retrieval_info.keys())
    while True:
        print("\nPlease input number of your option")
        print("1. Search individual information through student/staff ID")
        print("2. Search individual information through student/staff Name")
        print("3. Mass search through department")
        print("4. Mass search through position")
        print("5. Mass search through vaccination status")
        print("6. If you want to stop using, please input '6'")
        option = input("Please select one option: ")
        # retrieve information through student/staff ID
        if option == "1":
            personal_info_retrieval_option_one(keys, retrieval_info)
            f.close()
        # retrieve information through name
        elif option == "2":
            personal_info_retrieval_option_two(keys, retrieval_info)
            f.close()
        # retrieve information through department
        elif option == "3":
            personal_info_retrieval_option_three(keys, retrieval_info)
            f.close()
        # retrieve information through position
        elif option == "4":
            personal_info_retrieval_option_four(keys, retrieval_info)
            f.close()
        # retrieve information through vaccination status
        elif option == "5":
            personal_info_retrieval_option_five(keys, retrieval_info)
            f.close()
        # terminate the function
        elif option == "6":
            break
        else:
            print("invalid input")
            print("only '1' or '2' or '3' or '4' or '5' is allowed")
        f.close()


def personal_info_retrieval_option_one(keys, retrieval_info):
    """
    this is a part of personal_info_retrieval() function
    allows retrieval using student/staff id
    :param keys: keys in the dictionary of personal information, retrieval_info
    :param retrieval_info: dictionary of personal information

    """
    while True:
        idn = input("\nPlease input student/staff ID: ")
        print("Search result for student/staff ID '{}'".format(idn))
        # check if the existence of id number
        if idn in keys:
            # get the value in the dictionary according to the key
            content = retrieval_info.get(idn)
            # print head
            personal_info_retrieval_format_head()
            # print the information
            personal_info_retrieval_format(idn, content)
            break
        else:
            print("\nno result found")
            print("id number not exist")
            print("please check your input")


def personal_info_retrieval_option_two(keys, retrieval_info):
    """
    this is a part of personal_info_retrieval() function
    allows retrieval using name
    :param keys: keys in the dictionary of personal information, retrieval_info
    :param retrieval_info: dictionary of personal information
    """
    name_id = list()
    while True:
        # gets the name from the user
        name = registration_name()
        for key in keys:
            # search the corresponding  information using key
            if retrieval_info[key][0].lower() == name.lower():
                # append the name into the list
                name_id.append(key)
        # check if the name is empty
        if name_id:
            print("Search result for name '{}'".format(name))
            # print the head
            personal_info_retrieval_format_head()
            for i in name_id:
                # get the information of the name
                content = retrieval_info[i][0:4]
                # format the print
                personal_info_retrieval_format(i, content)
            break
        else:
            print("name not exist")


def personal_info_retrieval_option_three(keys, retrieval_info):
    """
    this is a part of personal_info_retrieval() function
    allows retrieval using department
    :param keys: keys in the dictionary of personal information, retrieval_info
    :param retrieval_info: dictionary of personal information
    """
    while True:
        depart_list = list()
        available_depart = list()
        for k in keys:
            # obtain the list of department in the file
            available_depart.append(retrieval_info[k][2])
        print("\ndepartment in the list: ")
        # print out the available list in the file
        # convert list to set to remove the duplicating cases
        for j in set(available_depart):
            print(j, end=" ")
        department = input("\nPlease input your department: ")
        for key in keys:
            # add the key of corresponding department in the list
            if retrieval_info[key][2] == department:
                depart_list.append(key)
        # check if the list is empty
        if depart_list:
            print("Search result for department '{}'".format(department))
            # print head
            personal_info_retrieval_format_head()
            for i in depart_list:
                # get the information according to the key in the list
                content = retrieval_info[i][0:4]
                personal_info_retrieval_format(i, content)
            break
        else:
            print("department not exist")


def personal_info_retrieval_option_four(keys, retrieval_info):
    """
    this is a part of personal_info_retrieval() function
    allows retrieval using position
    :param keys: keys in the dictionary of personal information, retrieval_info
    :param retrieval_info: dictionary of personal information
    """
    # ask user for the position he or she wants to search
    position = registration_position()
    position_list = list()
    for key in keys:
        # add the key of corresponding information to the list
        if retrieval_info[key][1] == position:
            position_list.append(key)
    # check if the list if empty
    if position_list:
        print("Search result for '{}'".format(position))
        # print the head
        personal_info_retrieval_format_head()
        for i in position_list:
            # print the content
            content = retrieval_info[i][0:4]
            personal_info_retrieval_format(i, content)
    else:
        print("no information found")


def personal_info_retrieval_option_five(keys, retrieval_info):
    """
    this function allows the retrieval through vaccination status
    :param keys: id number in the dictionary of vaccine information
    :param retrieval_info: dictionary of personal information
    """
    status_list = list()
    # ask user for the position he or she wants to search
    vaccine_status = registration_vaccine_status()
    for key in keys:
        if retrieval_info[key][3] == vaccine_status:
            status_list.append(key)
    if status_list:
        print("Search result for '{}'".format(vaccine_status))
        # print the head
        personal_info_retrieval_format_head()
        for i in status_list:
            # print content
            content = retrieval_info[i][0:4]
            personal_info_retrieval_format(i, content)


def vaccine_info_retrieval_format_head():
    """
    this function formats the head of retrieval vaccine information
    to form them in a row and in appropriate space
    """
    head1 = "student/staff ID"
    head2 = "student/staff Name"
    head3 = "Type of vaccination"
    head4 = "Date of completing vaccination"
    head5 = "Vaccination status of third dose(Only applicable to CoronaVac)"
    l1 = len(head1) + 2
    l2 = len(head2) + 2
    l3 = len(head3) + 2
    l4 = len(head4) + 2
    l5 = len(head5) + 2
    print()
    # give appropriate space to each information
    print("{0:{1}}".format(head1, l1), end="")
    print("{0:{1}}".format(head2, l2), end="")
    print("{0:{1}}".format(head3, l3), end="")
    print("{0:{1}}".format(head4, l4), end="")
    print("{0:{1}}".format(head5, l5))


def vaccine_info_retrieval_format(key, content):
    """
    this function formats the head of retrieval vaccine information
    to form them in a row and in appropriate space
    :param key: id number in the dictionary of vaccine information
    :param content: dictionary of vaccine information
    """

    head1 = "student/staff ID"
    head2 = "student/staff Name"
    head3 = "Type of vaccination"
    head4 = "Date of completing vaccination"
    head5 = "Vaccination status of third dose(Only applicable to CoronaVac)"
    l1 = len(head1) + 2
    l2 = len(head2) + 2
    l3 = len(head3) + 2
    l4 = len(head4) + 2
    l5 = len(head5) + 2
    # give each string appropriate space
    print("{0:<{1}}".format(key, l1), end="")
    print("{0:<{1}}".format(content[0], l2), end="")
    print("{0:<{1}}".format(content[1], l3), end="")
    print("{0:<{1}}".format(content[2], l4), end="")
    print("{0:<{1}}".format(content[3], l5))


def vaccine_retrieval():
    """
    this function allows the user to retrieve information in the vaccine record
    the user can retrieve information in several ways:
    1. student/staff id
    2. student/staff name
    3. type of vaccination
    give statistics of how many people receive this type vaccine
    4. quit
    if the user wants to stop using, he or she could terminate the function by typing 4
    """
    f = open("vac_rec.txt", "r")
    vacinfo = dict()
    lines = f.readlines()
    total_number = len(lines)
    for line in lines:
        line = line.strip().split(",")
        vacinfo[line[0]] = line[1:]
    keys = list(vacinfo.keys())
    while True:
        print("\nPlease select the search option by typing the number")
        print("1. student/staff ID")
        print("2. student/staff Name")
        print("3. Type of vaccination")
        print("4. quit")
        option = input("Please select your option: ")
        # retrieve through student/staff id
        if option == "1":
            vaccine_retrieval_option_one(keys, vacinfo)
            f.close()
        # retrieve through student/staff name
        elif option == "2":
            vaccine_retrieval_option_two(keys, vacinfo)
            f.close()
        # retrieve through the type of vaccination
        elif option == "3":
            vaccine_retrieval_option_three(keys, vacinfo, total_number)
            f.close()
        # quit
        elif option == "4":
            break
        # check if the input is valid
        else:
            print("invalid input")
            print("only number '1' '2' '3' '4' is allowed")


def vaccine_retrieval_option_one(keys, vacinfo):
    """
    this function allows the retrieval through id number
    :param keys: id number in the dictionary of vaccine information
    :param vacinfo: dictionary of personal information
    """
    idn = input("Please input student/staff ID: ")
    if idn in keys:
        print("Search result for student/staff ID {}".format(idn))
        # print the head
        vaccine_info_retrieval_format_head()
        # print the information using format function defined before
        content = vacinfo[idn]
        vaccine_info_retrieval_format(idn, content)
    else:
        print("id number not exist")
        print("please check your spelling")


def vaccine_retrieval_option_two(keys, vacinfo):
    """
    this function allows the retrieval through id number
    :param keys: id number in the dictionary of vaccine information
    :param vacinfo: dictionary of personal information

    """
    names = list()
    # allows the user to input name
    name = registration_name()
    for key in keys:
        # add key of corresponding in to the list
        if vacinfo[key][0].lower() == name.lower():
            names.append(key)
    # check if the name exists
    if names:
        print("Search result for name '{}'".format(name))
        # print the head
        vaccine_info_retrieval_format_head()
        for i in names:
            # print the content
            content = vacinfo[i]
            vaccine_info_retrieval_format(i, content)
    else:
        print("no such name exist")
        print("please check your spelling")


def vaccine_retrieval_option_three(keys, vacinfo, total_number):
    """
    this function allows the retrieval through type of vaccination
    :param keys: id number in the dictionary of vaccine information
    :param vacinfo: dictionary of personal information
    :param total_number:total number of people receive vaccination
    """
    available_vaccine = list()
    vaccine_name_list = list()
    while True:
        for k in keys:
            # obtain the vaccines exist in the file
            available_vaccine.append(vacinfo[k][1])
        print("available vaccine list")
        # print the vaccines
        # using set the remove the duplicates
        for j in set(available_vaccine):
            print(j, end="  ")
        vaccine_name = input("\nPlease input vaccination name: ")
        for key in keys:
            # search for the corresponding key with relevant information in the dictionary
            # add key to the list
            if vacinfo[key][1] == vaccine_name:
                vaccine_name_list.append(key)
        # check if the list is empty
        if vaccine_name_list:
            print("\nSearch result for vaccination type '{}'".format(vaccine_name))
            # print the head
            vaccine_info_retrieval_format_head()
            # get the number of people receive such vaccination
            number = len(vaccine_name_list)
            for i in vaccine_name_list:
                # print out the information
                content = vacinfo[i]
                vaccine_info_retrieval_format(i, content)
            # print out the statistics of dedicated vaccination name
            print("\n{0} among {1} number of people receive {2} vaccination".format(number, total_number, vaccine_name))
            break
        else:
            print("\nno such vaccination name in the list")


def personal_info_file_processing(filename):
    """
    this function reads the file
    assigns the id number to be the key in the dictionary
    :param filename: the name of file need to process
    return the dictionary and its keys
    """
    f = open(filename, "r")
    # read files
    lines = f.readlines()
    info = dict()
    for line in lines:
        # add the content into the list using id number as key
        line = line.strip().split(",")
        info[line[0]] = line[1:]
    keys = list(info.keys())
    return info, keys


def personal_vaccine_data_processing(vac_ana, keys):
    """
    this function count the total number of people, the number of people who receive vaccine
    and the number of people who doesn't receive vaccine in the whole file

    :param vac_ana: the dictionary contains vaccine information
    :param keys: id number in this dictionary as keys
    :return: number of people receive vaccine
             number of people doesn't receive vaccine
             total number of people
    """
    yes = 0
    no = 0
    for key in keys:
        # count the number of people who received vaccine
        if vac_ana[key][3] == "Yes":
            yes += 1
        # count the number of people who does not receive vaccine
        elif vac_ana[key][3] == "No":
            no += 1
    # count the total number of people
    total_number = len(keys)
    return yes, no, total_number


def department_info_processing(vac_ana, keys, department):
    """
    this function count the total number of people, the number of people who receive vaccine
    and the number of people who doesn't receive vaccine in a certian department
    :param vac_ana: the dictionary contains vaccine information
    :param keys: id number in this dictionary as keys
    :param department: department the user wants to analysis
    :return: number of people receive vaccine inside a department
             number of people doesn't receive vaccine inside a department
             total number of people inside a department
    """
    yes = 0
    no = 0
    count = 0
    for key in keys:
        # count people who receive vaccine inside a department
        if vac_ana[key][2] == department and vac_ana[key][3] == "Yes":
            yes += 1
            count += 1
        # count people who do not receive vaccine inside a department
        elif vac_ana[key][2] == department and vac_ana[key][3] == "No":
            no += 1
            count += 1
    return yes, no, count


def vaccine_analysis():
    """
    this function allows the user analyze the vaccination information inside polyU or a certain department
    this function provides four way to analyze:
    1. Percentage of complete/incomplete person in PolyU
    2. Percentage of total complete/incomplete person in a department
    3. Number of individuals of complete/complete person in PolyU
    4. Number of individuals of complete/complete person in a department
    5. quit
    if the user wants to stop using, he or she could type 5 to quit
    """
    vac_ana, keys = personal_info_file_processing("student_info.txt")
    while True:
        print("\nInformation available for analysis:")
        print("1. Percentage of complete/incomplete person in PolyU")
        print("2. Percentage of total complete/incomplete person in a department")
        print("3. Number of individuals of complete/complete person in PolyU")
        print("4. Number of individuals of complete/complete person in a department")
        print("5. quit")
        # choose the way to analyze
        option = input("\nPlease input the number of your option: ")
        # analyze the percentage of complete/incomplete person in PolyU
        if option == "1":
            vaccine_analysis_option_one(vac_ana, keys)
        # analyze the percentage of total complete/incomplete person in a department
        elif option == "2":
            vaccine_analysis_option_two(vac_ana, keys)
        # analyze the number of individuals of complete/complete person in PolyU
        elif option == "3":
            vaccine_analysis_option_three(vac_ana, keys)
        # analyze the number of individuals of complete/complete person in a department
        elif option == "4":
            vaccine_analysis_option_four(vac_ana, keys)
        elif option == "5":
            break
        else:
            print("invalid input")
            print("only number '1' '2' '3'  '4' or '5' is allowed")


def vaccine_analysis_option_one(vac_ana, keys):
    """
    this function allows the user analyze the percentage of complete/incomplete person in PolyU
    :param vac_ana: the dictionary contains vaccine information
    :param keys: id number in this dictionary as keys
    """
    while True:
        print("Please input two objects to compare")
        print("1. total number")
        print("2. completed individual")
        print("3. incomplete individual")
        print("4. If you want to quit, type '4' in both input")
        # input two statistics to compare
        division1 = input("\nPlease first option by typing the number: ")
        division2 = input("Please second option by typing the number: ")
        # check the input
        if division1 == "1" and division2 == "2" or division1 == "2" and division2 == "1":
            yes, no, total_number = personal_vaccine_data_processing(vac_ana, keys)
            # print the percentage of complete number and total number
            rate = yes / total_number
            print("\nPercentage of completed/total number of individual is {0:.2%}".format(rate))
            break
        elif division1 == "1" and division2 == "3" or division1 == "3" and division2 == "1":
            yes, no, total_number = personal_vaccine_data_processing(vac_ana, keys)
            rate = no / total_number
            # print the percentage of incomplete number and total number inside a department
            print("\nPercentage of incompleted/total number of individual is {0:.2%}".format(rate))
            break
        elif division1 == "4" or division2 == "4":
            break
        else:
            print("invalid input")
            print("only number '1', '2', '3', or '4' are allowed")


def vaccine_analysis_option_two(vac_ana, keys):
    """
    this function allows the user analyze the percentage of complete/incomplete person in a certain department
    :param vac_ana: the dictionary contains vaccine information
    :param keys: id number in this dictionary as keys
    """
    available_department = list()
    # add available departments inside the list
    for k in keys:
        available_department.append(vac_ana[k][2])
    print("\navailable department for analysis")
    # print out the available departments inside the file
    # using set to remove the duplicating information
    print(" ".join(list(set(available_department))))
    department = input("Please input department: ")
    # unify the input
    department = department.upper()
    # check if input department is available for analysis
    if department in available_department:
        print("\nPlease input two statistics to compare")
        print("1. total number of individuals in the department")
        print("2. completed individual in the department")
        print("3. incomplete individual in the department")
        division1 = input("Please first option by typing the number: ")
        division2 = input("Please second option by typing the number: ")
        # check the input
        if division1 == "1" and division2 == "2" or division1 == "2" and division2 == "1":
            yes, no, count = department_info_processing(vac_ana, keys, department)
            # print the percentage of complete number and total number inside a department
            rate = yes / count
            print("\nPercentage of completed/total number of individuals in {0} is {1:.2%}".format(department, rate))
        if division1 == "1" and division2 == "3" or division1 == "3" and division2 == "1":
            yes, no, count = department_info_processing(vac_ana, keys, department)
            # print the percentage of incomplete number and total number inside a department
            rate = no / count
            print("\nPercentage of incomplete/total number of individuals in {0} is {1:.2%}".format(department, rate))
    else:
        print("department not available for analysis")


def vaccine_analysis_option_three(vac_ana, keys):
    """
    this function allows the user analyze the number of complete/incomplete person in PolyU
    :param vac_ana: the dictionary contains vaccine information
    :param keys: id number in this dictionary as keys
    """
    yes, no, total_number = personal_vaccine_data_processing(vac_ana, keys)
    while True:
        print("Please select the statistics you want to analyze")
        print("1. total number")
        print("2. completed individual")
        print("3. incomplete individual")
        print("4. quit")
        division = input("\nPlease input your selection by typing the number: ")
        # total number of people inside polyU
        if division == "1":
            print("\nTotal number of people in PolyU is {}".format(total_number))
        # person receives vaccine inside polyU
        elif division == "2":
            print("\nNumber of people received vaccination in PolyU is {}".format(yes))
        # person who does not receive vaccine inside PolyU
        elif division == "3":
            print("\nNumber of people not received vaccination in PolyU is {}".format(no))
        # quit the function
        elif division == "4":
            break
        else:
            print("invalid input")
            print("only number '1' '2' '3' or '4' is allowed")


def vaccine_analysis_option_four(vac_ana, keys):
    """
    this function allows the user analyze the number of complete/incomplete person in a certain department
    :param vac_ana: the dictionary contains vaccine information
    :param keys: id number in this dictionary as keys
    """
    print("Please select the statistics you want to analyze")
    print("1. total number")
    print("2. completed individual")
    print("3. incomplete individual")
    print("4. quit")
    available_department = list()
    # add the department in the file to the list
    for k in keys:
        available_department.append(vac_ana[k][2])
    print("available department for analysis")
    # print out the list
    # use set to remove the duplicating information
    print(" ".join(list(set(available_department))))
    department = input("Please input department: ")
    # unify the input
    department = department.upper()
    yes, no, count = department_info_processing(vac_ana, keys, department)
    # check if the input department is in the file
    if department in available_department:
        print("Please select the statistics you want to analyze")
        print("1. total number")
        print("2. completed individual")
        print("3. incomplete individual")
        print("4. quit")
        while True:
            depart_pref = input("Please input your selection by typing the number: ")
            # total number of people inside a department
            if depart_pref == "1":
                print("Total number of people in department {0} is {1}".format(department, count))
            # number of people receives vaccine in a department
            elif depart_pref == "2":
                print("Number of people received vaccination in department {0} is {1}".format(department, yes))
            # number of people who does not receive vaccine in a department
            elif depart_pref == "3":
                print("Number of people not received vaccination in department {0} is {1}".format(department, no))
            elif depart_pref == "4":
                break
            else:
                print("invalid input")
                print("only number '1' '2' '3' or '4' is allowed")
    else:
        print("not in department list")


def main():
    """
    the control function of the whole program
    after execution
    the function provides three options:
    1. Student/Staff Registration
    2. Student/Staff Vaccination information input
    3. Administrator Login
    :return:
    """
    # welcoming message
    print("\nWelcome to PolyU Vaccination Tracking System")
    while True:
        # ask user whether to start or quit the program
        process = input("\nPlease input 'b' to begin or 'q' to quit the system: ")
        # check user input
        if process == "b":
            while True:
                print("\nPlease select:")
                print("\n1. Student/Staff Registration")
                print("If you never using this system before, please select this option to input your information")
                print("\n2. Student/Staff Vaccination information input")
                print("\n3. Administrator Login")
                print("\n4. quit")
                print("If you want to stop using, please type '4' to quit")
                action = input("Please input your option by typing the number of option: ")
                # check user input
                if action == "3":
                    # administrator login
                    userinfo = administrator_login()
                    break
                if action == "2":
                    # student staff login and vaccination information input if applicable
                    student_staff_login()
                elif action == "1":
                    # student/staff input their information
                    userinfo = "Student/Staff Registration"
                    break
                # quit function
                elif action == "4":
                    userinfo = "quit"
                    break
                else:
                    print("You should select one option.")
            if userinfo == "Administrator Login Successfully":
                while True:
                    # administrator options after login
                    print("\nPlease select one option by inputting the number of it")
                    print("1. update student/staff personal information")
                    print("2. retrieval student/staff personal information")
                    print("3. update student/staff vaccination information")
                    print("4. retrieval student/staff vaccination information")
                    print("5. Vaccination Information Analysis")
                    print("6. Email reminder of third dose of  COVID-19 Vaccine")
                    print("7. quit")
                    # check input
                    action = input("\nPlease input your option: ")
                    if action == "6":
                        # send email reminder to the person need third dose of vaccine
                        compare()
                    elif action == "3":
                        # update the vaccine information
                        update_vaccine_info()
                    elif action == "1":
                        # update the personal information
                        update_personal_info()
                    elif action == "2":
                        # retrieve the personal information
                        personal_info_retrieval()
                    elif action == "4":
                        # retrieve the vaccine information
                        vaccine_retrieval()
                    elif action == "5":
                        # vaccine information analysis
                        vaccine_analysis()
                    elif action == "7":
                        break
                    else:
                        print("invalid input. Please select again")
            elif userinfo == "Student/Staff Registration":
                # input student information
                print("\nPlease input your personal information")
                registration()
            # quit the program
            elif userinfo == "quit":
                break
        # quit the program
        elif process == "q":
            print("Thanks for using our system")
            break
        else:
            print("You should select one option, please select again.")



main()


# docstring:
# print(administrator_login.__doc__)
# print(change_vaccine_status.__doc__)
# print(compare.__doc__)
# print(department_info_processing.__doc__)
# print(dept.__doc__)
# print(email_sending.__doc__)
# print(exist_id.__doc__)
# print(faculty_info.__doc__)
# print(hksar_vac_info.__doc__)
# print(input_year.__doc__)
# print(main.__doc__)
# print(password.__doc__)
# print(personal_info_file_processing.__doc__)
# print(personal_info_retrieval.__doc__)
# print(personal_info_retrieval_format.__doc__)
# print(personal_info_retrieval_format_head.__doc__)
# print(personal_info_retrieval_option_five.__doc__)
# print(personal_info_retrieval_option_four.__doc__)
# print(personal_info_retrieval_option_two.__doc__)
# print(personal_info_retrieval_option_three.__doc__)
# print(personal_info_retrieval_option_one.__doc__)
# print(personal_vaccine_data_processing.__doc__)
# print(print_format.__doc__)
# print(read_vaccine_file.__doc__)
# print(registration.__doc__)
# print(registration_confirm.__doc__)
# print(registration_department.__doc__)
# print(registration_id.__doc__)
# print(registration_name.__doc__)
# print(registration_position.__doc__)
# print(registration_vaccine_status.__doc__)
# print(student_staff_login.__doc__)
# print(third_dose.__doc__)
# print(update_personal_info.__doc__)
# print(update_personal_option_one.__doc__)
# print(update_personal_option_two.__doc__)
# print(update_vaccine_info.__doc__)
# print(update_vaccine_option_one.__doc__)
# print(update_vaccine_option_two.__doc__)
# print(update_vaccine_option_three.__doc__)
# print(vaccine_analysis.__doc__)
# print(vaccine_analysis_option_one.__doc__)
# print(vaccine_analysis_option_two.__doc__)
# print(vaccine_analysis_option_three.__doc__)
# print(vaccine_analysis_option_four.__doc__)
# print(vaccine_info_confirm.__doc__)
# print(vaccine_info_retrieval_format.__doc__)
# print(vaccine_info_retrieval_format_head.__doc__)
# print(vaccine_name_input.__doc__)
# print(vaccine_retrieval.__doc__)
# print(vaccine_retrieval_option_one.__doc__)
# print(vaccine_retrieval_option_two.__doc__)
# print(vaccine_retrieval_option_three.__doc__)
# print(write_vaccine_file.__doc__)
# print(write_vaccine_info.__doc__)