import FWCore.ParameterSet.Config as cms

process = cms.Process("AMPT")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.Generator_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100000))
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
                 '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1200.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1201.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1202.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1203.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1204.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1205.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1206.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1207.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1208.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1209.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1210.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1211.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1212.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1213.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1214.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1215.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1216.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1217.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1218.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1219.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1221.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1222.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1223.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1224.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1225.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1226.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1227.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1229.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1230.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1231.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1232.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1233.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1234.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1235.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1236.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1237.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1238.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1239.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1240.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1241.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1242.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1243.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1244.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1245.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1246.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1247.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1248.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1249.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1250.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1251.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1252.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1253.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1254.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1255.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1256.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1257.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1258.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1259.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1260.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1261.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1262.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1263.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1264.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1265.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1266.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1268.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1269.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1270.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1271.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1272.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1273.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1274.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1275.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1276.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1277.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1278.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1279.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1280.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1281.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1282.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1283.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1284.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1285.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1286.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1287.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1288.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1289.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1290.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1291.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1292.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1293.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1294.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1295.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1296.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1297.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1298.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1299.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1300.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1301.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1302.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1303.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1304.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1305.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1307.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1308.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1309.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1310.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1311.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1313.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1314.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1316.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1317.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1318.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1319.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1320.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1322.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1323.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1324.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1325.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1326.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1327.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1328.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1329.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1330.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1331.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1332.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1333.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1334.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1335.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1336.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1337.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1338.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1339.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1340.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1341.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1342.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1343.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1344.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1345.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1346.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1347.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1348.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1349.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1350.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1351.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1352.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1353.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1354.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1355.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1356.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1357.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1358.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1359.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1360.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1361.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1362.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1363.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1364.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1365.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1366.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1367.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1368.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1369.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1370.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1371.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1372.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1373.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1374.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1375.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1376.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1377.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1378.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1379.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1380.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1381.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1382.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1383.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1384.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1385.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1386.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1387.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1388.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1389.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1390.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1391.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1392.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1393.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1394.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1395.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1396.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1397.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1398.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0001/amptDefault_cfi_py_GEN_1399.root'
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
    fileName = cms.string('AMPTsample_batch6_07.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
