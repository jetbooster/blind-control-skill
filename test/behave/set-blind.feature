Feature: set-blind
  Scenario: set blind to zero
    Given an English speaking user
      When the user says "set the office blind to 0"
      Then "blind-control-skill" should reply with "Moving blind to 0"
  Scenario: set blind to ten
    Given an English speaking user
      When the user says "move bedroom blind to 10"
      Then "blind-control-skill" should reply with "Moving blind to 10"