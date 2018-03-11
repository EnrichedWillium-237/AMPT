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
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_2.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_20.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_200.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_201.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_202.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_203.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_204.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_205.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_206.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_207.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_208.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_209.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_21.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_210.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_211.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_212.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_213.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_214.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_216.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_217.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_218.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_219.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_22.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_220.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_221.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_222.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_223.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_224.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_225.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_226.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_227.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_228.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_229.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_23.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_230.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_231.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_232.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_233.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_234.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_235.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_236.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_237.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_238.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_239.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_24.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_240.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_241.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_242.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_243.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_244.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_245.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_246.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_247.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_248.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_249.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_25.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_250.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_251.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_252.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_253.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_254.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_255.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_256.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_259.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_26.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_260.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_261.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_262.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_263.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_264.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_265.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_266.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_267.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_268.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_269.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_27.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_271.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_272.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_273.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_274.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_275.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_276.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_277.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_278.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_279.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_28.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_281.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_282.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_283.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_285.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_286.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_287.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_288.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_289.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_29.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_290.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_291.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_292.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_294.root',
                # '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_295.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_297.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_298.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_299.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_3.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_30.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_300.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_303.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_304.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_305.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_306.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_307.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_308.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_309.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_31.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_310.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_311.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_312.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_313.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_314.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_315.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_317.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_318.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_319.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_32.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_320.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_322.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_323.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_324.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_325.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_326.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_327.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_328.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_329.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_33.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_330.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_331.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_332.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_333.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_334.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_335.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_336.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_338.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_339.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_34.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_340.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_341.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_342.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_343.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_344.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_345.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_346.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_347.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_348.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_349.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_35.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_350.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_351.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_352.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_353.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_354.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_355.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_356.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_357.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_358.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_359.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_36.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_360.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_361.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_363.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_364.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_365.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_366.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_367.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_368.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_369.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_37.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_370.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_372.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_373.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_374.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_375.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_376.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_377.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_378.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_379.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_380.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_381.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_382.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_383.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_384.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_385.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_386.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_387.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_389.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_39.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_391.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_392.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_393.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_394.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_395.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_396.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_397.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_398.root',
                '/store/user/davidlw/AMPT_PbPb5TeV_Gen/mb_string_batch3/160222_030946/0000/amptDefault_cfi_py_GEN_399.root'
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
    fileName = cms.string('AMPTsample_batch3_01_v3.root')
)

process.ana = cms.Path(process.GeneInfo * process.QWEvent * process.QWTreeMaker * process.QWHepMC * process.QWHepMCMaker)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

process.schedule = cms.Schedule(
    process.ana,
#    process.RAWSIMoutput_step,
)
