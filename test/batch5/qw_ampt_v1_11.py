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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2200.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2201.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2202.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2203.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2204.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2205.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2206.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2207.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2208.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2209.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2210.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2212.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2213.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2214.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2215.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2216.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2217.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2219.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2220.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2221.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2222.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2223.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2224.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2225.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2226.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2227.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2228.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2229.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2230.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2231.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2232.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2233.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2234.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2235.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2236.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2237.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2238.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2239.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2241.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2242.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2243.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2244.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2245.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2246.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2247.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2248.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2249.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2250.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2251.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2252.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2253.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2254.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2255.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2256.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2257.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2258.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2259.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2260.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2261.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2262.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2263.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2264.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2265.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2266.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2267.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2268.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2269.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2270.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2271.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2272.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2273.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2274.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2275.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2276.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2277.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2278.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2279.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2280.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2281.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2282.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2283.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2284.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2285.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2286.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2287.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2288.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2289.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2290.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2291.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2293.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2294.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2295.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2296.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2297.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2298.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2299.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2300.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2301.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2302.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2303.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2304.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2305.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2306.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2307.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2309.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2310.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2311.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2312.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2313.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2314.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2315.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2316.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2317.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2318.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2320.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2321.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2322.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2323.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2324.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2325.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2326.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2327.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2328.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2329.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2331.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2332.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2333.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2334.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2335.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2337.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2338.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2339.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2340.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2341.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2342.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2343.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2344.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2345.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2346.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2347.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2348.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2349.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2350.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2351.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2352.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2353.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2354.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2355.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2356.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2357.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2358.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2359.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2360.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2361.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2362.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2363.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2364.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2365.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2366.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2367.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2368.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2369.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2370.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2371.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2372.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2373.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2374.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2375.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2376.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2377.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2378.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2379.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2380.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2381.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2382.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2383.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2384.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2385.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2386.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2387.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2388.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2389.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2390.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2391.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2392.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2393.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2395.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2396.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2397.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2398.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2399.root'
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
    fileName = cms.string('AMPTsample_batch5_11_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
