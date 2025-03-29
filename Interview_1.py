from typing import Final, final

MY_CONSTANT: Final[int] = 10

@final
class BaseClass:
    def my_method(self) -> None:
        print("Base method")

class SubClass(BaseClass):
    # The following line will cause a type checking error
    # def my_method(self) -> None:
    #     print("Subclass method")
    pass

# The following line will cause a type checking error
MY_CONSTANT = 20