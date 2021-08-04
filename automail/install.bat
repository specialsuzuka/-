if exist "D:\\bin"(
    setx file_organizer D:\\bin
)else(
    md "D:\\bin"
    setx file_organizer D:\\bin
)
move dist\automail.exe D:\\bin