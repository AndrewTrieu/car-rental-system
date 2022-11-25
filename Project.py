# Install necessary libraries if they are not already installed
# Asenna tarvittavat kirjastot, jos niitä ei ole jo asennettu
try:
    import matplotlib.pyplot as plt
except ImportError:
    import os
    os.system('pip install matplotlib')
    import matplotlib.pyplot as plt
try:
    from prettytable import PrettyTable
except ImportError:
    import os
    os.system('pip install prettytable')
    from prettytable import PrettyTable
from datetime import datetime
import random
import string
now = datetime.now()


# Go back to main menu
# Palaa päävalikkoon


def back():
    input('\nPress ENTER to return to main menu...')
    menu()

# Modify vehicle.txt file
# Muokkaa vehicle.txt-tiedostoa


def modify(tf, mod):
    if tf:
        with open(r'Vehicle.txt', 'w+') as rew:
            for w in mod:
                rew.write(w)

# Display cars available for rent
# Näytä autot vuokrattavissa


def displayCars(u):
    table = PrettyTable(['Registration number', 'Model name',
                        'Type (Ordinary/Premium)', 'Free mileage (km)', 'Daily rent (€)'])
    with open(r'Vehicle.txt', 'r') as f1:
        cars1 = f1.readlines()
        for i in cars1:
            i = i.split(',')
            i = [x.replace('\n', "") for x in i]
            if u == 'A':
                if i[5] == 'A':
                    table.add_row([i[0], i[1], i[2], i[3], i[4]])
            elif u == 'R':
                if i[5] == 'R':
                    table.add_row([i[0], i[1], i[2], i[3], i[4]])
            else:
                print('\nInvalid choice.')
                return
    print(table)

# Add and delete vehicles
# Lisää ja poista ajoneuvoja


def Add_Vehicle():
    lcpl = input('\nEnter Vehicle ID: ')
    ehto = True
    with open(r'Vehicle.txt', 'r') as fv:
        vec = fv.readlines()
        for vc in vec:
            vc = vc.split(',')
            if lcpl == vc[0]:
                print('\nVehicle already exists in database.')
                ehto = False
    if ehto:
        name = input('Enter Vehicle Name: ')
        while True:
            typ = input('Enter vehicle type (O/P): ')
            if typ == 'P':
                try:
                    mileage = float(
                        input("Enter Type-P Vehicle's mileage allowance: "))
                except Exception:
                    print('\nInvalid choice.\n')
                    continue
                else:
                    mileage = str(mileage)
                    break
            elif typ == 'O':
                mileage = '0'
                break
            else:
                print('\nInvalid choice.\n')
                continue
        while True:
            try:
                dailyrent = float(input("Enter daily rent rate: "))
            except Exception:
                print('\nInvalid choice.\n')
                continue
            else:
                dailyrent = str(dailyrent)
                break
        stat = input(
            "Enter status (A/R, if choose R please add rent details to rentVehicle.txt): ")
        with open(r'Vehicle.txt', 'a') as fa:
            fa.write('\n'+lcpl + ','+name+','+typ + ',' +
                     mileage + ','+dailyrent+','+stat)
    while True:
        try:
            con = input('\nDo you want to add another vehicle? (Y/N): ')
        except Exception:
            print("\nInvalid choice.")
            continue
        else:
            if con == 'Y':
                Add_Vehicle()
            elif con == 'N':
                menu()
                return
            else:
                print("\nInvalid choice.")
                continue


def Delete_Vehicle():
    lcpl2 = input('\nEnter Vehicle ID: ')
    with open(r'Vehicle.txt', 'r') as fd:
        ved = fd.readlines()
        for vd in ved:
            vd = vd.split(',')
            if lcpl2 == vd[0]:
                vd = ','.join(vd)
                with open(r'deletedVehicles.txt', 'a') as fr:
                    fr.write(vd+'\n')
                pos = ved.index(vd)
                del ved[pos]
                modify(True, ved)
                break
        else:
            print("\nVehicle does not exist.")
    while True:
        try:
            con = input('\nDo you want to delete another vehicle? (Y/N): ')
        except Exception:
            print("\nInvalid choice.")
            continue
        else:
            if con == 'Y':
                Delete_Vehicle()
            elif con == 'N':
                menu()
                return
            else:
                print("\nInvalid choice.")
                continue

# Add rent details to files
# Lisää tiedostoihin vuokratiedot


def rentDetails(path, app):
    plate = app.split(',')
    if path == 1:
        with open(r'rentVehicle.txt', 'a') as q:
            q.write(str(app))
            print('\nCar '+plate[1]+' is rented successfully.')
    elif path == 2:
        with open(r'Transactions.txt', 'a') as p:
            p.write(str(app))
            print('\nCar '+plate[1]+' is returned successfully.')

# Generate Receipt ID and check if it is already taken
# Luo kuittitunnus ja tarkista, onko se jo varattu


