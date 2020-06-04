import json

f = open('../../gen/data-preparation/temp/KLM_Air_France_tweets_file_1.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/KLM-direct_tweets.csv', 'w', encoding = 'utf-8')

outfile.write('id\ttext\n')

cnt = 0
for c in con:
    cnt+=1
    if ('{' not in c): continue
    if ('RT' in c) : continue
    if ('#CreditCard' in c) : continue
    if ('Casino' in c) : continue
    if ('#casino' in c) : continue
    if ('#airdrop' in c) : continue
    if ('#freespin' in c) : continue
    if ('#bounty' in c) : continue

    myobject = json.loads(c)

    id = myobject.get('id_str')
    text = myobject.get('text')
    text = text.replace('\n','').replace('\t', ' ')

    outfile.write(id+'\t'+text+'\n')
    #if (cnt>100): break

outfile.close()
print('done parsing direct tweets')

e = open('../../gen/data-preparation/temp/KLM_Air_France_tweets_file_1.json','r', encoding='utf-8')

don = e.readlines()

dutfile = open('../../gen/data-preparation/temp/KLM-re_tweets.csv', 'w', encoding = 'utf-8')

dutfile.write('id\ttext\n')

cnt = 0
for d in don:
    cnt+=1
    if ('{' not in d): continue
    if ('RT' not in d) : continue
    if ('#CreditCard' in d) : continue
    if ('Casino' in d) : continue
    if ('#casino' in d) : continue
    if ('#airdrop' in d) : continue
    if ('#freespin' in d) : continue
    if ('#bounty' in d) : continue

    myobject = json.loads(d)

    id = myobject.get('id_str')
    text = myobject.get('text')
    text = text.replace('\n','').replace('\t', ' ')

    dutfile.write(id+'\t'+text+'\n')
    #if (cnt>100): break

dutfile.close()
print('done parsing indirect tweets!')
