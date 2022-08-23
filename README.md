# ScratchSerialMiddleWare
A Middleware support Scratch3 communicate with Arduino by serial port

### 在python中 使用 scratchclient 和 scratch3官網做各種互動
本專案利用 「讀寫雲端變數」 之功能，將 Serial port 接收到的訊號傳遞給 scratch3之專案,  
藉此可和 Arduino、nodeMCU 等開發板做互動。  
目前提供 Arduino 之韌體互動規格如下：  
- Arduino端：  
  - 保留下列通訊埠  
    - A4: SDA  
    - A5: SCL  
    - D2 D3: interrupt 0,1  
    - D10~D13: SPI  
  - 輸出：  
    - PWM 輸出埠 D5,D6,D9  (0-255)
    - 數位 輸出埠 D7,D8   (0 or 1)
  - 輸入：  
    - 類比埠 A0,A1,A2,A3 (0~255)  
    - 數位埠 D4 (0 or 1)  
- scratch端雲端變數：  
  - 讀取 Arduino port 內容：
    - A0_R:讀取 A0 類比埠之電壓對應值 0-255
    - A1_R:讀取 A1 類比埠之電壓對應值 0-255
    - A2_R:讀取 A2 類比埠之電壓對應值 0-255
    - A3_R:讀取 A3 類比埠之電壓對應值 0-255
    - D4_R:讀取 D4 數位埠之電壓對應值 0 or 1
  - 寫入 Arduino port :
    - D5_W:
    - D6_W:
    - D9_W:
    - D7_W:
    - D8_W:
  範本：https://scratch.mit.edu/projects/724014896/ 
