import csv
import plotly
import psycopg2
import sys
import sqlite3
import time

import numpy as np
import pandas as pd


def create_and_populate_tables_psql():

    #Define our connection parameters
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"

    #Connect to database
    conn = psycopg2.connect(conn_string)

    #Initialize cursor
    cur = conn.cursor()

    creates=(
        """CREATE TABLE DATAMAIN (
            Country_name VARCHAR,
            Population INT,
            Density DECIMAL,
            Infant_Mortality DECIMAL,
            GDP DECIMAL,
            Literacy DECIMAL,
            Phones_Perc DECIMAL,
            Arable_Land DECIMAL,
            Crops_of_Arable DECIMAL,
            BirthoverDeath DECIMAL)""",

        """INSERT INTO DATAMAIN (Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath) VALUES
            ('Afghanistan',31056997,48,163.07,700,36,3.2,12.13,0.22,2.291052114),
            ('Albania',3581655,124.6,21.52,4500,86.5,71.2,21.09,4.42,2.894636015),
            ('Algeria',32930091,13.8,31,6000,70,78.1,3.22,0.25,3.718004338),
            ('American Samoa',57794,290.4,9.27,8000,97,259.5,10,15,6.868501529),
            ('Andorra',71201,152.1,4.05,19000,100,497.2,2.22,0,1.3936),
            ('Angola',12127071,9.7,191.19,1900,42,7.8,2.41,0.24,1.864049587),
            ('Anguilla',13477,132.1,21.03,8600,95,460,0,0,2.653558052),
            ('Antigua & Barbuda',69108,156,19.46,11000,89,549.9,18.18,4.55,3.152700186),
            ('Argentina',39921833,14.4,15.18,11200,97.1,220.4,12.31,0.48,2.21589404),
            ('Armenia',2976372,99.9,23.28,3500,98.6,195.7,17.55,2.3,1.466585662),
            ('Aruba',71891,372.5,5.89,28000,97,516.1,10.53,0,1.651197605),
            ('Australia',20264082,2.6,4.69,29000,100,565.5,6.55,0.04,1.616511318),
            ('Austria',8192880,97.7,4.66,30000,98,452.2,16.91,0.86,0.8954918033),
            ('Azerbaijan',7961619,91.9,81.74,3400,97,137.1,19.63,2.71,2.127179487),
            ('Bahamas The',303770,21.8,25.21,16700,95.6,460.6,0.8,0.4,1.941436464),
            ('Bahrain',698585,1050.5,17.27,16900,89.1,281.3,2.82,5.63,4.299516908),
            ('Bangladesh',147365352,1023.4,62.6,1900,43.1,7.3,62.11,3.07,3.603385732),
            ('Barbados',279912,649.5,12.5,15700,97.4,481.9,37.21,2.33,1.465974625),
            ('Belarus',10293011,49.6,13.37,6100,99.6,319.1,29.55,0.6,0.7960057061),
            ('Belgium',10379067,340,4.68,29100,98,462.6,23.28,0.4,1.010710808),
            ('Belize',287730,12.5,25.69,4900,94.1,115.7,2.85,1.71,5.041958042),
            ('Benin',7862944,69.8,85,1100,40.9,9.7,18.08,2.4,3.179214403),
            ('Bermuda',65773,1241,8.53,36000,98,851.4,20,0,1.472868217),
            ('Bhutan',2279723,48.5,100.44,1300,42.2,14.3,3.09,0.43,2.649606299),
            ('Bolivia',8989046,8.2,53.11,2400,87.2,71.9,2.67,0.19,3.094289509),
            ('Bosnia & Herzegovina',4498976,88,21.05,6100,0,215.4,13.6,2.96,1.060459492),
            ('Botswana',1639833,2.7,54.58,9000,79.8,80.5,0.65,0.01,0.7823728814),
            ('Brazil',188078227,22.1,29.61,7600,86.4,225.3,6.96,0.9,2.683954619),
            ('British Virgin Is.',23098,151,18.05,16000,97.8,506.5,20,6.67,3.368778281),
            ('Brunei',379444,65.8,12.61,18600,93.9,237.2,0.57,0.76,5.446376812),
            ('Bulgaria',7385367,66.6,20.55,7600,98.6,336.3,40.02,1.92,0.6762438683),
            ('Burkina Faso',13902972,50.7,97.57,1100,26.6,7,14.43,0.19,2.924358974),
            ('Burma',47382633,69.8,67.24,1800,85.3,10.1,15.19,0.97,1.82197355),
            ('Burundi',8090068,290.7,69.29,600,51.6,3.4,35.05,14.02,3.136701337),
            ('Cambodia',13881427,76.7,71.48,1900,69.4,2.6,20.96,0.61,2.969094923),
            ('Cameroon',17340702,36.5,68.26,1800,79,5.7,12.81,2.58,2.515961396),
            ('Canada',33098932,3.3,4.75,29800,97,552.2,4.96,0.02,1.382051282),
            ('Cape Verde',420979,104.4,47.77,1400,76.6,169.6,9.68,0.5,3.796946565),
            ('Cayman Islands',45436,173.4,8.19,35000,98,836.3,3.85,0,2.605316973),
            ('Central African Rep.',4303356,6.9,91,1100,51,2.3,3.1,0.14,1.818230563),
            ('Chad',9944201,7.7,93.82,1200,47.5,1.3,2.86,0.02,2.791819292),
            ('Chile',16134219,21.3,8.8,9900,96.2,213,2.65,0.42,2.621342513),
            ('China',1313973713,136.9,24.18,5000,90.9,266.7,15.4,1.25,1.901004304),
            ('Colombia',43593035,38.3,20.97,6300,92.5,176.2,2.42,1.67,3.670250896),
            ('Comoros',690948,318.4,74.93,700,56.5,24.5,35.87,23.32,4.503658537),
            ('Congo. Dem. Rep.',62660551,26.7,94.69,700,65.5,0.2,2.96,0.52,3.292388847),
            ('Congo. Repub.of the',3702314,10.8,93.86,700,83.8,3.7,0.51,0.13,3.292343387),
            ('Cook Islands',21388,89.1,0,5000,95,289.9,17.39,13.04,0),
            ('Costa Rica',4075261,79.8,9.95,9100,96,340.7,4.41,5.88,4.201834862),
            ('Cote d Ivoire',17654843,54.8,90.83,1400,50.9,14.6,9.75,13.84,2.365902965),
            ('Croatia',4494749,79.5,6.84,10600,98.5,420.4,26.09,2.27,0.8371080139),
            ('Cuba',11382820,102.7,6.33,2900,97,74.7,33.05,7.6,1.646814404),
            ('Cyprus',784301,84.8,7.18,19200,97.6,0,7.79,4.44,1.635416667),
            ('Czech Republic',10235455,129.8,3.93,15700,99.9,314.3,39.8,3.05,0.8517469311),
            ('Denmark',5450661,126.5,4.56,31100,100,614.6,54.02,0.19,1.074324324),
            ('Djibouti',486530,21.2,104.13,1300,67.9,22.8,0.04,0,2.047125842),
            ('Dominica',68910,91.4,14.15,5400,94,304.8,6.67,20,2.268945022),
            ('Dominican Republic',9183984,188.5,32.38,6000,84.7,97.4,22.65,10.33,4.052356021),
            ('East Timor',1062777,70.8,47.41,500,58.6,0,4.71,0.67,4.325320513),
            ('Ecuador',13547510,47.8,23.66,3300,92.5,125.6,5.85,4.93,5.269503546),
            ('Egypt',78887007,78.8,32.59,4000,57.7,131.8,2.87,0.48,4.38623327),
            ('El Salvador',6822378,324.3,25.1,4800,80.2,142.4,31.85,12.07,4.603806228),
            ('Equatorial Guinea',540109,19.3,85.13,2700,85.7,18.5,4.63,3.57,2.363213811),
            ('Eritrea',4786994,39.5,74.87,700,58.6,7.9,4.95,0.03,3.576041667),
            ('Estonia',1324333,29.3,7.87,12300,99.8,333.8,16.04,0.45,0.7577358491),
            ('Ethiopia',74777981,66.3,95.32,700,42.7,8.2,10.71,0.75,2.555854643),
            ('Faroe Islands',47246,33.8,6.24,22000,0,503.8,2.14,0,1.614942529),
            ('Fiji',905949,49.6,12.62,5800,93.7,112.6,10.95,4.65,3.991150442),
            ('Finland',5231372,15.5,3.57,27400,100,405.3,7.19,0.03,1.059837728),
            ('France',60876136,111.3,4.26,27600,99,586.4,33.53,2.07,1.311816193),
            ('French Guiana',199509,2.2,12.07,8300,83,255.6,0.14,0.05,4.192622951),
            ('French Polynesia',274578,65.9,8.44,17500,98,194.5,0.82,5.46,3.556503198),
            ('Gabon',1424906,5.3,53.64,5500,63.2,27.4,1.26,0.66,2.951836735),
            ('Gambia The',1641564,145.3,72.02,1700,40.1,26.8,25,0.5,3.213877551),
            ('Gaza Strip',1428757,3968.8,22.93,600,0,244.3,28.95,21.05,10.38157895),
            ('Georgia',4661473,66.9,18.59,2500,99,146.6,11.44,3.86,1.127843987),
            ('Germany',82422299,230.9,4.16,27600,99,667.9,33.85,0.59,0.7768361582),
            ('Ghana',22409572,93.6,51.43,2200,74.8,14.4,16.26,9.67,3.139917695),
            ('Gibraltar',27928,3989.7,5.13,17500,0,877.7,0,0,1.153598281),
            ('Greece',10688058,81,5.53,20000,97.5,589.7,21.1,8.78,0.9453125),
            ('Greenland',56361,0,15.82,20000,0,448.9,0,0,2.031887755),
            ('Grenada',89703,260.8,14.62,5000,98,364.5,5.88,29.41,3.209302326),
            ('Guadeloupe',452776,254.4,8.6,8000,90,463.8,11.24,3.55,2.471264368),
            ('Guam',171019,316.1,6.94,21000,99,492,9.09,16.36,4.194196429),
            ('Guatemala',12293545,112.9,35.93,4100,70.6,92.1,12.54,5.03,5.746153846),
            ('Guernsey',65409,838.6,4.71,20000,0,842.4,0,0,0.8801198801),
            ('Guinea',9690222,39.4,90.37,2100,35.9,2.7,3.63,2.58,2.697674419),
            ('Guinea-Bissau',1442029,39.9,107.17,800,42.4,7.4,10.67,8.82,2.251663642),
            ('Guyana',767245,3.6,33.26,4000,98.8,143.5,2.44,0.15,2.207729469),
            ('Haiti',8308504,299.4,73.45,1600,52.9,16.9,28.3,11.61,2.994248151),
            ('Honduras',7326496,65.4,29.32,2600,76.2,67.5,9.55,3.22,5.348484848),
            ('Hong Kong',6940432,6355.7,2.97,28800,93.5,546.7,5.05,1.01,1.158982512),
            ('Hungary',9981334,107.3,8.57,13900,99.4,336.2,50.09,2.06,0.7414187643),
            ('Iceland',299388,2.9,3.31,30900,99.9,647.7,0.07,0,2.029761905),
            ('India',1095351995,333.2,56.29,2900,59.5,45.4,54.4,2.74,2.690709046),
            ('Indonesia',245452739,127.9,35.6,3200,87.9,52,11.32,7.23,3.2544),
            ('Iran',68688433,41.7,41.58,7000,79.4,276.4,8.72,1.39,3.063063063),
            ('Iraq',26783383,61.3,50.25,1500,40.4,38.6,13.15,0.78,5.955307263),
            ('Ireland',4062235,57.8,5.39,29600,98,500.5,15.2,0.03,1.847826087),
            ('Isle of Man',75441,131.9,5.93,21000,0,676,9,0,0.9874888293),
            ('Israel',6352117,305.8,7.03,19800,95.4,462.3,16.39,4.17,2.90776699),
            ('Italy',58133509,193,5.94,26700,98.6,430.9,27.79,9.53,0.8384615385),
            ('Jamaica',2758124,250.9,12.36,3900,87.9,124,16.07,10.16,3.193251534),
            ('Japan',127463611,337.4,3.26,28200,99,461.2,12.19,0.96,1.022925764),
            ('Jersey',91084,785.2,5.24,24800,0,811.3,0,0,1.002155172),
            ('Jordan',5906760,64,17.35,4300,91.3,104.5,2.67,1.83,8.018867925),
            ('Kazakhstan',15233244,5.6,29.21,6300,98.4,164.1,7.98,0.05,1.6985138),
            ('Kenya',34707817,59.6,61.47,1000,85.1,8.1,8.08,0.98,2.833095578),
            ('Kiribati',105432,130,48.52,800,0,42.7,2.74,50.68,3.710653753),
            ('Korea. North',23113019,191.8,24.04,1300,99,42.4,20.76,2.49,2.179523142),
            ('Korea. South',48846823,496,7.05,17800,97.9,486.1,17.18,1.95,1.709401709),
            ('Kuwait',2418393,135.7,9.95,19000,83.5,211,0.73,0.11,9.10373444),
            ('Kyrgyzstan',5213898,26.3,35.64,1600,97,84,7.3,0.35,3.220338983),
            ('Laos',6368481,26.9,85.22,1700,66.4,14.1,3.8,0.35,3.072727273),
            ('Latvia',2274735,35.2,9.55,10200,99.8,321.4,29.67,0.47,0.6764275256),
            ('Lebanon',3874050,372.5,24.52,4800,87.4,255.6,16.62,13.98,2.982286634),
            ('Lesotho',2022331,66.6,84.23,3000,84.8,23.7,10.87,0.13,0.8620689655),
            ('Liberia',3042004,27.3,128.87,1000,57.5,2.3,3.95,2.28,1.938095238),
            ('Libya',5900754,3.4,24.6,6400,82.6,127.1,1.03,0.19,7.612068966),
            ('Liechtenstein',33987,212.4,4.7,25000,100,585.5,25,0,1.422005571),
            ('Lithuania',3585906,55,6.89,11400,99.6,223.4,45.22,0.91,0.7969034608),
            ('Luxembourg',474413,183.5,4.81,55100,100,515.4,23.28,0.4,1.419738407),
            ('Macau',453125,16183,4.39,19400,94.5,384.9,0,0,1.897091723),
            ('Macedonia',2050554,80.9,10.09,6700,0,260,22.26,1.81,1.370581528),
            ('Madagascar',18595469,31.7,76.83,800,68.9,3.6,5.07,1.03,3.727272727),
            ('Malawi',13013926,109.8,103.32,600,62.7,7.9,23.38,1.49,2.231246767),
            ('Malaysia',24385858,74,17.7,9000,88.7,179,5.48,17.61,4.526732673),
            ('Maldives',359008,1196.7,56.52,3900,97.2,90,13.33,16.67,4.930594901),
            ('Mali',11716829,9.5,116.79,900,46.4,6.4,3.82,0.03,2.949674364),
            ('Malta',400214,1266.5,3.89,17700,92.8,505,28.13,3.13,1.261728395),
            ('Marshall Islands',60422,5.1,29.45,1600,93.7,91.2,16.67,38.89,6.914225941),
            ('Martinique',436131,396.5,7.09,14400,97.7,394.4,10.38,9.43,2.12037037),
            ('Mauritania',3177388,3.1,70.89,1800,41.7,12.9,0.48,0.01,3.370888158),
            ('Mauritius',1240827,608.3,15.03,11400,85.6,289.3,49.26,2.96,2.249271137),
            ('Mayotte',201234,538.1,62.4,2600,0,49.7,0,0,5.318181818),
            ('Mexico',107449525,54.5,20.91,9000,92.2,181.6,12.99,1.31,4.364978903),
            ('Micronesia Fed St.',108004,153.9,30.21,2000,89,114.8,5.71,45.71,5.195789474),
            ('Moldova',4466706,132,40.42,1800,99.1,208.1,55.3,10.79,1.242088608),
            ('Monaco',32543,16271.5,5.43,27000,99,1035.6,0,0,0.7118512781),
            ('Mongolia',2832224,1.8,53.79,1800,97.8,55.1,0.77,0,3.10647482),
            ('Montserrat',9439,92.5,7.35,3400,97,0,20,0,2.477464789),
            ('Morocco',33241259,74.4,41.62,4000,51.7,40.4,19.61,2.17,3.9390681),
            ('Mozambique',19686505,24.6,130.79,1200,47.8,3.5,5.1,0.3,1.647775176),
            ('Namibia',2044147,2.5,48.98,7200,84,62.6,0.99,0,1.289501591),
            ('Nauru',13287,632.7,9.95,5000,0,143,0,0,3.695522388),
            ('Nepal',28287147,192.2,66.98,1400,45.2,15.9,21.68,0.64,3.327604726),
            ('Netherlands',16491461,397.1,5.04,28600,99,460.8,26.71,0.97,1.255760369),
            ('Netherlands Antilles',221736,231,10.03,11400,96.7,365.3,10,0,2.291472868),
            ('New Caledonia',219246,11.5,7.72,15000,91,252.2,0.38,0.33,3.182776801),
            ('New Zealand',4076140,15.2,5.85,21600,99,441.7,5.6,6.99,1.827357238),
            ('Nicaragua',5570129,43,29.11,2300,67.5,39.7,15.94,1.94,5.507865169),
            ('Niger',12525094,9.9,121.69,800,17.6,1.9,3.54,0.01,2.426111908),
            ('Nigeria',131859731,142.7,98.8,900,68,9.3,31.29,2.96,2.386658796),
            ('N.Mariana Islands',82459,172.9,7.11,12500,97,254.7,13.04,4.35,8.484716157),
            ('Norway',4610820,14.2,3.7,37800,100,461.7,2.87,0,1.219148936),
            ('Oman',3102229,14.6,19.51,13100,75.8,85.5,0,0.14,9.511811024),
            ('Pakistan',165803560,206.2,72.44,2100,45.7,31.8,27.87,0.87,3.613608748),
            ('Palau',20579,44.9,14.84,9000,92,325.6,8.7,4.35,2.651470588),
            ('Panama',3191319,40.8,20.47,6300,92.6,137.9,7.36,1.98,4.055970149),
            ('Papua New Guinea',5670544,12.3,51.45,2200,64.6,10.9,0.46,1.44,4.049655172),
            ('Paraguay',6506464,16,25.63,4700,94,49.2,7.6,0.23,6.481069042),
            ('Peru',28302603,22,31.94,5100,90.9,79.5,2.89,0.4,3.287319422),
            ('Philippines',89468677,298.2,23.51,4600,92.6,38.4,18.95,16.77,4.600739372),
            ('Poland',38536869,123.3,8.51,11100,99.8,306.3,45.91,1.12,0.9959555106),
            ('Portugal',10605870,114.8,5.05,18000,93.3,399.2,21.75,7.81,1.020952381),
            ('Puerto Rico',3927188,284.8,8.24,16800,94.1,283.1,3.95,5.52,1.669281046),
            ('Qatar',885359,77.4,18.61,21500,82.5,232,1.64,0.27,3.296610169),
            ('Reunion',787584,312.9,7.78,5800,88.9,380.9,13.6,1.2,3.442622951),
            ('Romania',22303552,93.9,26.43,7000,98.4,196.9,40.82,2.25,0.9090909091),
            ('Russia',142893540,8.4,15.39,8900,99.6,280.6,7.33,0.11,0.6791808874),
            ('Rwanda',8648248,328.4,91.23,1300,70.4,2.7,40.54,12.16,2.509011809),
            ('Saint Helena',7502,18.2,19,2500,97,293.3,12.9,0,1.857580398),
            ('Saint Kitts & Nevis',39129,149.9,14.49,8800,97,638.9,19.44,2.78,2.163265306),
            ('Saint Lucia',168458,273.5,13.53,5400,67,303.3,6.56,22.95,3.874015748),
            ('St Pierre & Miquelon',7026,29,7.54,6900,99,683.2,13.04,0,1.979502196),
            ('Saint  Vincent and the Grenadines',117848,303,14.78,2900,96,190.9,17.95,17.95,2.705685619),
            ('Samoa',176908,60.1,27.71,5600,99.7,75.2,21.2,24.38,2.481873112),
            ('San Marino',29251,479.5,5.73,34600,96,704.3,16.67,0,1.226438188),
            ('Sao Tome & Principe',193413,193.2,43.11,1200,79.3,36.2,6.25,48.96,6.221020093),
            ('Saudi Arabia',27019731,13.8,13.24,11800,78.8,140.6,1.67,0.09,11.37209302),
            ('Senegal',11987121,61.1,55.51,1600,40.2,22.2,12.78,0.21,3.479830149),
            ('Serbia',9396411,106.3,12.89,2200,93,285.8,33.35,3.2,0),
            ('Seychelles',81541,179.2,15.53,7800,58,262.4,2.22,13.33,2.548489666),
            ('Sierra Leone',6005250,83.7,143.64,500,31.4,4,6.98,0.89,1.986973513),
            ('Singapore',4492150,6482.2,2.29,23700,92.5,411.4,1.64,0,2.182242991),
            ('Slovakia',5439448,111.4,7.41,13300,0,220.1,30.16,2.62,1.126984127),
            ('Slovenia',2010347,99.2,4.45,19000,99.7,406.1,8.6,1.49,0.8709990301),
            ('Solomon Islands',552438,19.4,21.29,1700,0,13.4,0.64,2,7.655612245),
            ('Somalia',8863338,13.9,116.7,500,37.8,11.3,1.67,0.04,2.713770295),
            ('South Africa',44187637,36.2,61.81,10700,86.4,107,12.08,0.79,0.8272727273),
            ('Spain',40397842,80,4.42,22000,97.9,453.5,26.07,9.87,1.034979424),
            ('Sri Lanka',20222240,308.2,14.35,3700,92.3,61.5,13.86,15.7,2.378834356),
            ('Sudan',41236378,16.5,62.5,1900,61.1,16.3,6.83,0.18,3.849498328),
            ('Suriname',439117,2.7,23.57,4000,93,184.7,0.37,0.06,2.478679505),
            ('Swaziland',1136334,65.5,69.27,4900,81.6,30.8,10.35,0.7,0.9216543376),
            ('Sweden',9016596,20,2.77,26800,99,715,6.54,0.01,0.9961202716),
            ('Switzerland',7523934,182.2,4.39,32700,99,680.9,10.42,0.61,1.143698469),
            ('Syria',18881361,102,29.53,3300,76.9,153.8,25.22,4.43,5.771309771),
            ('Taiwan',23036087,640.3,6.4,23400,96.1,591,24,1,1.938271605),
            ('Tajikistan',7320815,51.2,110.76,1000,99.4,33.5,6.61,0.92,3.957575758),
            ('Tanzania',37445392,39.6,98.54,600,78.2,4,4.52,1.08,2.300793167),
            ('Thailand',64631595,125.7,20.48,7400,92.6,108.9,29.36,6.46,1.970170455),
            ('Togo',5548702,97.7,66.61,1500,60.9,10.6,46.15,2.21,3.765005086),
            ('Tonga',114689,153.3,12.62,2200,98.5,97.7,23.61,43.06,4.804924242),
            ('Trinidad & Tobago',1065842,207.9,24.31,9500,98.6,303.5,14.62,9.16,1.220435194),
            ('Tunisia',10175014,62.2,24.77,6900,74.2,123.6,17.86,13.74,3.025341131),
            ('Turkey',70413958,90.2,41.04,6700,86.5,269.5,30.93,3.31,2.783919598),
            ('Turkmenistan',5042920,10.3,73.08,5800,98,74.6,3.72,0.14,3.210465116),
            ('Turks & Caicos Is.',21152,49.2,15.67,9600,98,269.5,2.33,0,5.187648456),
            ('Tuvalu',11810,454.2,20.03,1100,0,59.3,0,0,3.11954993),
            ('Uganda',28195754,119.5,67.83,1400,69.9,3.6,25.88,10.65,3.868464052),
            ('Ukraine',46710816,77.4,20.34,5400,99.7,259.9,56.21,1.61,0.6129256428),
            ('United Arab Emirates',2602713,31.4,14.51,23200,77.9,475.3,0.6,2.25,4.309090909),
            ('United Kingdom',60609153,247.6,5.16,27700,99,543.5,23.46,0.21,1.057255676),
            ('United States',298444215,31,6.5,37800,97,898,19.13,0.22,1.711864407),
            ('Uruguay',3431932,19.5,11.95,12800,98,291.4,7.43,0.23,1.537016575),
            ('Uzbekistan',27307134,61,71.1,1700,99.3,62.9,10.83,0.83,3.362244898),
            ('Vanuatu',208869,17.1,55.16,2900,53,32.6,2.46,7.38,2.905370844),
            ('Venezuela',25730435,28.2,22.2,4800,93.4,140.1,2.95,0.92,3.802845528),
            ('Vietnam',84402966,256.1,25.95,2500,90.3,187.7,19.97,5.95,2.710610932),
            ('Virgin Islands',108605,56.9,8.03,17200,0,652.8,11.76,2.94,2.171073095),
            ('Wallis and Futuna',16025,58.5,0,3700,50,118.6,5,25,0),
            ('West Bank',2460492,419.9,19.62,800,0,145.2,16.9,18.97,8.079081633),
            ('Western Sahara',273008,1,0,0,0,0,0.02,0,0),
            ('Yemen',21456188,40.6,61.5,800,50.2,37.2,2.78,0.24,5.16746988),
            ('Zambia',11502010,15.3,88.29,800,80.6,8.2,7.08,0.03,2.057200201),
            ('Zimbabwe',12236805,31.3,67.69,1900,90.7,26.8,8.32,0.34,1.282509158);""")
    for create in creates:
        cur.execute(create)


    #Destroy connection to ensure execution and not compromise consistency
    cur.close()
    conn.commit()
    conn.close()

            ### DATA NOW INSERTED INTO DATABASE ON POSTGRESS SERVER AND HARDCODED INTO SERVER TO ENSURE CONSISTENCY
            ## DATA WAS HARDCODED BECAUSE IT IS 2015 CENSUS DATA THAT WILL NOT NEED TO BE CHANGED
