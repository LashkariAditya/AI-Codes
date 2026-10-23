#Take input such as name, percentage in 12th grade, stream in 12th, area of interest.Based on this suggest courses

def suggest_courses():
    name = input("Enter your name: ")
    percentage = float(input("Enter your percentage in 12th grade: "))
    stream = input("Enter your stream in 12th (Science/Commerce/Arts): ")
    area_of_interest = input("Enter your area of interest: ")

    print(f"\nHello {name}, based on your inputs, here are some course suggestions:\n")

    if stream.lower() == "science":
        if area_of_interest.lower() == "engineering":
            print("Suggested Courses: B.Tech, B.E., Diploma in Engineering")
        elif area_of_interest.lower() == "medical":
            print("Suggested Courses: MBBS, BDS, Nursing, Pharmacy")
        else:
            print("Suggested Courses: B.Sc. in various fields, Biotechnology, Environmental Science")
    
    elif stream.lower() == "commerce":
        if area_of_interest.lower() == "business":
            print("Suggested Courses: BBA, B.Com, MBA")
        elif area_of_interest.lower() == "finance":
            print("Suggested Courses: Chartered Accountancy (CA), Cost and Management Accountancy (CMA), Financial Planning")
        else:
            print("Suggested Courses: Economics, Business Analytics, Marketing")
    
    elif stream.lower() == "arts":
        if area_of_interest.lower() == "design":
            print("Suggested Courses: Bachelor of Design (B.Des), Fashion Design, Interior Design")
        elif area_of_interest.lower() == "media":
            print("Suggested Courses: Mass Communication, Journalism, Film Studies")
        else:
            print("Suggested Courses: Psychology, Sociology, Fine Arts")

    else:
        print("Invalid stream entered. Please enter Science, Commerce or Arts.")

    if percentage < 33:
        print("\nNote: Your percentage is below the passing criteria. Please consider improving your academic performance.")
    
suggest_courses()