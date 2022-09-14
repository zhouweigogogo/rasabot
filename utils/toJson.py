# -*- coding: UTF-8 -*-
import xlrd

# 猪类疾病表现字典化
# Body_temp_dict = {'体温升高': '1', '体温降低': '2', '体温正常': '3'}
# Skin_dict = {'皮肤正常': '1', '皮肤潮红': '2', '皮肤红肿': '3', '皮肤暗沉': '4', '皮肤有红斑': '5', '皮肤有紫斑': '6', '皮肤发白': '7', '皮肤出血': '8'}
# Hair_color_dict = {'毛色正常': '1', '毛色暗沉': '2', '毛色鲜亮': '3'}
# Breathe_dict = {'呼吸急促': '1', '呼吸正常': '2', '呼吸较慢': '3'}
# Discharge_dict = {'便秘': '1', '腹泻': '2', '正常': '3'}
# Faces_dict = {'粪便较稀': '1', '粪便正常': '2', '粪便较硬': '3'}
# Spirit_dict = {'精神亢奋': '1', '精神低沉': '2', '精神正常': '3'}

# data = xlrd.open_workbook("C:\\Users\\11726\\Desktop\\Pig_diseases.xls")    #打开所需Excel文件
# table = data.sheets()[0]    #索引Excel表中的Sheet1表格
#
# nrows = table.nrows     #获取Sheets1的总行数
# output = []
# for row in range(1,nrows):      #从第二行开始，遍历所有疾病
#     #猪类疾病编码的生成
#     code = ''
#     code = code + Body_temp_dict[table.cell_value(row,3)]
#     code = code + Skin_dict[table.cell_value(row,4)]
#     code = code + Hair_color_dict[table.cell_value(row,5)]
#     code = code + Breathe_dict[table.cell_value(row,6)]
#     code = code + Discharge_dict[table.cell_value(row,7)]
#     code = code + Faces_dict[table.cell_value(row,8)]
#     code = code + Spirit_dict[table.cell_value(row,9)]
#
#     solve = code + ' ' + table.cell_value(row,0) + ':' + table.cell_value(row,2)
#     output.append(solve)
# for i in output:
#     print(i)

# import json
#
# diseases_pig = {"1212212": {"name": "猪瘟",
#                             "symptom": "体温升高41℃左右，稽留不退，精神高度沉郁，喜饮脏水，喜睡怕冷，眼结膜发炎并有脓性眼粪。皮肤病初潮红，后期是苍白贫血，耳尖，四肢内侧，腹下，外阴等处出现紫斑或小出血点，公猪尿脐有积液胀大，初便秘后腹泻呈水样，有的交替进行，便秘时干粪球中常混有白色粘液或血液。急性病程多为1-2周，慢性病程在1个月以上，温和型的，不出现典型症状和病理变化，死亡多为仔猪。",
#                             "treat": "发病后药物治疗无明显效果，贵重猪可用抗猪瘟血清抢救治疗，剂量为1mlkg体重，肌肉或静脉注射。本病防治主要靠免疫接种和综合防治措施。免疫接种可采用超前免疫方案，即在仔猪吃初乳前进行首次接种1-2头份，以后在20日龄，60-65日龄各注射一次；种猪每年春秋各免疫一次。发生疫情后，对疫区和受威胁区采用紧急接种，剂量增加至2-5头份。综合性防治措施，主要是采取自繁、自养，保持环境卫生。"},
#                 "1112222": {"name": "猪口蹄疫",
#                             "symptom": "初期体温升高到40-41℃，减食或停食，继而病猪蹄冠，趾间部发红，以后形成黄豆，蚕豆大小充满灰白色或黄色液体的水疱，水疱破溃后形成暗红色烂斑，病程为1周左右，无继发感染可康复，若继发细菌感染，则会出现局部化脓性坏死，蹄甲脱落。有些猪感染后鼻镜、口腔粘膜和乳房也出现水疱和烂斑。仔猪感染后，常因严重的心肌炎和胃肠炎而死亡。",
#                             "treat": "老疫区和受威胁区可用灭活疫苗预防，肌肉或后海穴注射，大猪2m，小猪1m。平时要加强检疫，发现疫情及时上报。按国家《动物防疫法》规定，病猪和同群猪一律扑杀作无害化处理，不准治疗，并严格封锁疫区，加强消毒，防止扩散。"}}
#
# js = json.dumps(diseases_pig, ensure_ascii=False)
#
# with open("diseases_pig.json", "w", encoding="utf-8") as fp:
#     json.dump(diseases_pig, fp, ensure_ascii=False)
#
# # print(data)
#
# with open("diseases_pig.json", "r", encoding="utf-8") as fp:
#     data = json.load(fp)
#     print(data)
#     print(type(data))
#     ID = "1212212"
#     disease = data[ID]
#     print("疾病名：", disease["name"])
#     print("疾病症状：", disease["symptom"])
#     print("救治措施：", disease["treat"])