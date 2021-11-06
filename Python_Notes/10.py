#if applicant high income AND / OR good credit Eligible for loan

#AND: both
#OR: at least one
#NOT: opposit


has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")



has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
