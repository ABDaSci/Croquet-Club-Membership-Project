applications = [[58, 20], [45, 2], [61, 12], [37, 6], [40, 40], [21, 21]]

def Croquet_Applications(Applications_list):
    membership = []
    for applicant in Applications_list:
        age, handicap = applicant[0], applicant[1]
        
        if ((-2 > handicap) or (handicap > 26)):
            applicant = "Out of Range"
            membership.append(applicant)
            continue
        
        if ((age >= 55) and (7 <= handicap <= 26)):
            applicant = "Senior"
            membership.append(applicant)
            
        elif ((age < 55) or (-2 <= handicap < 7)):
            applicant = "Open"
            membership.append(applicant)

        

    return membership

print(Croquet_Applications(applications))