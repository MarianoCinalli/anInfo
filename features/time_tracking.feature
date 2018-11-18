Feature: Time tracking

    Scenario: Add hours for task
        Given a task
        When one hour is added to the task
        Then the count should increase by one
