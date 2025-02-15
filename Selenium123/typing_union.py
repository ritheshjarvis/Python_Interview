"""
arg: Union[argType1, argType2] -> To pass two types of argument type to a single argument
"""

from typing import Union

def element_to_be_clickable(mark: Union[WebElement, tuple[str, str]]):
    pass


"""
mark: → This is the function parameter.
Union[WebElement, Tuple[str, str]] → This is a type hint, meaning mark can accept:
A WebElement object (i.e., an already located Selenium123 element).
A tuple of two strings (By.<METHOD>, "locator") (i.e., a locator strategy like By.ID, "submit-button").
"""


# Example 1
def element_to_be_clickable(
    mark: Union[WebElement, Tuple[str, str]]
) -> Callable[[WebDriverOrWebElement], Union[Literal[False], WebElement]]:
    """An Expectation for checking an element is visible and enabled such that
    you can click it.

    element is either a locator (text) or an WebElement
    """

    # renamed argument to 'mark', to indicate that both locator
    # and WebElement args are valid
    def _predicate(driver: WebDriverOrWebElement):
        target = mark
        if not isinstance(target, WebElement):  # if given locator instead of WebElement
            target = driver.find_element(*target)  # grab element at locator
        element = visibility_of(target)(driver)
        if element and element.is_enabled():
            return element
        return False

    return _predicate


# Example 2
def func1(arg1 : Union[int, str], arg2 : Union[int, str]):
    if isinstance(arg1, int) and isinstance(arg2, int):
        print("The Sum is: ", arg1+arg2)
    else:
        print("The concatination is: ", arg1+arg2)


func1(3, 7) # The Sum is: 10
func1('rithesh', 'brao') # The concatination is: ritheshbrao