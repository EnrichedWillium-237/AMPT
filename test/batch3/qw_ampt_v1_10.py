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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2000.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2001.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2002.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2004.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2005.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2006.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2007.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2008.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2009.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2011.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2012.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2013.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2014.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2015.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2016.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2017.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2018.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2019.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2020.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2021.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2022.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2023.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2024.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2025.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2026.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2028.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2029.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2030.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2031.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2032.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2035.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2036.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2037.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2038.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2039.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2040.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2041.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2042.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2043.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2044.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2045.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2046.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2048.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2049.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2050.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2051.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2052.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2053.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2054.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2055.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2056.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2057.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2058.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2059.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2060.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2061.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2062.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2063.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2064.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2065.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2066.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2067.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2068.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2069.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2070.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2071.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2073.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2074.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2075.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2076.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2078.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2079.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2080.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2081.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2082.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2083.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2084.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2086.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2087.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2088.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2089.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2090.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2091.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2092.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2093.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2094.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2096.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2097.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2098.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2099.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2100.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2101.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2102.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2103.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2104.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2105.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2106.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2107.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2109.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2110.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2111.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2112.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2113.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2114.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2115.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2116.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2117.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2118.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2119.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2120.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2121.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2122.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2123.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2124.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2125.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2126.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2127.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2128.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2129.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2130.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2131.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2132.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2133.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2134.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2135.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2136.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2137.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2138.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2139.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2140.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2141.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2142.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2143.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2144.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2145.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2146.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2147.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2148.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2149.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2150.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2151.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2152.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2153.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2154.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2155.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2156.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2157.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2158.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2159.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2160.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2161.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2162.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2163.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2164.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2165.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2166.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2167.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2169.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2170.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2171.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2172.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2173.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2174.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2175.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2176.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2177.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2178.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2179.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2180.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2181.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2182.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2183.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2184.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2185.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2186.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2187.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2188.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2190.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2191.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2192.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2193.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2194.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2195.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2196.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2197.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0002/amptDefault_cfi_py_GEN_2199.root'
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
    fileName = cms.string('AMPTsample_batch3_10_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
