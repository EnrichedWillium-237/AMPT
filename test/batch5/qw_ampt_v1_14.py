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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2800.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2801.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2802.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2803.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2804.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2805.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2806.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2807.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2808.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2809.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2810.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2811.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2813.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2814.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2815.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2816.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2817.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2818.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2819.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2821.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2823.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2824.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2825.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2826.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2827.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2828.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2829.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2830.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2833.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2834.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2835.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2838.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2839.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2840.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2841.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2842.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2843.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2844.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2845.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2847.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2850.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2852.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2853.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2854.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2855.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2857.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2858.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2862.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2863.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2864.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2866.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2867.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2868.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2869.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2870.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2871.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2872.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2874.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2875.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2876.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2877.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2878.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2880.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2881.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2882.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2883.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2884.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2886.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2888.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2891.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2894.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2896.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2897.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2900.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2905.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2906.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2908.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2910.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2912.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2916.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2917.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2919.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2920.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2922.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2923.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2924.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2926.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2927.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2928.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2929.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2930.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2931.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2932.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2933.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2934.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2935.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2936.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2937.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2938.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2939.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2940.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2941.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2942.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2943.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2944.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2945.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2949.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2950.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2951.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2952.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2953.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2955.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2956.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2958.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2963.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2964.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2965.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2968.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2972.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2973.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2974.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2977.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2978.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2979.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2982.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2985.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2986.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2987.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2988.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2989.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2990.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2991.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2992.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2993.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2994.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2995.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2996.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2997.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2998.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0002/amptDefault_cfi_py_GEN_2999.root'
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
    fileName = cms.string('AMPTsample_batch5_14_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
