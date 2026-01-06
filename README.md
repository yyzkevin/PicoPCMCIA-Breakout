## Connectors

The PicoPCMCIA External I/O uses Hirose ST-series connectors, chosen for their compact size and robust locking mechanism.

🔗 **Hirose ST Series:**  
https://www.hirose.com/en/product/series/ST

### Connector Part Numbers

| Description | Part Number |
|------------|-------------|
| **Card Receptacle** | ST60-18P(30) |
| **Breakout Plug** | ST60X-18S(30) |
| **Cable Plug Assembly** | ST40X-18S-CV(30) |
| **Cable Bushing** | ST40X-BS(4.0) |
| **Cable Clamp (4 mm)** | ST40X-CM |




## Pinout
| Pin | Signal       | Notes                                                   |
| --: | ------------ | ------------------------------------------------------- |
|   1 | **SWCLK**    | RP2354 Serial Wire Debug (SWD)                          |
|   2 | **SWDIO**    | RP2354 Serial Wire Debug (SWD)                          |
|   3 | **GPIO34**   | User I/O: GPIO, UART0 TX, or I²C1 SDA                   |
|   4 | **GPIO35**   | User I/O: GPIO, UART0 RX, or I²C1 SCL                   |
|   5 | **USB D−**   | RP2354 USB Port                                         |
|   6 | **USB D+**   | RP2354 USB Port                                         |
|   7 | **BOOTSEL**  | Boot select (firmware flashing / recovery)              |
|   8 | **5V**       | 5 V from PC bus (350 mA fused)                          |
|   9 | **GND**      | Ground                                                  |
|  10 | **I2C0 SDA** | I²C master (onboard DSP + external peripherals)         |
|  11 | **I2C0 SCL** | I²C master (onboard DSP + external peripherals)         |
|  12 | —            | Not connected                                           |
|  13 | **GPIO26**   | UART1 TX (also internally connected to SAM2695 MIDI RX) |
|  14 | **IN1_L**    | Line-in left (to DSP)                                   |
|  15 | **IN1_R**    | Line-in right (to DSP)                                  |
|  16 | **HPL**      | Headphones out left (from DSP)                          |
|  17 | **HPR**      | Headphones out right (from DSP)                         |
|  18 | **GND**      | Ground                                                  |
