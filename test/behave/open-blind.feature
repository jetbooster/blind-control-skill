Feature: open-blind
  Scenario: open bedroom blind
    Given an English speaking user
      When the user says "open bedroom blind"
      Then "blind-control-skill" should reply with "opening bedroom blind"
  Scenario: open bedroom blind
    Given an English speaking user
      When the user says "open office blind"
      Then "blind-control-skill" should reply with "opening office blind"