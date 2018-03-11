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
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1601.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1602.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1603.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1604.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1605.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1606.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1607.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1608.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1609.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1610.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1611.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1612.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1613.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1614.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1615.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1616.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1617.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1618.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1619.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1620.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1621.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1622.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1623.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1624.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1626.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1627.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1629.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1630.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1631.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1632.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1633.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1634.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1635.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1636.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1637.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1638.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1639.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1640.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1641.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1642.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1643.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1644.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1645.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1646.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1649.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1650.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1651.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1652.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1653.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1654.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1656.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1657.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1658.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1659.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1660.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1661.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1662.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1663.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1664.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1665.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1666.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1667.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1668.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1669.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1670.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1671.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1672.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1673.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1674.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1675.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1676.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1677.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1678.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1679.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1681.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1682.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1683.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1684.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1685.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1686.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1687.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1688.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1689.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1690.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1691.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1692.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1693.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1694.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1695.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1696.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1697.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1698.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1699.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1700.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1701.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1702.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1703.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1704.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1705.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1706.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1707.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1708.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1709.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1710.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1711.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1712.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1713.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1714.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1715.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1716.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1717.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1718.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1719.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1720.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1721.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1722.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1723.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1724.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1725.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1726.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1727.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1728.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1729.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1730.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1731.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1733.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1734.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1735.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1736.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1737.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1738.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1739.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1740.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1741.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1742.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1743.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1744.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1745.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1746.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1747.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1748.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1749.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1750.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1751.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1752.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1753.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1754.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1755.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1756.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1757.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1758.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1759.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1760.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1761.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1762.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1763.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1764.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1765.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1766.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1767.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1768.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1769.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1770.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1771.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1772.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1773.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1774.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1775.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1776.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1777.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1778.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1779.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1780.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1781.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1782.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1783.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1784.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1785.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1786.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1787.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1788.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1789.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1790.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1791.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1792.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1793.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1794.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1795.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1796.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1797.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1798.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1799.root'
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
    fileName = cms.string('AMPTsample_batch4_08.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
