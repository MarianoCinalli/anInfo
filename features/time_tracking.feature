Feature: Time tracking

    Scenario: Add hours for task
        Given a task
        When one hour is added to the task
        Then the count should increase by one

   Scenario: Add hours to finished task
        Given a task with status done
        When trying to add one hour to a finished task
	Then the time should remain the same

   Scenario: Add hours to pending task
	Given a task with pending status
        When adding one hour
        Then one hour should be added
        And status should change to started

   Scenario: Add hours to task above max time for user in project
        Given a task for a jorge.bolco
        When trying to add hours above the maximum time for that user in the project
        Then the time for jorge.bolcos task should remain the same

   Scenario: Add negative hours
        Given a task with pending status for jorge.bolco
        When trying to add negative hours
        Then the time for the task should remain the same
