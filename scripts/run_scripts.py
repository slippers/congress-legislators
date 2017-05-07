from subprocess import check_call, Popen

scripts = ['house_contacts.py',
'house_websites.py',
'senate_contacts.py',
'committee_membership.py',
'historical_committees.py',
'social_media.py',
'influence_ids.py',
]

for x in scripts:
    donkey = check_call(['python', x])
    print(x, donkey)
