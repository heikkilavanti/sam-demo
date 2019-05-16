*** Settings ***
Library          TestLibrary.py

*** Variables ***
${task_id}  = ""

*** Test Cases ***
No tasks found before tests are run
    ${response_code}    ${response_json}    Get all tasks
    Should Be Equal As Integers    404    ${response_code}

Create Task table
    [Tags]    critical
    ${response_code}    ${response_json}    Create Task table
    Should Be Equal As Integers    201    ${response_code}

Create task
    [Tags]    critical
    ${response_code}    ${response_json}    Create task    My First Task    Do the dishes
    Should Be Equal As Integers    201    ${response_code}

Only one task found
    ${response_code}    ${response_json}    Get all tasks
    Should Be Equal As Integers    200    ${response_code}
    ${length}=    Get Length    ${response_json}
    Should Be Equal As Integers    1    ${length}
    Set Global Variable    ${task_id}    ${response_json[0]['taskId']}

Delete task
    ${response_code}    ${response_json}     Delete task    ${task_id}
    Should Be Equal As Integers    204    ${response_code}
     ${length}=    Get Length    ${response_json}
     Should Be Equal As Integers    0    ${length}

No tasks found after deletion
    ${response_code}    ${response_json}    Get all tasks

Delete Task table
    ${response_code}    ${response_json}    Delete task table
    Should Be Equal As Integers    204    ${response_code}