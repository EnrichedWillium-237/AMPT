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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1400.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1401.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1402.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1403.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1404.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1406.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1407.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1408.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1409.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1410.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1411.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1412.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1413.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1414.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1415.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1416.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1417.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1418.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1419.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1420.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1421.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1422.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1423.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1424.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1425.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1426.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1427.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1428.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1429.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1430.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1431.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1432.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1433.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1434.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1435.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1436.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1437.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1438.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1439.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1440.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1441.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1442.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1443.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1444.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1445.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1446.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1447.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1448.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1449.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1450.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1451.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1452.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1453.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1454.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1455.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1456.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1457.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1458.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1459.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1460.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1461.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1462.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1463.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1464.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1465.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1466.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1467.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1468.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1469.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1470.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1471.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1472.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1473.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1474.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1475.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1477.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1478.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1479.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1480.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1482.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1483.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1484.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1485.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1486.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1487.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1488.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1489.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1490.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1491.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1492.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1494.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1495.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1496.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1497.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1498.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1499.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1500.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1501.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1502.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1504.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1505.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1506.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1508.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1509.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1510.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1511.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1512.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1513.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1514.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1515.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1517.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1518.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1519.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1520.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1521.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1522.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1523.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1524.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1525.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1526.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1529.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1531.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1532.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1533.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1534.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1535.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1536.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1537.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1538.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1539.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1540.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1541.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1542.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1544.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1545.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1546.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1547.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1548.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1549.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1550.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1551.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1552.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1553.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1554.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1555.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1556.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1557.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1558.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1559.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1560.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1561.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1562.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1563.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1564.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1565.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1566.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1567.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1568.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1569.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1570.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1571.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1572.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1573.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1574.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1575.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1576.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1577.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1578.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1579.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1580.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1581.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1582.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1583.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1584.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1585.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1586.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1587.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1588.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1589.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1590.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1591.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1592.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1593.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1594.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1595.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1596.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1597.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0001/amptDefault_cfi_py_GEN_1599.root'
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
    fileName = cms.string('AMPTsample_batch3_07_v3.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
