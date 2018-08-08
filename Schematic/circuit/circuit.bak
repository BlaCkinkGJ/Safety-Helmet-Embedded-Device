EESchema Schematic File Version 4
LIBS:circuit-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Smart Helmet Arduino Nano Schematic"
Date "2018-08-08"
Rev "1.0.0"
Comp "Safty First"
Comment1 "Disjoint Available Port is \"D3\""
Comment2 "Raspberry Pi and Arduino Nano are connected by USB port"
Comment3 "Raspberry Pi must connect the PiCamera"
Comment4 ""
$EndDescr
$Comp
L MCU_Module:Arduino_Nano_v3.x A1
U 1 1 5B5DC8C0
P 5000 3800
F 0 "A1" H 5000 2714 50  0001 C CNN
F 1 "Arduino_Nano_v3.x" H 5000 2623 50  0000 C BNN
F 2 "Module:Arduino_Nano" H 5150 2850 50  0001 L CNN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 5000 2800 50  0001 C CNN
	1    5000 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R330
U 1 1 5B5DE1BD
P 4050 3850
F 0 "R330" H 4120 3896 50  0000 L CNN
F 1 "R" H 4120 3805 50  0000 L CNN
F 2 "" V 3980 3850 50  0001 C CNN
F 3 "~" H 4050 3850 50  0001 C CNN
	1    4050 3850
	1    0    0    -1  
$EndComp
$Comp
L Sensor_Temperature:DS18B20 U1
U 1 1 5B5DE5C2
P 3900 3050
F 0 "U1" V 3626 3050 50  0001 C CNN
F 1 "DS18B20" V 3535 3050 50  0000 C TNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 2900 2800 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 3750 3300 50  0001 C CNN
	1    3900 3050
	0    1    1    0   
$EndComp
$Comp
L Device:Buzzer BZ1
U 1 1 5B5DFBC5
P 3850 4250
F 0 "BZ1" H 3856 4540 50  0001 C CNN
F 1 "Buzzer" H 3856 4449 50  0000 C CNN
F 2 "Buzzer_Beeper:Buzzer_12x9.5RM7.6" V 3825 4350 50  0001 C CNN
F 3 "~" V 3825 4350 50  0001 C CNN
	1    3850 4250
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R250
U 1 1 5B5DEA74
P 3900 3550
F 0 "R250" H 3970 3596 50  0000 L CNN
F 1 "R" H 3970 3505 50  0000 L CNN
F 2 "" V 3830 3550 50  0001 C CNN
F 3 "~" H 3900 3550 50  0001 C CNN
	1    3900 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 3700 4050 3700
Wire Wire Line
	4050 4000 4050 4350
Wire Wire Line
	4050 4800 5000 4800
Wire Wire Line
	3950 4350 4050 4350
Connection ~ 4050 4350
Wire Wire Line
	4050 4350 4050 4800
Wire Wire Line
	4250 3400 4250 3500
Wire Wire Line
	4250 3500 4500 3500
Wire Wire Line
	3900 3400 4250 3400
Wire Wire Line
	4050 3700 4250 3700
Wire Wire Line
	4250 3700 4250 3600
Wire Wire Line
	4250 3600 4500 3600
Connection ~ 4050 3700
Wire Wire Line
	3950 4150 4350 4150
Wire Wire Line
	4350 4150 4350 3700
Wire Wire Line
	4350 3700 4500 3700
Wire Wire Line
	4500 3400 4350 3400
Wire Wire Line
	4350 3400 4350 3350
Wire Wire Line
	4350 3350 3900 3350
Wire Wire Line
	5200 2800 5200 2750
Wire Wire Line
	5200 2750 4350 2750
Wire Wire Line
	4350 2750 4350 3050
Wire Wire Line
	4350 3050 4200 3050
Wire Wire Line
	5100 4800 5100 4900
Wire Wire Line
	3600 4900 3600 3050
Wire Wire Line
	3600 4900 5100 4900
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 5B6B3572
P 7100 3850
F 0 "J1" H 7100 5328 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 7100 5237 50  0000 C CNN
F 2 "" H 7100 3850 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 7100 3850 50  0001 C CNN
	1    7100 3850
	1    0    0    -1  
$EndComp
Text Notes 5600 3850 0    50   ~ 0
USB port is \nconnected by\nUSB mini b type
$EndSCHEMATC
