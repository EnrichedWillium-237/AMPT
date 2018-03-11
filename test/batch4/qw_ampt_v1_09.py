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
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1800.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1801.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1802.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1803.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1804.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1805.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1806.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1807.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1808.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1809.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1810.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1811.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1812.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1813.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1814.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1815.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1816.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1817.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1818.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1819.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1820.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1821.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1822.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1823.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1824.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1825.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1826.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1827.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1828.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1829.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1830.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1831.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1832.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1833.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1835.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1836.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1837.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1839.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1840.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1841.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1842.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1843.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1844.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1845.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1846.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1847.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1848.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1849.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1850.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1851.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1852.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1853.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1854.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1855.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1856.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1857.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1858.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1860.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1861.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1862.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1863.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1864.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1865.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1866.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1867.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1868.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1869.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1870.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1871.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1872.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1873.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1874.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1875.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1876.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1877.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1878.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1879.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1880.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1881.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1882.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1883.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1884.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1885.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1886.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1887.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1888.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1889.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1890.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1892.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1893.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1894.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1895.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1896.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1897.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1898.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1899.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1900.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1901.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1902.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1903.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1904.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1905.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1906.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1907.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1908.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1909.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1910.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1911.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1912.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1913.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1914.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1915.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1916.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1917.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1918.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1919.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1920.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1921.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1922.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1923.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1924.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1925.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1926.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1927.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1928.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1929.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1930.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1931.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1932.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1933.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1934.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1935.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1936.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1937.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1938.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1939.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1940.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1941.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1942.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1943.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1944.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1945.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1946.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1947.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1948.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1949.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1950.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1951.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1952.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1953.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1954.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1955.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1956.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1957.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1958.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1959.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1960.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1961.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1962.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1963.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1964.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1965.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1966.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1967.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1968.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1969.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1970.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1971.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1972.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1973.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1974.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1975.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1977.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1978.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1979.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1980.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1981.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1983.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1984.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1985.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1986.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1987.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1988.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1989.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1990.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1991.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1992.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1993.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1994.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1995.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1996.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1997.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch4/160318_142915/0001/amptDefault_cfi_py_GEN_1998.root'
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
    fileName = cms.string('AMPTsample_batch4_09.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
