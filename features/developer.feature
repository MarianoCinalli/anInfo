Feature: See tasks

    Scenario: Display tasks
        Given a user requests all tasks
        Then the user sees all tasks

    Scenario: Display jorge.bolco tasks
        Given jorge.bolco requests his tasks
        Then jorge.bolco sees his tasks

