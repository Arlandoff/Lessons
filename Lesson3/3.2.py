
def pers_info(name, surname, year, city, email, telephone):
    return f"Name -{name}; Surname - {surname}; Year - {year}; City -{city}; Email -  {email}; Telephone - {telephone}"


print(pers_info(name=input("enter name: "), surname=input("enter surname: "), year=input("enter year: "),
                city=input("enter city: "), email=input("enter email: "), telephone=input("enter telephone: ")))
