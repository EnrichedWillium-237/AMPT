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
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3800.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3801.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3802.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3803.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3804.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3805.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3806.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3807.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3808.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3809.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3810.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3811.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3812.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3813.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3814.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3815.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3816.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3817.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3818.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3819.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3820.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3821.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3822.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3823.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3824.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3825.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3826.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3827.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3828.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3829.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3830.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3831.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3832.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3833.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3834.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3835.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3836.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3837.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3838.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3839.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3840.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3841.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3842.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3843.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3844.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3845.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3846.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3847.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3848.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3849.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3850.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3851.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3852.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3853.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3854.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3855.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3856.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3857.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3858.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3859.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3860.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3861.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3862.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3863.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3864.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3865.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3866.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3867.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3869.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3870.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3871.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3872.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3873.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3874.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3875.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3876.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3877.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3878.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3879.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3880.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3881.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3882.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3883.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3884.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3885.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3886.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3887.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3888.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3889.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3890.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3891.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3892.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3893.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3894.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3895.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3896.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3897.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3898.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3899.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3900.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3901.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3902.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3903.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3904.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3905.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3906.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3907.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3908.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3909.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3910.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3911.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3912.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3913.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3914.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3915.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3916.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3917.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3918.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3919.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3920.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3921.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3922.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3923.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3924.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3925.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3926.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3927.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3928.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3929.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3930.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3931.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3932.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3933.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3934.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3935.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3936.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3937.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3938.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3939.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3940.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3941.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3942.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3943.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3944.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3945.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3946.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3947.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3948.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3949.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3950.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3951.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3952.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3953.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3954.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3955.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3956.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3957.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3958.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3959.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3960.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3961.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3962.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3963.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3964.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3965.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3966.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3967.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3968.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3969.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3970.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3971.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3972.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3973.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3974.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3975.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3976.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3977.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3978.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3979.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3980.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3981.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3982.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3983.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3984.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3985.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3986.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3987.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3988.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3989.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3990.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3991.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3993.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3994.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3995.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3996.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3997.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3998.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch1/160219_191452/0003/amptDefault_cfi_py_GEN_3999.root'
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
    fileName = cms.string('AMPTsample_batch1_19.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
