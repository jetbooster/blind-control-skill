Feature: close-blind
  Scenario: close bedroom blind
    Given an English speaking user
      When the user says "close bedroom blind"
      Then "blind-control-skill" should reply with "closing bedroom blind"
  Scenario: close bedroom blind
    Given an English speaking user
      When the user says "close office blind"
      Then "blind-control-skill" should reply with "closing office blind"