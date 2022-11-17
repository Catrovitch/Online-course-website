*** Settings ***
Resource  resource.robot
Test Setup

*** Test Cases ***
Register User With Valid Username And Password
    Register  gandalf  thewhite123  thewhite123
    Click button  Create Account
