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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2600.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2601.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2602.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2603.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2604.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2605.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2606.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2608.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2609.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2610.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2611.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2612.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2613.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2614.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2615.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2616.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2617.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2618.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2619.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2620.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2621.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2622.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2623.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2624.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2625.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2626.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2627.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2628.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2629.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2630.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2631.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2632.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2633.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2634.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2635.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2636.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2637.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2638.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2639.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2640.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2641.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2642.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2643.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2644.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2646.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2647.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2648.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2649.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2650.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2651.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2652.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2653.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2654.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2655.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2656.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2657.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2658.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2659.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2660.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2661.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2662.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2663.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2664.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2665.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2666.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2667.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2668.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2669.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2670.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2671.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2672.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2673.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2674.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2675.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2676.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2677.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2679.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2682.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2683.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2684.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2686.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2687.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2688.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2689.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2690.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2692.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2693.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2694.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2695.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2696.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2697.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2699.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2700.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2701.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2702.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2703.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2704.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2705.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2706.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2707.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2708.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2709.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2710.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2711.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2712.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2713.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2714.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2715.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2716.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2717.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2718.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2719.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2720.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2721.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2722.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2723.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2724.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2725.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2726.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2727.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2729.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2730.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2731.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2732.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2733.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2734.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2735.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2736.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2737.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2738.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2739.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2740.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2741.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2742.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2743.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2744.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2745.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2746.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2747.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2748.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2749.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2750.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2751.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2752.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2753.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2754.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2755.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2756.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2757.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2758.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2759.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2760.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2761.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2762.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2763.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2764.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2765.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2766.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2767.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2768.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2769.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2770.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2771.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2772.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2773.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2774.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2775.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2776.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2777.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2778.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2779.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2780.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2781.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2782.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2783.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2784.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2785.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2786.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2787.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2788.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2789.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2790.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2791.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2793.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2794.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2795.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2796.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2797.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2798.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2799.root'
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
    fileName = cms.string('AMPTsample_batch5_13_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
