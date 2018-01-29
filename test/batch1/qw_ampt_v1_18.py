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
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3601.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3602.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3603.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3604.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3605.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3606.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3607.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3608.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3609.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3610.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3611.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3612.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3613.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3614.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3615.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3616.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3617.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3618.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3619.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3620.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3621.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3622.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3623.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3624.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3625.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3626.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3628.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3629.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3630.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3631.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3632.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3633.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3634.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3635.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3637.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3638.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3639.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3640.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3641.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3642.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3643.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3644.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3645.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3646.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3647.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3648.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3649.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3650.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3651.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3652.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3653.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3654.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3655.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3656.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3657.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3658.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3659.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3660.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3661.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3662.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3663.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3664.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3665.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3666.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3667.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3669.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3670.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3671.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3672.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3673.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3674.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3675.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3676.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3677.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3678.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3679.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3680.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3681.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3683.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3684.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3685.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3686.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3687.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3688.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3689.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3690.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3691.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3692.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3693.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3695.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3696.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3697.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3698.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3699.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3700.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3701.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3702.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3703.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3704.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3705.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3706.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3707.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3708.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3709.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3710.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3711.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3712.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3713.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3714.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3715.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3716.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3717.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3718.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3719.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3720.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3721.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3722.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3723.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3724.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3725.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3726.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3727.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3728.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3729.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3730.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3731.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3732.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3733.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3734.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3735.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3736.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3737.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3738.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3739.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3740.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3741.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3742.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3743.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3744.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3745.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3746.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3747.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3748.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3749.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3750.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3751.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3752.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3753.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3754.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3755.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3756.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3757.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3758.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3759.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3760.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3761.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3762.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3763.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3764.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3765.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3766.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3767.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3768.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3769.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3770.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3771.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3772.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3773.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3774.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3775.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3777.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3778.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3779.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3780.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3781.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3782.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3783.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3784.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3785.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3786.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3787.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3788.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3789.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3790.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3791.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3792.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3793.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3794.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3795.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3796.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3797.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3798.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3799.root'
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
    fileName = cms.string('AMPTsample_batch1_18.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
