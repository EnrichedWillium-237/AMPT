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
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2400.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2401.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2402.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2403.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2404.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2405.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2407.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2408.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2409.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2410.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2411.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2412.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2413.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2414.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2415.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2416.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2417.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2418.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2419.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2420.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2421.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2422.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2423.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2424.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2426.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2427.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2428.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2429.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2430.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2431.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2432.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2433.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2434.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2436.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2437.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2438.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2440.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2441.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2442.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2443.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2444.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2445.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2446.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2448.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2449.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2450.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2451.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2452.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2453.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2454.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2455.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2456.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2457.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2458.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2459.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2460.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2461.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2462.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2463.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2464.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2465.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2466.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2467.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2468.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2469.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2470.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2471.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2472.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2473.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2474.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2475.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2476.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2477.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2478.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2479.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2480.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2481.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2482.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2483.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2484.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2485.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2486.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2487.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2489.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2490.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2491.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2492.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2493.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2494.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2495.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2496.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2497.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2498.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2499.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2500.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2501.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2502.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2503.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2504.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2505.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2506.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2507.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2508.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2509.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2510.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2511.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2512.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2513.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2514.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2516.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2517.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2518.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2519.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2520.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2521.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2522.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2523.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2524.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2525.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2526.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2528.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2529.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2530.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2531.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2532.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2533.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2534.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2535.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2536.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2537.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2538.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2539.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2540.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2541.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2542.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2543.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2545.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2546.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2548.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2549.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2550.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2551.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2552.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2553.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2554.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2555.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2556.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2557.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2558.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2559.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2560.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2561.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2562.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2563.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2564.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2565.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2566.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2567.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2568.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2569.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2570.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2571.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2572.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2573.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2574.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2575.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2576.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2577.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2578.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2579.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2580.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2581.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2582.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2583.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2584.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2585.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2586.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2587.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2588.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2589.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2590.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2591.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2592.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2593.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2594.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2595.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2596.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2597.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2598.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0002/amptDefault_cfi_py_GEN_2599.root'
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
    fileName = cms.string('AMPTsample_batch1_12.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
