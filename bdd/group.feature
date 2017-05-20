Feature: Group Feature
  Description

  Scenario Outline: Add new group
    Given a group list
    Given a group list with <name>, <header>, <footer>
    When I add a new group to the list
    Then a new group list is equal to the old list with the new group

    Examples:
    | name | header  | footer |
    | bbjk | giukhkj | bhjjn |
    |23hjj | HHh     | HJH   |
    |оашп  | bjbi    | io3   |
