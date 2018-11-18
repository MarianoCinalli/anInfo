Feature: Time tracking

    Scenario: Add hours for task
        Given a task
        When one hour is added to the task
        Then the count should increase by one

   Scenario: Add hours to finished task
        Given a task with status done
        When trying to add an hour to a finished task
	Then the time should remain the same
