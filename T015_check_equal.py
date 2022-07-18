#Adam Saunders (101217748) (Reviewer)
#Owen Petersen (101233850) (Reviewer)
#Isaac Walberg (101234320) (Reviewer)
#Fiona Cheng (101234672) (Compiler)

def check_equal(description: str, expected, outcome) -> bool:
    """
    Returns True if outcome and expected have the same type and are equal.
    Prints to the console whether or not the test case for a function specified by "description" passed or failed.
    Developed by Fiona Cheng (101234672)
    
    >>>check_equal("next_num(1)", 2, next_num(1))
    Testing: next_num(1)
    Expected outcome: 2 	Actual outcome: 2
    TEST PASSED
    True
    
    >>>check_equal("next_num(1)", 2, next_num(1))
    Testing: next_num(1)
    Expected outcome: 2 	Actual outcome: 3
    TEST FAILED 
    Values do not match.
    False
    
    >>>check_equal("next_num(1)", 2, str(next_num(1)))
    Testing: next_num(1)
    Expected outcome: 2 	Actual outcome: 2
    TEST FAILED 
    Types do not match. Expected type: 'int' Outcome type: 'str'
    False
    """
    outcome_type = str(type(outcome)).strip('<class> ')
    expected_type = str(type(expected)).strip('<class> ')

    print("Testing:", description)
    print("Expected outcome:", expected, "\tActual outcome:", outcome)

    if outcome_type != expected_type: #checks types
        print("TEST FAILED", "\nTypes do not match. Expected type:", expected_type, "Outcome type:", outcome_type, '\n')
        return False

    if outcome_type == 'float': #compares float values
        if abs(outcome - expected) > 0.001:
            print("TEST FAILED", "\nValues do not match.\n")
            return False
    else:
        if outcome != expected: #compares non-float values
            print("TEST FAILED", "\nValues do not match.\n")
            return False

    print("TEST PASSED\n")
    return True