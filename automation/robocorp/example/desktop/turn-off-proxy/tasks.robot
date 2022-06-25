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
    Sleep             1

    TRY
        Wait For Element    image:now-on.png
        Press Keys    tab
        Press Keys    tab
        Press Keys    space
    EXCEPT  TimeoutException: No matches found for: image:now-on.png
        Log           Already off.
    END

    Press Keys        alt  f4
    Log               Done.