*** Settings ***
Library    RPA.Desktop

*** Tasks ***
Turn on wi-fi
    Log               Turning on wi-fi.
    Click             image:expand.png
    Wait For Element  image:not-connected.png
    Click             image:not-connected.png
    Wait For Element  image:eduroam.png
    Click             image:eduroam.png
    Wait For Element  image:connect.png
    Click             image:connect.png
    Log               Done.