@Echo off
:: SetLocal
SET OldLine=initial_value_to_be_neglected
Rem Create name of output file
SET FileName=arp
SET OutFileAlt=%tmp%\arpAlt
SET OutFileAltAlt=%tmp%\arpAltAlt
SET FileExt=.txt
SET Infile=%tmp%\%FileName%%FileExt%
SET OutFile=%tmp%\%FileName%_NODUPL%FileExt%
echo. 2>%Infile%
echo. 2>%OutFile%
:Loop
:: Filing input file with current ARP tableIf NOT Exist %OutFile%
arp -a -v | findstr dynamic >> %Infile%
SET N=0;
SET J=1;
If Exist %OutFile% DEL %OutFile%
If Exist %OutFileAlt%%FileExt% DEL %OutFileAlt%%FileExt%
Rem Process file
sort %Infile% /O %Infile%
For /F "tokens=*" %%L In (%Infile%) Do SET Line=%%L&Call :NoDupL
EndLocal
GoTo flush
:err
Echo File %1 not found!
GoTo EOF
:NoDupL
If "%Line%" == "%OldLine%" GoTo EOF
Echo %Line%>>%OutFile%
SET OldLine=%Line%
GoTo EOF
:flush
del %Infile% /Q
rename %OutFile% %FileName%%FileExt%
GoTo FillDiff
:: Get IP addresses from the filtered ARP table
:FillDiff
For /F "tokens=1 delims= " %%L In (%Infile%) Do SET Line=%%L
GoTo CheckForDup
:: Checking for duplicate IP addresses for different MAC addresses in order to signal it
:CheckForDup
SET OldLine=initial_value_to_be_neglected
For /F "tokens=1 delims= " %%L In (%Infile%) Do SET Line=%%L&Call :DupL
GoTo flush2
:DupL
If "%Line%" == "%OldLine%" Echo %Line%>>%OutFileAlt%%FileExt%
SET OldLine=%Line%
GoTo EOF
:: Export to screen
:flush2
:: echo in2
If NOT Exist %OutFileAlt%%FileExt% Echo No MAC Spoofing detected till now&GoTo TakeYourTime
For /F "tokens=1 delims= " %%L In (%OutFileAlt%%FileExt%) Do Echo %%L was found with a duplicate MAC Address&
::del %Infile% /Q
:: rename %OutFile% %Infile%
GoTo Trigger
:: take your time, don't hurry up
:TakeYourTime
ping localhost -n 2 -w 1000 >nul
GoTo Loop
:: Trigger a system command whenever a MAC spoof has been detected
:Trigger
Echo Disabling your WiFi interface NOW !
wmic path win32_networkadapter where NetConnectionID="Wireless Network Connection" call disable>nul
Pause
:EOF