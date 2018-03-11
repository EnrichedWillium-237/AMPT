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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4200.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4201.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4202.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4203.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4204.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4205.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4206.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4207.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4208.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4209.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4211.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4212.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4213.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4214.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4215.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4216.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4217.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4218.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4219.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4220.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4221.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4222.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4223.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4224.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4225.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4226.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4227.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4228.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4229.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4230.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4231.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4232.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4233.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4234.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4235.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4236.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4237.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4239.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4240.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4241.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4242.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4243.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4244.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4245.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4246.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4247.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4248.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4249.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4250.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4251.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4252.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4253.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4254.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4255.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4256.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4257.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4258.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4259.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4260.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4261.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4262.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4263.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4264.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4265.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4266.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4267.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4268.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4269.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4270.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4271.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4273.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4274.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4275.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4276.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4277.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4278.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4279.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4280.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4281.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4282.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4283.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4284.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4285.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4286.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4287.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4288.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4289.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4290.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4291.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4292.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4293.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4294.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4295.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4296.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4297.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4298.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4299.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4300.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4301.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4302.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4303.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4304.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4305.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4306.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4307.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4308.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4309.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4311.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4312.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4313.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4314.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4315.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4316.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4317.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4318.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4319.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4320.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4321.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4323.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4324.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4325.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4327.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4328.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4329.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4330.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4331.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4332.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4333.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4334.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4335.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4336.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4337.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4338.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4339.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4340.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4341.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4342.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4343.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4344.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4345.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4346.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4347.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4348.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4349.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4350.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4351.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4352.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4353.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4354.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4355.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4356.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4357.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4358.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4359.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4360.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4361.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4362.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4363.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4364.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4365.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4366.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4367.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4368.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4369.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4370.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4371.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4372.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4373.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4374.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4375.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4376.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4378.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4379.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4380.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4381.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4382.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4383.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4384.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4385.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4386.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4388.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4389.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4390.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4391.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4392.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4393.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4395.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4396.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4397.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4398.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0004/amptDefault_cfi_py_GEN_4399.root'
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
    fileName = cms.string('AMPTsample_batch3_21_v2.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
