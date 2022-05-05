#Main FEI Operating System.
#Copyright @FEI Group 2020-2022.
#########This is an open-source project.#########

import os,re,time
print('Setup system,please wait')
time.sleep(2)
a = re.compile('out\s*')
b = re.compile('run\s*')
c = re.compile('exit\s*')
d = re.compile('taskkill\s*')
d1 = re.compile('taskkill\s-e\s*')
tasklist = ['System']
daemon = ['System']
def load(pof):
    f = open(pof,'r+')
    try:
        while True:
            line = f.readline()
            if line == '':
                break
            elif line[0] == '#':
                continue
            elif re.match(a,line):
                t = line.strip('out ')
                print(t)
            elif re.match(c,line):
                t = line.strip('exit ')
                if t == '':
                    f.close()
                    return
                else:
                    print(f'Script exited with code {t}')
                    f.close()
                    return
            elif re.match(d,line):
                if re.match(d1,line):
                    print(tasklist)
                else:
                    print(tasklist)
            else:
                print('Invalid function.')
                f.close()
                return
    except Exception:
        print('Internal error.Please report this to Company.')
        return
time.sleep(1)
load(r'.\test.fei')
print('FEI Operating System')
print('If you see "System is fine",go on setup')
os.system('pause')
while True:
    s = input('>>>')
    if s == '':
        continue
    elif re.match(a,s):
        t = s.strip('out ')
        print(t)
    elif re.match(b,s):
        t = s.strip('run ')
        try:
            tasklist.append(t)
            load(f'{t}')
            tasklist.remove(t)
        except Exception:
            print('Invalid script')
            tasklist.remove(t)
    elif re.match(c,s):
        exit()
    elif re.match(d,s):
        if re.match(d1,s):
            a = s.strip('taskkill -e ')
            tasklist.remove(f'{a}')
        else:
            print(tasklist)
    else:
        print('Invalid function')
        continue
    