def delete_tables():
    #Define our connection parameters
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"

    #Connect to database
    conn = psycopg2.connect(conn_string)

    #Initialize cursor
    commands = ("DROP TABLE DATAMAIN CASCADE")
        #cascade necessary to completely remove all entries

    for command in commands :
        cur.execute(command)

        #Destroy connection
    cur.close()
    conn.commit()
    conn.close()

def math():
        ###

        conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
        #Connect to database
        con = psycopg2.connect(conn_string)
        cur = con.cursor()


        mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


        cur.execute(mathcommand1)

        newmath1 = pd.read_sql(mathcommand1, con=con)
        mathcommand2=("""SELECT * FROM DATAMAIN""")
        for j in mathcommand2:
            cur.execute(mathcommand2)
        newmath2 = pd.read_sql(mathcommand2, con=con)
        print(newmath2)
        cur.close()
        con.commit()
        con.close()



def math2():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand3=("""SELECT Country_name, Population FROM DATAMAIN ORDER BY Population""")
    for j in mathcommand3:
        cur.execute(mathcommand3)
    newmath3 = pd.read_sql(mathcommand3, con=con)
    print(newmath3)
    cur.close()
    con.commit()
    con.close()

def math3():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, Density FROM DATAMAIN ORDER BY Density DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def math4():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, Infant_Mortality FROM DATAMAIN ORDER BY Infant_Mortality DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def math5():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, GDP FROM DATAMAIN ORDER BY GDP DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def math6():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, Literacy FROM DATAMAIN ORDER BY Literacy DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def math7():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, Phones_Perc FROM DATAMAIN ORDER BY Phones_Perc DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def math8():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, Arable_Land FROM DATAMAIN ORDER BY Arable_Land DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def math9():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, Crops_of_Arable FROM DATAMAIN ORDER BY Crops_of_Arable DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def math10():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, BirthoverDeath FROM DATAMAIN ORDER BY BirthoverDeath DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def population():
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    TotalPopulation=("""SELECT SUM(Population) AS "WORLD POPULATION TOTAL" FROM DATAMAIN """)
    for j in TotalPopulation:
        cur.execute(TotalPopulation)
    newmath4 = pd.read_sql(TotalPopulation, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath():
        ###

        conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
        #Connect to database
        con = psycopg2.connect(conn_string)
        cur = con.cursor()


        mathcommand1="SELECT POWER(Population, 30) FROM DATAMAIN"


        cur.execute(mathcommand1)

        newmath1 = pd.read_sql(mathcommand1, con=con)
        mathcommand2=("""SELECT * FROM DATAMAIN""")
        for j in mathcommand2:
            cur.execute(mathcommand2)
        newmath2 = pd.read_sql(mathcommand2, con=con)
        print(newmath2)
        cur.close()
        con.commit()
        con.close()



def pmath2():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand3=("""SELECT Country_name, POWER(Population,30) FROM DATAMAIN ORDER BY Population""")
    for j in mathcommand3:
        cur.execute(mathcommand3)
    newmath3 = pd.read_sql(mathcommand3, con=con)
    print(newmath3)
    cur.close()
    con.commit()
    con.close()

def pmath3():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(Density, 30) FROM DATAMAIN ORDER BY Density DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath4():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(Infant_Mortality,30) FROM DATAMAIN ORDER BY Infant_Mortality DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath5():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(GDP,30) FROM DATAMAIN ORDER BY GDP DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath6():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(Literacy,30) FROM DATAMAIN ORDER BY Literacy DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath7():

###Country_name, Population, Density, Infant_Mortality, GDP, Literacy, Phones_Perc, Arable_Land, Crops_of_Arable, BirthoverDeath

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(Phones_Perc,30) FROM DATAMAIN ORDER BY Phones_Perc DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath8():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(Arable_Land,30) FROM DATAMAIN ORDER BY Arable_Land DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath9():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(Crops_of_Arable,30) FROM DATAMAIN ORDER BY Crops_of_Arable DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def pmath10():

###

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    mathcommand4=("""SELECT Country_name, POWER(BirthoverDeath,30) FROM DATAMAIN ORDER BY BirthoverDeath DESC""")
    for j in mathcommand4:
        cur.execute(mathcommand4)
    newmath4 = pd.read_sql(mathcommand4, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

def ppopulation():
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
#Connect to database
    con = psycopg2.connect(conn_string)
    cur = con.cursor()


    #mathcommand1="SELECT AVG(Population) FROM DATAMAIN"


    #cur.execute(mathcommand1)

    #newmath1 = pd.read_sql(mathcommand1, con=con)
    TotalPopulation=("""SELECT POWER(Population,30) AS "WORLD POPULATION TOTAL" FROM DATAMAIN """)
    for j in TotalPopulation:
        cur.execute(TotalPopulation)
    newmath4 = pd.read_sql(TotalPopulation, con=con)
    print(newmath4)
    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    psql_start = time.time()
    create_and_populate_tables_psql()
    #create_and_populate_tables_sql()
    math()
    math2()
    math3()
    math4()
    math5()
    math6()
    math7()
    math8()
    math9()
    math10()
    population()



    psql_end = time.time()
    print("Time for PotgreSQL compilation and query evaluation::: ", psql_end-psql_start)

    #NOW TO DEMONSTRATE POWERMATH AND SPEED OF PSQL TRANSACTIONS
    ppsql_start = time.time()
    pmath()
    pmath2()
    pmath3()
    pmath4()
    pmath5()
    pmath6()
    pmath7()
    pmath8()
    pmath9()
    pmath10()
    ppopulation()
    ppsql_end = time.time()
    print("Time for PotgreSQL compilation and query evaluation::: ", ppsql_end-ppsql_start)
