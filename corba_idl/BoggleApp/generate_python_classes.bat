@echo off

call :main
endlocal

:generateStubs
    omniidl -bpython -Wbmodules=lexilogic/utility/corbaModules -Wbstubs=lexilogic/utility/corbaStubs UIControllers.idl
    omniidl -bpython -Wbmodules=lexilogic/utility/corbaModules -Wbstubs=lexilogic/utility/corbaStubs GameService.idl
    omniidl -bpython -Wbmodules=lexilogic/utility/corbaModules -Wbstubs=lexilogic/utility/corbaStubs PlayerService.idl
    omniidl -bpython -Wbmodules=lexilogic/utility/corbaModules -Wbstubs=lexilogic/utility/corbaStubs ProgramUtilities.idl
    
    goto :eof

:main
    if exist lexilogic\ (
        echo Deleting existing dir
        rd lexilogic /s /q
    )
    mkdir lexilogic\utility\corbaStubs
    mkdir lexilogic\utility\corbaModules
    call :generateStubs
    echo Stubs Generated