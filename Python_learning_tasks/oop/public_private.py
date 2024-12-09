# Examples of Public and Private Access Modifiers:
# Public access modifier allows data to be publicly accessible
# while Private access modifier allows data to be hidden privately

class Person:
    # Public attribute
    public_attribute = 'Public'

    # Private attribute
    _private_attribute = 'Private'

    # Public method
    def public_method(self):
        print('This is a public method.')

    # Private method
    def _private_method(self):
        print('This is a private method.')

    # Public method that uses private attribute
    def access_private_attribute(self):
        print(self._private_attribute)

    # Private method that tries to access private attribute
    def _try_access_private_attribute(self):
        print(self._private_attribute)  # This will raise an AttributeError


