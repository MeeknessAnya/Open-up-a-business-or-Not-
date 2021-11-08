print('-------------------------Open or Not!!!-----------------------')

name = input("What is your name? ")
print("Welcome to Harvard Business Service Inc, " + name + "! Determine if you can open that business or not!!!")

print("\n")
reason = input("Hi " + name + ", can you tell us why you want to open a business? ")
print('Great!')

print("\n")
print('---------------------------SKILLS----------------------------')

print("You'd be asked for five skills that you have, please enter them below")

basicSkills = ['communication', 'leadership', 'teamwork', 'time management', 'creativity', 'stress management', 'analytical thinking']

skills = []
count = 0
skill = input('Type in one skill: ')
skills.append(skill.lower())

while skill != "":
  skill = input('Type in another skill: ')
  skills.append(skill.lower())
  count += 1
  if count == 4:
    break
  else:
    continue
print("--------Thank You!!--------")

isNotIn = False
for skill in skills:
  if skill in basicSkills:
    isNotIn = False
    break
  else:
    isNotIn = True
    continue

#average cost of opening such business.
businessTypes = {'Service Business': 10000, 'Retailing': 7000, 'Intermediary': 3000, 'Producing': 50000}

if isNotIn:
  print("Awwwwww. You'd have to learn these important skills first!")
  print(basicSkills)
  print("Please check back later")
  print("Thank you for your time!!")
else: 
  print("You are on point! You've got the skills. Let's move on.")
  print("-----------------------------------------------------------")
  print("BUSINESS TYPES: Service Business, Retailing, Intermediary, Producing")

  businessType = input('What type of business do you plan to open? This will determine capital!!! ')

  business = input('Please enter the specific business: ')

  capital = int(input("And how much capital have you got? "))

  payroll = int(input("What's the estimated total annual amount you are willing to pay employees? "))

  if capital < (businessTypes[businessType] + payroll):
    print("Hey. You have little capital!, please earn more..")
    print("You shouldn't open a business at this time")
    print("Please check back later. Thank you for your time!!")
  elif capital == (businessTypes[businessType] + payroll):
    print("Just equal!! Please earn more however")
    print("Please check back later. Thank you for your time!!")
  else:
    print("Yay, you've got capital!, please continue")
    print("-------------------------------------------------------------")

    partner = input("A partnership or not? yes/no ")

    if partner == 'no':
      print("Hmmm! You should be prepared for challenges and risks that you will face")
    else:
      print("Also great!. Having a helping hand is good. Be cautious however!!")
    print("\n")
    location = input("Have a good location as headquarters yet? yes/no ") 

    if location == 'no':
      print("Having a suitable location is important, try to get one :)")
      print("You shouldn't open a business at this time")
      print("Please check back later. Thank you for your time!!")
    else:
      print("Sounds great. Good location means a better market")
      print("---------------------------------------------------------")

      experience = input('From your research, have you got experience? yes/no ')

      if experience == 'no':
        print("Some bit of experience is needed. You do not want to run into a loss")
        print("You shouldn't open a business at this time")
        print("Please check back later. Thank you for your time!!")
      else:
        print("It is great to know you're familiar with the ropes of this business")
        print("\n")
        target = input("Have you got your target demographics of the business? yes/no ")

        if target == 'no':
          print("The target customers should be priority. You should have this")
          print("You shouldn't open a business at this time")
          print("Please check back later. Thank you for your time!!")
        else:
          print("Good!!!")
          print("\n")
          credit = input("Do you have a good credit? yes/no ")

          if credit == 'no':
            print("Good credit ensures easy access to loans and other benefits. For a business to run, good credit is needed")
            print("You shouldn't open a business at this time")
            print("Please check back later. Thank you for your time!!")
          else:
            print("Yay!! Good credit comes with various benefits and perks to help businesses")

            taxes = input("Are you prepared to pax income tax, which is 10% of your income? yes/no ")

            if taxes == 'no':
              print("You can't start a business without preparing for taxes")
              print("You shouldn't open a business at this time")
              print("Please check back later. Thank you for your time!!")
            else:
              print("Great. You are almost there.") 
              print("\n")
              vision = input("You've passed all tests so far :) ; Please enter the vision for your business")
              print("\n")
              print("Congratulations. You can definitely start the " + business + "business")
              print("Goodluck!! Thank you for your time!!")

              print("--------------------THE VISION--------------------")
              print(vision)