*** Settings ***
#Suite Setup       Pre_Check
#Suite Teardown    Post_Check
Test Timeout      20 minutes
Library           OperatingSystem
Library           download_confirm.py

*** Variables ***
${file_cksum}  8951f6406eff66dcf70a0af7b9f4946c
*** Test Cases ***
#ID_DWN_TC001
    #[tags]      Download file from Google drive
    #[Documentation]    Validate the file is downloaded and exists
    #...
    #...    Test case title - ID_DWN_TC001

    #${check_dwn}= download file from google drive   download_url  output_path


ID_DWN_TC002
    [tags]      Check File Exists post download
    [Documentation]    Validate the file is downloaded and exists
    ...
    ...    Test case title - ID_DWN_TC002

    ${fileExists}=    OperatingSystem.File Should Exist   star.png
    Run Keyword If    ${fileExists} is True    Log To Console    Exists!

ID_DWN_TC003
    [tags]      Check MD5Sum of downloaded file
    [Documentation]    compare the checksum of downloaded file with uploaded file
    ...
    ...    Test case title - ID_DWN_TC003

    ${checksum}=    md5sum   star.png
    log    ${checksum}
    Should Be Equal  ${checksum}  ${file_cksum}

