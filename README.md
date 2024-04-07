# CPSC 2030 (Lab_08)

Tuesday, April 9th

**Due**: By the end of the day (Monday, April 15th)

**Instructions**  
Write a program that prompts the user to enter 10 even numbers, ignoring any odd numbers entered, then prints out the array neatly.

You should satisfy the following requirements:
- Write a *function* that returns a *Boolean* (true if the passed parameter is an even number, and false if the number passed is odd).
- Prompt the user to enter an integer, and *if it is odd* (use your function in step #2!), store the number in an integer array.
- Continue to prompt the user until they enter 10 odd numbers (ignoring any even numbers, unless completing the optional task) and re-prompting them to enter an odd number.
- Print (neatly) the contents of the array.
- Use good programming style.

Optional Requirements (2 bonus points):
- Create an integer array that stores all even numbers entered by the user.
- Write a *function* that returns a *float* that shows the average of all even integers entered.
- After printing the contents of the odd integer array (in the requirements above), print the average of the even integer array and notify the user how many even numbers were entered.

Good Programming Style:
- File begins with a header containing Doxygen comments, including @file, brief description, @author, @date
- Uses #define or const variables for all constants.
- Variables are i) clearly named according to purpose; 2) declared at the beginning of the function; 3) initialized when declared; 4) commented on the same line when declared
- Code is commented for each task (not necessarily every line)
- Indentation is consistent inside each level of {} in if/for/while statements.
- Program exists with `return 0;`