def receiptID():
    while True:
        code = ''.join([random.choice(string.ascii_letters + string.digits)
                        for n in range(10)])
        with open('rentVehicle.txt', 'r') as cd:
            cdc = cd.readlines()
            for cdi in cdc:
                cdi = cdi.split(',')
                if cdi[0] == code:
                    continue
            else:
                return code

# Check Odometer reading
# Tarkista matkamittarin lukema


def odometer(way, qq):
    if way == 1:
        while True:
            try:
                vv = float(
                    input('Enter odometer reading at time of renting: '))
            except Exception:
                print('\nOdometer reading must be a float or an integer.\n')
                continue
            else:
                return vv
    elif way == 2:
        while True:
            try:
                ww = float(
                    input('Enter odometer reading at time of returning: '))
            except Exception:
                print('\nOdometer reading must be a float or an integer.\n')
                continue
            else:
                if (ww) < (qq):
                    print(
                        '\nEnd odometer value must be larger than initial odometer value.\n')
                    continue
                else:
                    return ww

# Add accessories
# Lisää lisävarusteita


def accessories():
    while True:
        paina = input('\nDo you want to add them? (Y/N): ')
        if paina == 'Y':
            return 20
        elif paina == 'N':
            return 0
        else:
            print("\nInvalid choice.")
            continue

# Rent a car
# Vuokrata auton


def rentVehicle(id1):
    with open(r'Vehicle.txt', 'r') as f2:
        cars2 = f2.readlines()
        for j in cars2:
            j = [i.rstrip() for i in j.split(',')]
            if id1 == j[0]:
                if j[5] == 'A':
                    rentID = input('Enter Renter ID: ')
                    odo = str(odometer(1, 0))
                    acc = 0
                    recid = receiptID()
                    if j[2] == 'P':
                        print(
                            '\nThe following accessories could be added to your vehicle for only €20:')
                        print('1. HD Dash Cam')
                        print('2. GPS Navigation')
                        print('3. Engine Heater')
                        acc = accessories()
                    print('\nCar '+j[0]+' is rented to '+rentID)
                    table1 = PrettyTable(['Receipt ID', recid])
                    table1.add_row(['Renter ID', rentID])
                    table1.add_row(['Vehicle ID', id1])
                    table1.add_row(['Description', j[1]])
                    table1.add_row(['Status', 'A -> R'])
                    table1.add_row(['Accessories', '€'+str(acc)])
                    table1.add_row(['Daily rate', '€'+j[4]])
                    table1.add_row(['Date/time of rent',
                                   now.strftime("%d/%m/%Y %H:%M")])
                    table1.add_row(['Rent starting odometer', odo])
                    print(table1)
                    appnew = (recid+','+id1+','+rentID+',' +
                              now.strftime("%d/%m/%Y %H:%M") +
                              ','+odo+','+str(acc)+'\n')
                    rentDetails(1, appnew)
                    j[5] = 'A\n'
                    dx = cars2.index(','.join(j))
                    j[5] = 'R\n'
                    j = ','.join(j)
                    cars2[dx] = j
                    return True, cars2
                elif j[5] == 'R\n':
                    print('\nVehicle is on rent.')
                    return False, []
        else:
            print('\nVehicle does not exist.')
            return False, []

# Return a car
# Palauta auton


def rentComplete(id2):
    with open(r'rentVehicle.txt', 'r') as f3:
        cars3 = f3.readlines()
        for r in cars3:
            r = r.split(',')
            if id2 == r[0]:
                with open(r'Vehicle.txt', 'r') as f4:
                    rented = f4.readlines()
                    for v in rented:
                        v = v.split(',')
                        if v[5] == 'R\n':
                            odo2 = str(odometer(2, float(r[4])))
                            startdate = r[3]
                            dayrent = datetime.strptime(
                                startdate, '%d/%m/%Y %H:%M')
                            daydelta = (now - dayrent).days
                            kms = float(odo2)-float(r[4])
                            typefee = 0
                            if v[2] == 'O':
                                typefee = 0.020
                            elif v[2] == 'P':
                                typefee = 0.025
                            charge = str(
                                ((daydelta+1)*float(v[4]))+((daydelta+1)*float(r[5]))+(kms*typefee))
                            print('\nCar '+r[1]+' is returned from '+r[2])
                            table2 = PrettyTable(['Receipt ID', r[0]])
                            table2.add_row(['Renter ID', r[2]])
                            table2.add_row(['Vehicle ID', r[1]])
                            table2.add_row(['Description', v[1]])
                            table2.add_row(['Status', 'R -> A'])
                            table2.add_row(
                                ['Accessories', '€'+r[5].strip('\n')])
                            table2.add_row(['Daily rate', '€'+v[4]])
                            table2.add_row(['Date/time of rent', r[3]])
                            table2.add_row(['Date/time of return',
                                            now.strftime("%d/%m/%Y %H:%M")])
                            table2.add_row(['Number of days', daydelta+1])
                            table2.add_row(['Rent starting odometer', r[4]])
                            table2.add_row(['Rent end odometer', odo2])
                            table2.add_row(['Distance traveled', kms])
                            table2.add_row(['Rental charges', '€'+charge])
                            print(table2)
                            appdone = (id2+','+r[1]+',' + r[2]+',' + now.strftime(
                                "%d/%m/%Y %H:%M") + ','+r[4]+','+odo2+','+charge+'\n')
                            rentDetails(2, appdone)
                            dy = rented.index(','.join(v))
                            v[5] = 'A\n'
                            v = ','.join(v)
                            rented[dy] = v
                            return True, rented
                    else:
                        print(
                            "Receipt ID found but vehicle is not on rent.")
                        return False, []
        else:
            print('\nReceipt ID does not exist.')
            return False, []

