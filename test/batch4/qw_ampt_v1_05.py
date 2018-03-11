import FWCore.ParameterSet.Config as cms

process = cms.Process("AMPT")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.Generator_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(500000))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

# process.source = cms.Source("PoolSource",
# 		fileNames = cms.untracked.vstring('file:output.root','),
# 		secondaryFileNames = cms.untracked.vstring()
# 		)
# process.source = cms.Source("PoolSource",
# 		fileNames = cms.untracked.vstring('/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0000/amptDefault_cfi_py_GEN_1.root'),
# 		)
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring( *(
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1001.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1002.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1003.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1004.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1005.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1006.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1007.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1008.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1009.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1010.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1011.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1012.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1013.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1014.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1015.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1016.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1017.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1018.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1019.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1020.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1021.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1022.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1023.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1024.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1025.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1026.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1027.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1028.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1029.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1030.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1031.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1032.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1033.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1035.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1036.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1037.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1038.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1039.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1040.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1041.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1042.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1043.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1044.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1045.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1046.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1047.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1048.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1049.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1050.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1051.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1052.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1053.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1054.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1056.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1057.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1058.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1059.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1060.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1061.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1062.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1063.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1064.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1065.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1066.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1067.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1068.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1069.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1070.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1071.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1072.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1073.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1074.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1075.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1076.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1077.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1078.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1079.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1080.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1081.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1082.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1083.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1084.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1085.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1086.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1087.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1088.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1089.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1090.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1091.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1092.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1093.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1094.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1095.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1096.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1097.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1098.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1099.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1100.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1101.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1102.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1103.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1104.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1105.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1106.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1107.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1108.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1109.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1110.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1111.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1112.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1113.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1114.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1115.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1116.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1117.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1118.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1119.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1120.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1121.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1122.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1123.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1124.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1125.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1126.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1127.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1128.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1129.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1130.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1131.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1132.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1133.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1134.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1135.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1136.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1137.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1138.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1139.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1140.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1141.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1142.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1143.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1144.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1145.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1146.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1147.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1148.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1149.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1151.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1152.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1154.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1155.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1156.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1157.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1158.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1159.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1160.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1161.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1162.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1163.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1164.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1165.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1166.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1167.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1168.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1169.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1170.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1171.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1172.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1173.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1174.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1175.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1176.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1177.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1178.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1179.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1180.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1181.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1182.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1183.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1184.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1185.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1186.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1187.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1188.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1189.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1190.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1191.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1192.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1193.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1194.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1195.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1197.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1198.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1199.root'
                ) )
        )

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string('ampt.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('ana')
    )
)


process.QWEvent = cms.EDProducer("QWGenEventProducer",
		trackSrc  = cms.untracked.InputTag("genParticles"),
		isPrompt  = cms.untracked.bool(False),
		Etamin = cms.untracked.double(-5.0),
		Etamax = cms.untracked.double(5.0),
		ptMin = cms.untracked.double(0.3),
		ptMax = cms.untracked.double(12.0),
		)

process.QWHepMC = cms.EDProducer('QWHepMCProducer',
		src = cms.untracked.InputTag('generator')
		)

process.QWTreeMaker = cms.EDAnalyzer('QWTreeMaker',
		src = cms.untracked.InputTag('QWEvent'),
		vTag = cms.untracked.vstring('phi', 'eta', 'pt', 'charge')
		)

process.QWHepMCMaker = cms.EDAnalyzer('QWDTreeMaker',
		src = cms.untracked.InputTag('QWHepMC'),
		vTag = cms.untracked.vstring('b', 'EP', 'Npart', 'Ncoll')
		)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('AMPTsample_batch4_05.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
