@echo off

call :main
endlocal

:generateStubs
    omniidl -bpython -Wbmodules=utility.corbaModules -Wbstubs=utility.corbaStubs UIControllers.idl
    omniidl -bpython -Wbmodules=utility.corbaModules -Wbstubs=utility.corbaStubs GameService.idl
    omniidl -bpython -Wbmodules=utility.corbaModules -Wbstubs=utility.corbaStubs PlayerService.idl
    omniidl -bpython -Wbmodules=utility.corbaModules -Wbstubs=utility.corbaStubs ProgramUtilities.idl
    
    goto :eof

:main
    if exist utility\ (
        echo Deleting existing dir
        rd utility /s /q
    )
    mkdir utility\corbaStubs
    mkdir utility\corbaModules
    call :generateStubs
    echo Stubs Generated