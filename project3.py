def email_strip(email):
    """
    This function takes an email address as input and returns the username and domain name as a tuple.
    """
    username = email[: email.index("@")]
    domain_name = email[email.index("@") + 1 :]
    print(f"Your user name is '{username}' and your domain is '{domain_name}'")

email_strip("gabrielmagno.ryan@gmail.com")
