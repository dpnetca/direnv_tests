# Environmental variable secrets test


This started as a simple script to test usnig direnv (https://direnv.net/) for managing environmental variables for projects.
But, this doubled as a simple opportunity to do some unit test, TDD, and eventually CI practice and as such has evolved.

in my project directory I have enabled direnv with a .envrc file containing the following environmental variables:

    export secret1=monkeys
    export some_other_secret=cats
    dotenv .env

the .env file is simply:

    secret2=dogs
    secret3=mouse
