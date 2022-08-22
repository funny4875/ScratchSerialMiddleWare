from scratchclient import ScratchSession
import time
import serial
import sys
'''
username = "funny4875" 
password = "5215440" 
projectID = 723657421
COMport = "COM4"
'''
username = "ccsh_ky" 
password = "123456987" 
projectID = 723627909
COMport = "COM4"

try:
    serialPort = serial.Serial(port = COMport, baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except: print('please check the Arduino connection');sys.exit()

session = ScratchSession(username, password)
connection = session.create_cloud_connection(projectID)

OUTPUT_VAR = {'☁ D5_W','☁ D6_W','☁ D7_W','☁ D8_W','☁ D9_W'}
apdu_ex = ""
@connection.on("set")
def on_set(variable):
    global serialPort,apdu_ex
    #print(variable.name, variable.value)
    if variable.name in OUTPUT_VAR:
        try:
            print(variable.name, variable.value)
            if serialPort.writable():
                #print('change apdu')
                portNum = int(variable.name[3])
                apdu_ex = b'\x49\x02'+bytes([portNum,int(variable.value)])
                #print(apdu_ex,portNum)
                #serialPort.write(apdu_ex)                               
        except:
            apdu_ex=b'\x49\x02'+bytes([portNum,0])
            print('error while preparing apdu_ex')

#connection.set_cloud_variable("A0_R", 0)
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
        '''
        print('A0 =',serialString[0],end=',')
        print('A1 =',serialString[1],end=',')
        print('A2 =',serialString[2],end=',')
        print('A3 =',serialString[3],end=',')
        print('D4 =',serialString[4])
        '''
        if serialString[0]!= lastSerialString[0]:
                connection.set_cloud_variable('A0_R', serialString[0])
        if serialString[1]!= lastSerialString[1]:
                connection.set_cloud_variable('A1_R', serialString[1])
        if serialString[2]!= lastSerialString[2]:
                connection.set_cloud_variable('A2_R', serialString[2])
        if serialString[3]!= lastSerialString[3]:
                connection.set_cloud_variable('A3_R', serialString[3])
        if serialString[4]!= lastSerialString[4]:
                connection.set_cloud_variable('D4_R', serialString[4])
        lastSerialString = serialString
        
    serialPort.flush()
    time.sleep(0.1)
print('end')