if (NOT EXISTS "D:/MyFolder/AltSTU_repo/7_sem/Computer-graphics__Andreeva/lab2/Graphic-master/cmake-build-debug-mingw/install_manifest.txt")
    message(FATAL_ERROR "Cannot find install manifest: \"D:/MyFolder/AltSTU_repo/7_sem/Computer-graphics__Andreeva/lab2/Graphic-master/cmake-build-debug-mingw/install_manifest.txt\"")
endif(NOT EXISTS "D:/MyFolder/AltSTU_repo/7_sem/Computer-graphics__Andreeva/lab2/Graphic-master/cmake-build-debug-mingw/install_manifest.txt")

file(READ "D:/MyFolder/AltSTU_repo/7_sem/Computer-graphics__Andreeva/lab2/Graphic-master/cmake-build-debug-mingw/install_manifest.txt" files)
string(REGEX REPLACE "\n" ";" files "${files}")
foreach (file ${files})
    message(STATUS "Uninstalling \"$ENV{DESTDIR}${file}\"")
    execute_process(
        COMMAND C:/Program Files/JetBrains/CLion 2022.2.3/bin/cmake/win/bin/cmake.exe -E remove "$ENV{DESTDIR}${file}"
        OUTPUT_VARIABLE rm_out
        RESULT_VARIABLE rm_retval
    )
    if(NOT ${rm_retval} EQUAL 0)
        message(FATAL_ERROR "Problem when removing \"$ENV{DESTDIR}${file}\"")
    endif (NOT ${rm_retval} EQUAL 0)
endforeach(file)

