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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3200.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3201.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3202.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3203.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3204.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3205.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3206.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3207.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3208.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3209.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3210.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3211.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3212.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3213.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3214.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3215.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3216.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3217.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3218.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3219.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3220.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3221.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3222.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3223.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3224.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3225.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3226.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3227.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3228.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3229.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3230.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3231.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3232.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3233.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3234.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3235.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3236.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3237.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3238.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3239.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3240.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3241.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3242.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3243.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3244.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3245.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3246.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3247.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3248.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3249.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3250.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3251.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3252.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3253.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3254.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3255.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3256.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3257.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3258.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3259.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3260.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3261.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3262.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3263.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3264.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3265.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3266.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3267.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3268.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3269.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3270.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3271.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3272.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3273.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3274.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3275.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3276.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3277.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3278.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3279.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3280.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3281.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3282.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3283.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3284.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3285.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3286.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3287.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3288.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3289.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3290.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3291.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3292.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3293.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3294.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3295.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3296.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3297.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3298.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3299.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3300.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3301.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3302.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3303.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3304.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3305.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3306.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3307.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3308.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3309.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3310.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3311.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3312.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3314.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3315.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3316.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3318.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3319.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3320.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3321.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3322.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3323.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3324.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3325.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3326.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3327.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3328.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3329.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3330.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3332.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3334.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3335.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3336.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3337.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3338.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3339.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3341.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3342.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3343.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3344.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3345.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3346.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3347.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3348.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3349.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3350.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3351.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3352.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3353.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3354.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3355.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3356.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3357.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3358.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3359.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3360.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3361.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3362.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3363.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3364.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3365.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3366.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3367.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3368.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3369.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3370.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3371.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3372.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3373.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3374.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3375.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3376.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3377.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3378.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3379.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3380.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3381.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3382.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3383.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3384.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3385.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3386.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3387.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3388.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3389.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3390.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3391.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3392.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3393.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3394.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3395.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3396.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3397.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3398.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch5/160318_143041/0003/amptDefault_cfi_py_GEN_3399.root'
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
    fileName = cms.string('AMPTsample_batch5_16_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
