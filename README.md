# Password-Cracking-Application
This is a tool that attempts to crack passwords.

## Project Overview
Here's some features of the password cracker code:
Mask-Based Brute-Force Attack: Allows for pattern-based guessing, where only specific placeholders (?) are varied.
Custom Character Set: Allows you to define which characters to use for brute-force attacks.
Algorithm Selection: Enables the choice between MD5 and SHA-256 hashing.
Enhanced Logging and Reporting: Provides progress reports for each attack type.
Improved CLI Interface: Includes more options to select attack types and configurations easily.

## Features of the Code
### Explanation of Additions
mask_based_brute_force Function:
Allows pattern-based brute-force attempts, where each ? in the mask is replaced by a character from charset.
This is useful for cases where you have partial information about the password format.

Algorithm Flexibility:
The hash_password function now takes an algorithm parameter, allowing users to choose between MD5 and SHA-256.
In the main function, the user selects the hashing algorithm.

Character Set Customization:
The charset variable can be easily modified to include or exclude character types (e.g., only digits, lowercase letters).

User Input for Attack Configuration:
The main function prompts the user to choose an attack type, specify maximum password length for brute-force, select the dictionary file, or define a mask pattern.
Reporting:
Each attack method now logs start and end times, and the number of attempts, providing feedback on the process and performance.
