#!/user/bin/python3
"""defining a locked class."""


class LockedClass:
    """
    prevent the user from instantiating new lockedclass attributes
    for anything but attributes called 'first name'
    """
    
    __slots__ = ["first_name"]
