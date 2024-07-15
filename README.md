# task_4_calculator

This is my fourth task at Mainflow and Services.

Here's a breakdown of what each part of the code does:

🌠Function Definitions:

-add(x, y): Returns the sum of x and y.
-subtract(x, y): Returns the difference of x and y.
-multiply(x, y): Returns the product of x and y.
-divide(x, y): Returns the quotient of x and y, with a check to prevent division by zero.

🌠Helper Functions:

-get_number(prompt): Prompts the user to enter a number, validates the input, and returns it.
-get_operation(): Prompts the user to choose an operation (+, -, *, /) and validates the input.

🌠Main Calculator Function:

-calculator(): The main function that runs the calculator. It:
-Greets the user.
-Continuously prompts the user for numbers and an operation.
-Performs the chosen operation and displays the result.
-Asks if the user wants to perform another calculation, and exits if they don't.

🌠Script Entry Point:

-if __name__ == "__main__":: Ensures that calculator() runs only if the script is executed directly, not when imported as a module