# Data visualization
# Tietojen visualisointi


def Graph1():
    ordinary = 0
    premium = 0
    with open(r'Vehicle.txt', 'r') as g:
        gc = g.readlines()
        for gline in gc:
            gline = gline.split(',')
            gline = [gl.replace('\n', '') for gl in gline]
            if gline[2] == 'O':
                ordinary += 1
            elif gline[2] == 'P':
                premium += 1
    labels = ['Ordinary', 'Premium']
    data = [ordinary, premium]
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Types')
    plt.ylabel('Amounts')
    plt.title('Number of Ordinary and Premium Vehicles')
    plt.bar(range(len(data)), data, color='pink')
    plt.show()


def Graph2():
    dct = {}
    sanakirja = {}
    total = 0
    with open(r'Transactions.txt', 'r') as g2:
        gd = g2.readlines()
        for item in gd:
            if len(dct.keys()) == 12:
                break
            item = item.split(',')
            item = [gh.replace('\n', '') for gh in item]
            item[6] = float(item[6])
            total += item[6]
            paivamaara = datetime.strptime(
                item[3], '%d/%m/%Y %H:%M')
            paiva = paivamaara.strftime('%m/%Y')
            try:
                dct[paiva] = item[6]+float(dct[paiva])
            except KeyError:
                dct[paiva] = 0
                dct[paiva] = item[6]+float(dct[paiva])
    d_items = dct.items()
    sortdct = sorted(d_items)
    for sana in sortdct:
        sanakirja[sana[0]] = sana[1]
    kuukausi = sanakirja.keys()
    tulo = sanakirja.values()
    plt.plot(kuukausi, tulo, color='maroon', marker='*')
    plt.title('Income earned for last '+str(len(dct.keys()))+' month(s)')
    plt.xlabel('Month')
    plt.ylabel('Income (€/month)')
    plt.grid(True)
    plt.show()


# Remove extra lines
# Poista ylimääräiset rivit

def extraLinesTerminator():
    with open('Vehicle.txt', 'r') as z:
        content = z.readlines()
        for i in content:
            if i == '\n' or not i:
                content.remove(i)
        modify(True, content)

# Main menu
# Päävalikko


def menu():
    extraLinesTerminator()
    print('\n           Vehicle Menu')
    print('Display Cars                       1')
    print('Add/delete Vehicle                 2')
    print('Rent Vehicle                       3')
    print('Complete Rent                      4')
    print('Reporting Vehicle Information      5')
    print('Exit                               6')
    try:
        choice = int(input('\nChoose your options: '))
    except Exception:
        print("\nInvalid choice.")
        back()
    else:
        if choice == 1:
            slt = input(
                '\nA for available vehicles or R for vehicles on rent: ')
            displayCars(slt)
            back()
        elif choice == 2:
            try:
                slt2 = int(
                    input('\n1 to add vehicles and 2 to delete vehicles: '))
            except Exception:
                print("\nInvalid choice.")
                back()
            else:
                if slt2 == 1:
                    Add_Vehicle()
                elif slt2 == 2:
                    Delete_Vehicle()
                else:
                    print("\nInvalid choice.")
                    back()
        elif choice == 3:
            idc2 = input('\nEnter Vehicle ID: ')
            o2 = rentVehicle(idc2)
            modify(o2[0], o2[1])
            back()
        elif choice == 4:
            idc3 = input('\nEnter Receipt ID: ')
            o3 = rentComplete(idc3)
            modify(o3[0], o3[1])
            back()
        elif choice == 5:
            print(
                '\nDisplay the number of vehicles of each type: Ordinary and Premium        1')
            print(
                'Display the income earned for last months (maximum 12)                   2')
            try:
                opp = int(input('\nCHoose your options: '))
            except Exception:
                print("\nInvalid choice.")
                back()
            else:
                if opp == 1:
                    Graph1()
                    back()
                elif opp == 2:
                    Graph2()
                    back()
                else:
                    print("\nInvalid choice.")
                    back()
        elif choice == 6:
            print('\nThanks for using Car Rental System. Bye!')
            return
        else:
            print('\nInvalid choice.')
            back()


menu()
