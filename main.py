import requests,json
import facebook
import pytz
from datetime import datetime
#-----------------------------------------------------------------
f = open('/home/mdtuhinhasnat/FB_AUTO_POST/credential.json')
data = json.load(f)
#-----------------------------------------------------------------
def post(contest_data,time):
    name = contest_data['name']
    id = contest_data['id']
    dt = datetime.utcnow().replace(tzinfo=pytz.UTC)
    timezone = pytz.timezone('Asia/Dhaka')
    contest_time = dt.astimezone(timezone)
    encrypted_token = data['access_token']
    group_id = data['group_id']
    user_id = data['user_id']
    message = '🅲🅾🅽🆃🅴🆂🆃 🅰🅻🅴🆁🆃'+'\nName: '+name+'\nTime: '+str(contest_time.strftime("%I:%M %P"))
    Link = 'https://codeforces.com/contests/'+str(id)
    graph = facebook.GraphAPI(encrypted_token)
    graph.put_object(group_id, 'feed', message=message, link=Link, from_user=user_id)
    print('Post published successfully!')

def codeforces():
    respons_api = requests.get('https://codeforces.com/api/contest.list?"phase"="BEFORE" ')
    data = json.loads(respons_api.text)
    p = data['result']
    # print(p)
    for i in p:
        if i['phase']=='BEFORE' :
            timestamp = i['startTimeSeconds']
            time = datetime.fromtimestamp(timestamp)
            today = datetime.today()
            # post(i,time)
            if time.day == today.day and time.month == today.month and time.year == today.year :
                post(i,time)
codeforces()
