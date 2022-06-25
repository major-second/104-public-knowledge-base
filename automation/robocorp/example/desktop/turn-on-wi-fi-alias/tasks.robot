*** Settings ***
Library    RPA.Desktop

*** Tasks ***
Turn on wi-fi
    Log               Turning on wi-fi.
    Click             image:expand.png

    Wait For Element  image:not-connected.png
    ${not-con}=       Find Element    image:not-connected.png
    Click             ${not-con}

    Wait For Element  ocr:eduroam    timeout=3
    ${eduroam}=       Find Element    ocr:eduroam
    Click             ${eduroam}

    Wait For Element  image:connect.png
    ${connect}=       Find Element    image:connect.png
    Click             ${connect}

    Log               Done.