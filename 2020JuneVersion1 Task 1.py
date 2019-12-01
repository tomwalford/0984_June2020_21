# 0984/21
# May/June 2020

deviceCode = ['BPCM','BPSH','RPSS','RPLL','YPLS','YPLL','RTMS','RTLM','YTLM','YTLL']
simCode = ['SMNO','SMPG']
caseCode = ['CSST','CSLX']
chargerCode = ['CGCR','CGHM']

deviceCategory = ['Phone','Phone','Phone','Phone','Phone','Phone', 'Tablet', 'Tablet', 'Tablet', 'Tablet']
deviceDesc = ['Compact',
            'Clam Shell',
            'RoboPhone – 5-inch screen and 64GB memory',
            'RoboPhone – 6-inch screen and 256GB memory',
            'Y-Phone Standard – 6-inch screen and 64GB memory',
            'Y-Phone Deluxe – 6-inch screen and 256GB memory',
            'RoboTab – 8-inch screen and 64GB memory',
            'RoboTab – 10-inch screen and 128GB memory',
            'Y-Tab Standard – 10-inch screen and 128GB memory',
            'Y-Tab Deluxe – 10-inch screen and 256GB memory']
simDesc = ['SIM Free (no SIM card purchased)', 'Pay As You Go (SIM card purchased)']
caseDesc = ['Standard', 'Luxury']
chargerDesc = ['Car', 'Home']

devicePrice = [29.99, 49.99, 199.99, 499.99, 549.99, 659.99, 149.99, 299.99, 499.99, 599.99]
simPrice = [0.00, 9.99]
casePrice = [0.00, 50.00]
chargerPrice = [19.99, 15.99]

YesNo = ['Y','N']

# Task One

ordertotal = 0
    
total = 0

valid = False
while valid is False:
    
    temp = input('Enter item code to be purchased: ').upper()   

    if temp in deviceCode:
        valid = True
    else:
        print('Invalid phone or device type entered')

device = deviceCode.index(temp)

if deviceCategory[device] == 'Phone':
    valid = False
    while valid is False:

        print()
        print('0: SIM Free')
        print('1: Pay as You Go')
        
        temp = input('Enter choice (0 or 1): ')

        if temp in ['0', '1']:
            valid = True
        else:
            print('Invalid choice')

    sim = int(temp)

valid = False
while valid is False:

    print()
    print('0: Standard Case')
    print('1: Luxury Case')
    
    temp = input('Enter choice (0 or 1): ')

    if temp in ['0', '1']:
        valid = True
    else:
        print('Invalid choice')

case = int(temp)
        
valid = False
while valid is False:

    print()
    print('0: No Chargers')
    print('1: Car Charger')
    print('2: Home Charger')
    print('3: Both home and car chargers')
    
    temp = input('Enter choice (0, 1, 2 or 3): ')

    if temp in ['0', '1', '2', '3']:
        valid = True
    else:
        print('Invalid choice')

charger = int(temp)
        
print()
print('{:<8}: {:4} {:<50} ${:7.2f}'.format('Device',deviceCode[device],deviceDesc[device],devicePrice[device]))

total = total + devicePrice[device]

if deviceCategory[device] == 'Phone':
    
    print('{:<8}: {:4} {:<50} ${:7.2f}'.format('SIM Card',simCode[sim],simDesc[sim],simPrice[sim]))

    total = total + simPrice[sim]

print('{:<8}: {:4} {:<50} ${:7.2f}'.format('Case',caseCode[case],caseDesc[case],casePrice[case]))

total = total + casePrice[case]

if charger in [0,1,2]:
    
    if charger == 0:

        code = ''
        desc = 'None'
        price = 0
        
    elif charger == 1:

        code = chargerCode[0]
        desc = chargerDesc[0]
        price = chargerPrice[0]

    else:

        code = chargerCode[1]
        desc = chargerDesc[1]
        price = chargerPrice[1]

    print('{:<8}: {:4} {:<50} ${:7.2f}'.format('Charger',code,desc,price))
    total = total + price
    
else:

    for i in range(2):

        print('{:<8}: {:4} {:<50} ${:7.2f}'.format('Charger',chargerCode[i],chargerDesc[i],chargerPrice[i]))
        total = total + chargerPrice[i]

print()
print('{:<65} ${:7.2f}'.format('Item Total:', total))
print()

ordertotal = ordertotal + total

print('{:<65} ${:7.2f}'.format('Overall Order Total:', ordertotal))

