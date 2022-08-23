# ScratchSerialMiddleWare
A Middleware support Scratch3 communicate with Arduino by serial port

### 在python中 使用 scratchclient 和 scratch3官網做各種互動
本專案利用 「讀寫雲端變數」 之功能，將 Serial port 接收到的訊號傳遞給 scratch3之專案,  
藉此可和 Arduino、nodeMCU 等開發板做互動。  
目前提供 Arduino 之韌體互動規格如下：  
Arduino端：  
- 保留下列通訊埠  
  -- A4: SDA  
  -- A5: SCL  
  -- D2 D3: interrupt 0,1  
  -- D10~D13: SPI  
- 輸出：  
  -- PWM 輸出埠 D5,D6,D9  
  -- 數位 輸出埠 D7,D8,D9   
- 輸入：  
  -- 類比埠 A0,A1,A2,A3 (0~255)  
  -- 數位埠 D4 (0,1)  
scratch端：  
