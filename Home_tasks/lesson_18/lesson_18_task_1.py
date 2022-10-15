"""Create a class method named `validate`, which should
be called from the `__init__` method to validate parameter
email, passed to the constructor. The logic inside the
`validate` method could be to check if the passed email
parameter is a valid email string.

"""


class EmailAddress:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    digits = '0123456789'
    local_symbols = "!#$%&'*+-/=?^_`{|}~"
    domain_symbol = '-.'

    def __init__(self, email_param):
        self.validate(email_param)
        self.email_param = email_param

    @classmethod
    def validate(cls, email_param):
        if type(email_param) != str:
            raise TypeError("Email must be a string.")

        a = email_param.split('@')

        if '@' not in email_param:
            raise TypeError("Separator '@' must be in email address.")

        if 64 < len(a[0]) < 1:
            raise TypeError('Local part can not be longer then 64 and shorter then 1 symbol.')

        if 255 < len(a[1]) < 4:
            raise TypeError('Domain part can not be longer then 255 and shorter then 4 symbols.')

        for i in a[0]:
            if i not in cls.alphabet and i not in cls.alphabet_upper \
                    and i not in cls.digits and i not in cls.local_symbols:
                raise TypeError("Wrong symbols in local part.")

        for i in a[1]:
            if i not in cls.alphabet and i not in cls.alphabet_upper \
                    and i not in cls.digits and i not in cls.domain_symbol:
                raise TypeError("Wrong symbols in domain part.")

        print(f'email {email_param} is right one.')


ea = EmailAddress('Griffindor@hogwarts.mw')
ea2 = EmailAddress('best@i.ua')
ea3 = EmailAddress('zero.hotmail.com')
ea4 = EmailAddress('one@com/.md')
