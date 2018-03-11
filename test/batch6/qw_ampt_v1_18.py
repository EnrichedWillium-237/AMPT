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
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3400.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3401.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3402.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3403.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3404.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3405.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3406.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3407.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3408.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3409.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3410.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3411.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3412.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3413.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3414.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3415.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3416.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3417.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3418.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3419.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3420.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3421.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3422.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3423.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3424.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3425.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3426.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3427.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3428.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3429.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3430.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3431.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3432.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3433.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3434.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3435.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3436.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3437.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3438.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3439.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3440.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3441.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3442.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3443.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3444.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3445.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3446.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3447.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3448.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3449.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3450.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3451.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3452.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3453.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3454.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3455.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3456.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3457.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3458.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3459.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3460.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3461.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3462.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3463.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3464.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3465.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3466.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3467.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3468.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3469.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3470.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3471.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3472.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3473.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3474.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3475.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3476.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3477.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3478.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3479.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3480.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3481.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3482.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3484.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3485.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3486.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3487.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3488.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3489.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3490.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3491.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3492.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3493.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3494.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3495.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3496.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3497.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3498.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3499.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3500.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3501.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3502.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3503.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3504.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3505.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3506.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3507.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3508.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3509.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3510.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3511.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3512.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3513.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3514.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3515.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3516.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3517.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3518.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3519.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3520.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3521.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3522.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3523.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3524.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3526.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3527.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3528.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3529.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3530.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3531.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3532.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3533.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3534.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3535.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3536.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3537.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3538.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3539.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3540.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3541.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3542.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3543.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3544.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3545.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3546.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3547.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3548.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3549.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3550.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3551.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3552.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3553.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3554.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3555.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3556.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3557.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3558.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3559.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3560.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3562.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3563.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3564.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3565.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3566.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3567.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3568.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3569.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3570.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3571.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3572.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3573.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3574.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3575.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3576.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3577.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3578.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3579.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3580.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3581.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3582.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3583.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3584.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3585.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3586.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3587.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3588.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3589.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3590.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3591.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3592.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3593.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3594.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3595.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3596.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3597.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3598.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0003/amptDefault_cfi_py_GEN_3599.root'
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
    fileName = cms.string('AMPTsample_batch6_18.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
