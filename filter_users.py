import json

def filter_users_by_name(name):
    """filters for a given name

    Args:
        name (str): name to search for
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """filters users by a given age

    Args:
        age (int): age to filter by
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["age"] == age]
    
    for user in filtered_users:
        print(user)


def filter_by_email(email):
    """filters users by a given email

    Args:
        age (str): email to filter by
    """
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["email"] == email]
    
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by?: ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter by: "))
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter by: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")