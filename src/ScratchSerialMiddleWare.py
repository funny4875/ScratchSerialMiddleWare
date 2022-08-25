from scratchclient import ScratchSession
import time
import serial
import sys

username = "ccsh_ky" 
password = "123456987" 
projectID = 724014896
COMport = "COM6"
inputVARs='A0_R,D4_R'
import sys

if len(sys.argv)>5:
    username = sys.argv[1]
    password = sys.argv[2]
    projectID= sys.argv[3]
    COMport  = sys.argv[4]
    inputVARs = sys.argv[5]
else:
    print('依序附帶下列5個參數，以空白字元當間隔\n[1]username [2]password [3]projectID [4]COMport [5]inputVARs\nanykey...')
    input()
    sys.exit()

try:
    serialPort = serial.Serial(port = COMport, baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except: print('please check the Arduino connection');sys.exit()

session = ScratchSession(username, password)
connection = session.create_cloud_connection(projectID)

OUTPUT_VAR = {'☁ D5_W','☁ D6_W','☁ D7_W','☁ D8_W','☁ D9_W'}
INPUT_VAR =set(inputVARs.split(','))
apdu_ex = ""
@connection.on("set")
def on_set(variable):
    global serialPort,apdu_ex
    if variable.name in OUTPUT_VAR:
        try:
            print(variable.name, variable.value)
            if serialPort.writable():
                portNum = int(variable.name[3])
                apdu_ex = b'\x49\x02'+bytes([portNum,int(variable.value)])                          
        except:
            apdu_ex=b'\x49\x02'+bytes([portNum,0])
            print('error while preparing apdu_ex')

#connection.set_cloud_variable("A0_R", 0)
#apdu_ex = b'\x49\x02'+bytes([2,0])

print('start...')
apdu = b'\x49\x00'
lastSerialString =bytes(5)
while True:
    if apdu_ex !='':
        serialPort.write(apdu_ex)
        apdu_ex=''
    else: serialPort.write(apdu)
    
    if(serialPort.in_waiting > 0):
        serialString = serialPort.read(size=5)
       
        if serialString[0]!= lastSerialString[0] and 'A0_R' in INPUT_VAR:
                connection.set_cloud_variable('A0_R', serialString[0])
        if serialString[1]!= lastSerialString[1] and 'A1_R' in INPUT_VAR:
                connection.set_cloud_variable('A1_R', serialString[1])
        if serialString[2]!= lastSerialString[2] and 'A2_R' in INPUT_VAR:
                connection.set_cloud_variable('A2_R', serialString[2])
        if serialString[3]!= lastSerialString[3] and 'A3_R' in INPUT_VAR:
                connection.set_cloud_variable('A3_R', serialString[3])
        if serialString[4]!= lastSerialString[4] and 'D4_R' in INPUT_VAR:
                connection.set_cloud_variable('D4_R', serialString[4])
        lastSerialString = serialString
        
    serialPort.flush()
    time.sleep(0.1)
print('end')
