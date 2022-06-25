*** Settings ***
Library    RPA.Desktop
Library    RPA.Windows

*** Tasks ***
Turn off proxy
    Log               Turning off proxy.
    
    Press Keys        cmd
    Type Text         proxy settings
    Press Keys        enter
    Press Keys        cmd  up


    TRY
        Wait For Element    image:already-on.png
        Press Keys    tab
        Press Keys    tab
        Press Keys    space
    EXCEPT  TimeoutException: No matches found for: image:already-on.png
        Log           Already off.
    END

    Press Keys        alt  f4
    Log               Done.