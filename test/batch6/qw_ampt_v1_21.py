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
                    '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4000.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4001.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4002.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4003.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4004.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4005.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4006.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4007.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4008.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4009.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4010.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4011.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4012.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4013.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4014.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4015.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4016.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4017.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4019.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4020.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4021.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4022.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4023.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4024.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4025.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4026.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4027.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4028.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4029.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4030.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4031.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4032.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4033.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4034.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4035.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4036.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4037.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4038.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4039.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4040.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4041.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4042.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4043.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4044.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4045.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4046.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4047.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4048.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4050.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4051.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4052.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4053.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4054.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4055.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4056.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4057.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4058.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4059.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4060.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4061.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4062.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4063.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4064.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4065.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4066.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4067.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4068.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4069.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4070.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4071.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4072.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4073.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4074.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4075.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4076.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4077.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4078.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4079.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4080.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4081.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4082.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4083.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4084.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4085.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4086.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4087.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4088.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4089.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4090.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4091.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4092.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4093.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4094.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4095.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4096.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4097.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4098.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4099.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4100.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4101.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4102.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4103.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4104.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4105.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4106.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4107.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4108.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4109.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4110.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4111.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4112.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4113.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4114.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4115.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4116.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4117.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4118.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4119.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4120.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4121.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4122.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4123.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4124.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4125.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4126.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4127.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4128.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4129.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4131.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4132.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4133.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4134.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4135.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4136.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4137.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4138.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4139.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4140.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4141.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4142.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4143.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4144.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4145.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4146.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4147.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4148.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4149.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4150.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4151.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4152.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4153.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4154.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4155.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4156.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4157.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4158.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4160.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4161.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4162.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4163.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4164.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4165.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4166.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4167.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4168.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4169.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4170.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4171.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4172.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4173.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4174.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4175.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4176.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4177.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4178.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4179.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4180.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4182.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4183.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4184.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4185.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4186.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4187.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4188.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4189.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4190.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4191.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4192.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4193.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4194.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4195.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4196.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4197.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4198.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch6/160318_143120/0004/amptDefault_cfi_py_GEN_4199.root'
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
    fileName = cms.string('AMPTsample_batch6_21.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
