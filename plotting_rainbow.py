#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:43:38 2021

@author: andershartmann
"""
import math
import matplotlib.pyplot as plt

def P(n):
    
    m=89
    t=737
    l=24
    
    return 1 - math.exp(-math.sqrt(2*m*n**2/2**l)*(math.exp(math.sqrt(2*m*t**2/2**l)) - 1)/(math.exp(math.sqrt(2*m*t**2/2**l)) + 1))


DP=[0]*256

for i in range(1,257):
    DP[i-1]=P(i)
    
#dp=[0.0026674270629882812, 0.005431830883026123, 0.008027911186218262, 0.010587751865386963, 0.013361573219299316, 0.016122102737426758, 0.0187341570854187, 0.02144414186477661, 0.024105191230773926, 0.02678394317626953, 0.02936798334121704, 0.03198504447937012, 0.03477674722671509, 0.037480056285858154, 0.04012864828109741, 0.04270690679550171, 0.04511946439743042, 0.04767203330993652, 0.050086259841918945, 0.05267024040222168, 0.05528378486633301, 0.0579107403755188, 0.06042182445526123, 0.06303626298904419, 0.06569045782089233, 0.06825906038284302, 0.07082325220108032, 0.07329541444778442, 0.07562416791915894, 0.07814580202102661, 0.08061480522155762, 0.08305025100708008, 0.08546692132949829, 0.08794939517974854, 0.09031516313552856, 0.09278607368469238, 0.09547579288482666, 0.09794753789901733, 0.10037094354629517, 0.10281407833099365, 0.10536181926727295, 0.10792893171310425, 0.11027860641479492, 0.112612783908844, 0.11501824855804443, 0.11735886335372925, 0.11974400281906128, 0.12220197916030884, 0.12446045875549316, 0.12690585851669312, 0.1293874979019165, 0.13179069757461548, 0.1341424584388733, 0.1364123821258545, 0.1387966275215149, 0.1411399245262146, 0.14340662956237793, 0.14565372467041016, 0.14800184965133667, 0.15019774436950684, 0.1525261402130127, 0.15477973222732544, 0.15714585781097412, 0.15963029861450195, 0.161818265914917, 0.16390633583068848, 0.1661698818206787, 0.16836249828338623, 0.17048102617263794, 0.17288631200790405, 0.1751936674118042, 0.17737352848052979, 0.17963039875030518, 0.18176627159118652, 0.1840071678161621, 0.1862364411354065, 0.18821585178375244, 0.19049710035324097, 0.19282901287078857, 0.19513386487960815, 0.1972704529762268, 0.1995713710784912, 0.20182013511657715, 0.20386570692062378, 0.20604342222213745, 0.20811277627944946, 0.21040046215057373, 0.2125152349472046, 0.21467626094818115, 0.21680307388305664, 0.218805193901062, 0.22088050842285156, 0.22308969497680664, 0.2251605987548828, 0.22739428281784058, 0.2293681502342224, 0.23156535625457764, 0.23355460166931152, 0.2355913519859314, 0.23764967918395996, 0.23955506086349487, 0.241613507270813, 0.24359744787216187, 0.24549740552902222, 0.2476557493209839, 0.24965238571166992, 0.2516742944717407, 0.25371670722961426, 0.2557189464569092, 0.25781959295272827, 0.2597169876098633, 0.26166409254074097, 0.2635313868522644, 0.26558756828308105, 0.2676240801811218, 0.269631564617157, 0.2716076970100403, 0.2733820676803589, 0.2754579186439514, 0.2775347828865051, 0.27948176860809326, 0.28149598836898804, 0.2834932804107666, 0.28543227910995483, 0.28735774755477905, 0.2891836166381836, 0.2910769581794739, 0.29300886392593384, 0.29499804973602295, 0.29690808057785034, 0.29881751537323, 0.3008229732513428, 0.30271267890930176, 0.30462127923965454, 0.3065917491912842, 0.30844807624816895, 0.31026625633239746, 0.3120470643043518, 0.31397682428359985, 0.31574082374572754, 0.31765836477279663, 0.3194652795791626, 0.32135874032974243, 0.3232138752937317, 0.32495856285095215, 0.32672756910324097, 0.3285098075866699, 0.3302004337310791, 0.3319677710533142, 0.3337740898132324, 0.33555346727371216, 0.3373255133628845, 0.3391323685646057, 0.34091413021087646, 0.34271663427352905, 0.34450238943099976, 0.34615689516067505, 0.34790146350860596, 0.34969663619995117, 0.35157257318496704, 0.3532875180244446, 0.35502034425735474, 0.3567669987678528, 0.3586021661758423, 0.3602783679962158, 0.36197203397750854, 0.3636068105697632, 0.36538296937942505, 0.3671334981918335, 0.3689044713973999, 0.37070947885513306, 0.3724901080131531, 0.37417352199554443, 0.3759583830833435, 0.377715528011322, 0.3794226050376892, 0.3810626268386841, 0.382643461227417, 0.3843858242034912, 0.38601452112197876, 0.3876878619194031, 0.3892059922218323, 0.3908301591873169, 0.39257246255874634, 0.3941926956176758, 0.3958924412727356, 0.3974802494049072, 0.3991760015487671, 0.400820791721344, 0.4024258255958557, 0.4039682149887085, 0.40553855895996094, 0.4071958661079407, 0.4089927673339844, 0.41067057847976685, 0.41218990087509155, 0.41376227140426636, 0.4153215289115906, 0.4168481230735779, 0.41834789514541626, 0.41995954513549805, 0.42156195640563965, 0.4231231212615967, 0.4245949387550354, 0.4261348843574524, 0.4276919960975647, 0.4293484687805176, 0.43087542057037354, 0.4323606491088867, 0.43394291400909424, 0.4354548454284668, 0.43697816133499146, 0.438443660736084, 0.440035879611969, 0.441603422164917, 0.44305241107940674, 0.4445918798446655, 0.44609612226486206, 0.44750869274139404, 0.4488961100578308, 0.450367271900177, 0.45195549726486206, 0.4534107446670532, 0.45482176542282104, 0.4563230872154236, 0.4577580690383911, 0.4592651128768921, 0.46079885959625244, 0.4622962474822998, 0.4638226628303528, 0.4652913212776184, 0.4667589068412781, 0.46825599670410156, 0.46959996223449707, 0.47111737728118896, 0.47258490324020386, 0.47397667169570923, 0.475402295589447, 0.4767950177192688, 0.47814786434173584, 0.4796452522277832, 0.48105931282043457, 0.4824925661087036, 0.4838160276412964, 0.48532646894454956, 0.48673200607299805, 0.4881472587585449, 0.489448606967926, 0.49082261323928833, 0.4921809434890747, 0.49354809522628784, 0.49487829208374023, 0.4962432384490967, 0.4975869059562683, 0.49886637926101685, 0.5002763271331787]
#plt.plot(DP,'bo',color='blue') 
#plt.plot(dp,'r+',color='red') 
#plt.show()




def P1(t):
    l=24
    m=(2**8)*(500/(t))
    x=1 - (2/(2+m*t**2/(2**l)))**2
    return x

DP=[0]*500

for i in range(1,501):
    DP[i-1]=P1(i)

#plt.plot(DP,'-',color='blue')
#plt.xlabel("t")
#plt.ylabel("Success probability p")
#plt.title("Theoretical point coverage")

DP1=[127011, 252580, 376636, 499386, 620863, 740749, 859570, 976948, 1093061, 1207711, 1321314, 1433663, 1544832, 1654668, 1763325, 1870834, 1977408, 2082831, 2186916, 2289982, 2391841, 2492944, 2592904, 2691724, 2789443, 2886125, 2981687, 3076632, 3170659, 3263678, 3355691, 3446790, 3536832, 3625993, 3714220, 3801485, 3887929, 3973546, 4058279, 4142271, 4225501, 4307898, 4389626, 4470379, 4550452, 4629663, 4708238, 4785882, 4862915, 4938940, 5014362, 5089116, 5163181, 5236607, 5309397, 5381091, 5452611, 5523276, 5593201, 5662716, 5731499, 5799524, 5866901, 5933769, 6000068, 6065485, 6130678, 6195100, 6258991, 6321828, 6384582, 6446673, 6508101, 6569028, 6629516, 6689370, 6748413, 6807282, 6865757, 6923359, 6980461, 7036957, 7092871, 7148675, 7203974, 7258712, 7313047, 7367066, 7420591, 7473565, 7526001, 7577942, 7629680, 7680679, 7731481, 7781723, 7831662, 7881193, 7930195, 7979088, 8027543, 8075557, 8122951, 8169886, 8216666, 8263018, 8308972, 8354587, 8400070, 8445063, 8489894, 8534042, 8577659, 8621009, 8664343, 8707181, 8749612, 8791661, 8833491, 8875029, 8916419, 8957502, 8998009, 9038041, 9077873, 9117621, 9156795, 9195612, 9234195, 9272442, 9310510, 9348482, 9386071, 9423058, 9459796, 9496280, 9532718, 9569147, 9605237, 9640688, 9676419, 9711408, 9745918, 9780618, 9814971, 9848893, 9882777, 9916391, 9949705, 9982689, 10015484, 10048029, 10080347, 10112380, 10144337, 10176066, 10207544, 10238760, 10269616, 10300501, 10331081, 10361391, 10391417, 10421345, 10451036, 10480824, 10510010, 10539071, 10567980, 10596556, 10625247, 10653526, 10681455, 10709584, 10737318, 10765008, 10792548, 10819636, 10846733, 10873751, 10900148, 10926543, 10952903, 10978910, 11004879, 11030575, 11056013, 11081413, 11106563, 11131597, 11156428, 11181042, 11205457, 11229856, 11253812, 11277941, 11301967, 11325936, 11349622, 11373291, 11396755, 11419829, 11442980, 11465644, 11488457, 11511223, 11533842, 11556125, 11578481, 11600667, 11622710, 11644418, 11665986, 11687301, 11708646, 11730145, 11751116, 11772040, 11792733, 11813348, 11833785, 11854378, 11874628, 11894922, 11915206, 11935178, 11954800, 11974430, 11993963, 12013415, 12032670, 12051663, 12070822, 12089805, 12108876, 12127605, 12146260, 12164722, 12183054, 12201226, 12219192, 12237198, 12255220, 12273240, 12290945, 12308624, 12326266, 12343720, 12361014, 12378231, 12395217, 12412186, 12429141, 12445888, 12462682, 12479432, 12495906, 12512304, 12528811, 12544928, 12561011, 12577359, 12593368, 12609318, 12625181, 12640986, 12656521, 12671989, 12687358, 12702840, 12718194, 12733467, 12748702, 12763823, 12778755, 12793574, 12808335, 12823263, 12837855, 12852379, 12866983, 12881310, 12895624, 12909937, 12924134, 12938261, 12952458, 12966376, 12980248, 12994116, 13007785, 13021556, 13035142, 13048689, 13062205, 13075558, 13088918, 13102197, 13115328, 13128387, 13141333, 13154082, 13167043, 13179882, 13192544, 13205200, 13217853, 13230254, 13242827, 13255218, 13267551, 13279864, 13292079, 13304259, 13316462, 13328500, 13340230, 13352084, 13363876, 13375761, 13387517, 13399111, 13410602, 13422041, 13433430, 13444855, 13456147, 13467403, 13478554, 13489554, 13500625, 13511680, 13522823, 13533731, 13544720, 13555593, 13566321, 13577034, 13587773, 13598483, 13608993, 13619584, 13629950, 13640423, 13650999, 13661474, 13671719, 13681954, 13692140, 13702294, 13712259, 13722307, 13732279, 13742227, 13752095, 13761910, 13771752, 13781417, 13791186, 13800672, 13810313, 13819778, 13829252, 13838623, 13848075, 13857449, 13866844, 13876025, 13885081, 13894402, 13903410, 13912559, 13921325, 13930238, 13939163, 13948073, 13956943, 13965801, 13974556, 13983164, 13992025, 14000725, 14009346, 14018103, 14026623, 14034979, 14043557, 14051974, 14060276, 14068596, 14077023, 14085202, 14093483, 14101659, 14109776, 14118097, 14126215, 14134216, 14142233, 14150166, 14158127, 14165986, 14173767, 14181659, 14189486, 14197323, 14204935, 14212666, 14220338, 14228035, 14235505, 14243195, 14250689, 14258155, 14265621, 14273089, 14280455, 14287714, 14294915, 14302228, 14309410, 14316627, 14323790, 14331019, 14338207, 14345317, 14352440, 14359446, 14366502, 14373420, 14380349, 14387227, 14394026, 14400763, 14407562, 14414519, 14421238, 14427958, 14434748, 14441506, 14448233, 14454965, 14461669, 14468396, 14474941, 14481405, 14487855, 14494295, 14500687, 14507097, 14513483, 14519787, 14526084, 14532263, 14538568, 14544751, 14550886, 14557117, 14563355, 14569549, 14575588, 14581683, 14587719, 14593753, 14599719, 14605892, 14611991, 14618010, 14624043, 14629979, 14635966, 14641842, 14647639, 14653495, 14659284, 14665086, 14670823, 14676670, 14682372, 14688058, 14693689, 14699291, 14704773, 14710243, 14715791, 14721262, 14726541, 14732057, 14737588, 14742940, 14748367, 14753709, 14759069, 14764385, 14769826, 14775052, 14780397, 14785614, 14790789, 14795965]

DP1=[DP1[i]/2**24 for i in range(len(DP1))]
#plt.plot(DP1,'-',color='red')
#plt.xlabel("t")
#plt.ylabel("Point coverage")
#plt.title("Point coverage in practice")


DP2=[abs(DP[i]-DP1[i]) for i in range(500)]
plt.plot(DP2,'-',color='green')
plt.xlabel("t")
plt.ylabel("Difference of theoritacal and practical values")
plt.title("Absolute difference between theoritcal and practical values")















