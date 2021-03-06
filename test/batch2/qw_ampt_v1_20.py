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
                                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3000.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3001.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3002.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3003.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3004.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3005.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3006.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3007.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3008.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3009.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3010.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3011.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3012.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3013.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3014.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3015.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3016.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3017.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3018.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3019.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3020.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3021.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3022.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3023.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3024.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3025.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3026.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3027.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3028.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3029.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3030.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3031.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3032.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3033.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3034.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3035.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3036.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3037.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3038.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3039.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3040.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3041.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3042.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3043.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3044.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3045.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3046.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3048.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3049.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3050.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3051.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3053.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3054.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3055.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3056.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3057.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3058.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3059.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3060.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3061.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3062.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3063.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3064.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3065.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3066.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3067.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3068.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3070.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3071.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3072.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3073.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3074.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3075.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3076.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3077.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3078.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3079.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3080.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3081.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3082.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3083.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3084.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3085.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3086.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3087.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3088.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3089.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3090.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3091.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3092.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3093.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3094.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3095.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3096.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3097.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3098.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3099.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3100.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3101.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3102.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3103.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3104.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3105.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3106.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3107.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3108.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3109.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3110.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3111.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3113.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3114.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3115.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3116.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3117.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3118.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3119.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3120.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3121.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3122.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3123.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3124.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3125.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3126.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3127.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3129.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3130.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3131.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3132.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3133.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3134.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3135.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3136.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3137.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3138.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3139.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3140.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3141.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3142.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3143.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3144.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3145.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3146.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3147.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3148.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3149.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3150.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3151.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3152.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3153.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3154.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3155.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3156.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3157.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3158.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3159.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3160.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3161.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3162.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3163.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3164.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3165.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3166.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3167.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3168.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3169.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3170.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3171.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3172.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3173.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3174.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3175.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3176.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3177.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3179.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3180.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3181.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3182.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3183.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3185.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3186.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3187.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3188.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3189.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3190.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3191.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3192.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3193.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3195.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3196.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3197.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3198.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch2/160220_111702/0003/amptDefault_cfi_py_GEN_3199.root'
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
    fileName = cms.string('AMPTsample_20.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
