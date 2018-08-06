EESchema Schematic File Version 4
LIBS:circuit-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_Module:Arduino_Nano_v3.x A?
U 1 1 5B5DC8C0
P 6600 3600
F 0 "A?" H 6600 2514 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 6600 2423 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 6750 2650 50  0001 L CNN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 6600 2600 50  0001 C CNN
	1    6600 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 4300 5700 4300
$Comp
L Device:R R330
U 1 1 5B5DE1BD
P 5900 4450
F 0 "R330" H 5970 4496 50  0000 L CNN
F 1 "R" H 5970 4405 50  0000 L CNN
F 2 "" V 5830 4450 50  0001 C CNN
F 3 "~" H 5900 4450 50  0001 C CNN
	1    5900 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 4300 5900 4300
Connection ~ 5900 4300
Wire Wire Line
	6800 2600 6800 2450
$Comp
L Sensor_Temperature:DS18B20 U?
U 1 1 5B5DE5C2
P 5600 3000
F 0 "U?" V 5326 3000 50  0000 C CNN
F 1 "DS18B20" V 5235 3000 50  0000 C CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4600 2750 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 5450 3250 50  0001 C CNN
	1    5600 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 4600 5900 4600
Connection ~ 5900 4600
Wire Wire Line
	5900 4600 6600 4600
Wire Wire Line
	6800 2450 5600 2450
Wire Wire Line
	5600 2450 5600 2700
Wire Wire Line
	5900 3000 6000 3000
Wire Wire Line
	6000 3000 6000 3200
Wire Wire Line
	6000 3200 6100 3200
$Comp
L Device:Buzzer BZ?
U 1 1 5B5DFBC5
P 5300 3600
F 0 "BZ?" H 5306 3890 50  0000 C CNN
F 1 "Buzzer" H 5306 3799 50  0000 C CNN
F 2 "" V 5275 3700 50  0001 C CNN
F 3 "~" V 5275 3700 50  0001 C CNN
	1    5300 3600
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5400 3700 5600 3700
Wire Wire Line
	5600 3300 5600 3700
Connection ~ 5600 3700
Wire Wire Line
	5600 3700 5600 4600
Text Notes 4700 4800 0    50   ~ 0
Only port 13(D10)\ncan be removed.\n\nAlso, You can remove\nthe R250 resistors.\n\nBut it probably makes\ncircuit to be damaged.
Wire Wire Line
	5400 3500 6100 3500
$Comp
L Device:R R250
U 1 1 5B5DEA74
P 5700 4150
F 0 "R250" H 5770 4196 50  0000 L CNN
F 1 "R" H 5770 4105 50  0000 L CNN
F 2 "" V 5630 4150 50  0001 C CNN
F 3 "~" H 5700 4150 50  0001 C CNN
	1    5700 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 4000 5700 4000
$EndSCHEMATC
