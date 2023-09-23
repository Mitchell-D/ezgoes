"""
Descriptions of ABI products from the NOAA github page here:
https://github.com/awslabs/open-data-docs/tree/main/docs/noaa/noaa-goes16

Also, hard-coded instances of valid GOES_Products (as of 20230817).
This list may need to be updated at times, which can be done by copying
the dictionary returned by GetGOES()._get_product_api().
"""

from collections import namedtuple

GOES_Product = namedtuple(
        "GOES_Product", "satellite sensor level scan", defaults=(None,)*4)
GOES_File = namedtuple(
        "GOES_File", "product stime label path", defaults=(None,)*4)

goes_products = [
        GOES_Product(satellite='17', sensor='ABI', level='L1b', scan='RadC'),
        GOES_Product(satellite='17', sensor='ABI', level='L1b', scan='RadF'),
        GOES_Product(satellite='17', sensor='ABI', level='L1b', scan='RadM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACHAC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACHAF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACHAM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACHTF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACHTM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACMC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACMF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACMM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACTPC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACTPF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ACTPM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ADPC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ADPF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='ADPM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='AICEF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='AITAF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='AODC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='AODF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='BRFC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='BRFF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='BRFM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CMIPC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CMIPF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CMIPM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CODC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CODF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CPSC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CPSF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CPSM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CTPC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='CTPF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DMWC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DMWF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DMWM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DMWVC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DMWVF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DMWVM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DSIC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DSIF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DSIM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DSRC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DSRF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='DSRM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='FDCC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='FDCF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='FDCM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LSAC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LSAF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LSAM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LST2KMF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LSTC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LSTF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LSTM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LVMPC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LVMPF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LVMPM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LVTPC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LVTPF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='LVTPM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='MCMIPC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='MCMIPF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='MCMIPM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='RRQPEF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='RSRC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='RSRF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='SSTF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='TPWC'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='TPWF'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='TPWM'),
        GOES_Product(satellite='17', sensor='ABI', level='L2', scan='VAAF'),
        GOES_Product(satellite='17', sensor='EXIS', level='L1b', scan='SFEU'),
        GOES_Product(satellite='17', sensor='EXIS', level='L1b', scan='SFXR'),
        GOES_Product(satellite='17', sensor='GLM', level='L2', scan='LCFA'),
        GOES_Product(satellite='17', sensor='MAG', level='L1b', scan='GEOF'),
        GOES_Product(satellite='17', sensor='SEIS', level='L1b', scan='EHIS'),
        GOES_Product(satellite='17', sensor='SEIS', level='L1b', scan='MPSH'),
        GOES_Product(satellite='17', sensor='SEIS', level='L1b', scan='MPSL'),
        GOES_Product(satellite='17', sensor='SEIS', level='L1b', scan='SGPS'),
        GOES_Product(satellite='17', sensor='SUVI', level='L1b', scan='Fe093'),
        GOES_Product(satellite='17', sensor='SUVI', level='L1b', scan='Fe131'),
        GOES_Product(satellite='17', sensor='SUVI', level='L1b', scan='Fe171'),
        GOES_Product(satellite='17', sensor='SUVI', level='L1b', scan='Fe195'),
        GOES_Product(satellite='17', sensor='SUVI', level='L1b', scan='Fe284'),
        GOES_Product(satellite='17', sensor='SUVI', level='L1b', scan='He303'),
        GOES_Product(satellite='18', sensor='ABI', level='L1b', scan='RadC'),
        GOES_Product(satellite='18', sensor='ABI', level='L1b', scan='RadF'),
        GOES_Product(satellite='18', sensor='ABI', level='L1b', scan='RadM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHA2KMC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHA2KMF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHA2KMM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHAC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHAF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHAM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHP2KMC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHP2KMF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHP2KMM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHTF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACHTM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACMC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACMF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACMM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACTPC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACTPF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ACTPM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ADPC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ADPF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='ADPM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='AICEF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='AITAF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='AODC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='AODF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='BRFC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='BRFF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='BRFM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CCLC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CCLF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CCLM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CMIPC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CMIPF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CMIPM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='COD2KMF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CODC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CODF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CPSC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CPSF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CPSM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CTPC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='CTPF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DMWC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DMWF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DMWM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DMWVC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DMWVF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DMWVM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DSIC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DSIF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DSIM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DSRC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DSRF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='DSRM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='FDCC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='FDCF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='FDCM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='FSCC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='FSCF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='FSCM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LSAC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LSAF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LSAM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LST2KMF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LSTC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LSTF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LSTM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LVMPC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LVMPF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LVMPM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LVTPC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LVTPF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='LVTPM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='MCMIPC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='MCMIPF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='MCMIPM'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='RRQPEF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='RSRC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='RSRF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='SSTF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='TPWC'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='TPWF'),
        GOES_Product(satellite='18', sensor='ABI', level='L2', scan='TPWM'),
        GOES_Product(satellite='18', sensor='EXIS', level='L1b', scan='SFEU'),
        GOES_Product(satellite='18', sensor='EXIS', level='L1b', scan='SFXR'),
        GOES_Product(satellite='18', sensor='GLM', level='L2', scan='LCFA'),
        GOES_Product(satellite='18', sensor='MAG', level='L1b', scan='GEOF'),
        GOES_Product(satellite='18', sensor='SEIS', level='L1b', scan='EHIS'),
        GOES_Product(satellite='18', sensor='SEIS', level='L1b', scan='MPSH'),
        GOES_Product(satellite='18', sensor='SEIS', level='L1b', scan='MPSL'),
        GOES_Product(satellite='18', sensor='SEIS', level='L1b', scan='SGPS'),
        GOES_Product(satellite='18', sensor='SUVI', level='L1b', scan='Fe093'),
        GOES_Product(satellite='18', sensor='SUVI', level='L1b', scan='Fe131'),
        GOES_Product(satellite='18', sensor='SUVI', level='L1b', scan='Fe171'),
        GOES_Product(satellite='18', sensor='SUVI', level='L1b', scan='Fe195'),
        GOES_Product(satellite='18', sensor='SUVI', level='L1b', scan='Fe284'),
        GOES_Product(satellite='18', sensor='SUVI', level='L1b', scan='He303'),
        GOES_Product(satellite='16', sensor='ABI', level='L1b', scan='RadC'),
        GOES_Product(satellite='16', sensor='ABI', level='L1b', scan='RadF'),
        GOES_Product(satellite='16', sensor='ABI', level='L1b', scan='RadM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHA2KMC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHA2KMF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHA2KMM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHAC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHAF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHAM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHP2KMC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHP2KMF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHP2KMM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHTF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACHTM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACMC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACMF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACMM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACTPC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACTPF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ACTPM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ADPC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ADPF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='ADPM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='AICEF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='AITAF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='AODC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='AODF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='BRFC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='BRFF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='BRFM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CCLC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CCLF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CCLM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CMIPC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CMIPF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CMIPM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='COD2KMF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CODC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CODF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CPSC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CPSF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CPSM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CTPC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='CTPF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DMWC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DMWF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DMWM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DMWVC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DMWVF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DMWVM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DSIC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DSIF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DSIM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DSRC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DSRF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='DSRM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='FDCC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='FDCF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='FDCM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='FSCC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='FSCF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='FSCM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LSAC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LSAF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LSAM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LST2KMF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LSTC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LSTF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LSTM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LVMPC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LVMPF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LVMPM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LVTPC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LVTPF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='LVTPM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='MCMIPC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='MCMIPF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='MCMIPM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='RRQPEF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='RSRC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='RSRF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='SSTF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='TPWC'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='TPWF'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='TPWM'),
        GOES_Product(satellite='16', sensor='ABI', level='L2', scan='VAAF'),
        GOES_Product(satellite='16', sensor='EXIS', level='L1b', scan='SFEU'),
        GOES_Product(satellite='16', sensor='EXIS', level='L1b', scan='SFXR'),
        GOES_Product(satellite='16', sensor='GLM', level='L2', scan='LCFA'),
        GOES_Product(satellite='16', sensor='MAG', level='L1b', scan='GEOF'),
        GOES_Product(satellite='16', sensor='SEIS', level='L1b', scan='EHIS'),
        GOES_Product(satellite='16', sensor='SEIS', level='L1b', scan='MPSH'),
        GOES_Product(satellite='16', sensor='SEIS', level='L1b', scan='MPSL'),
        GOES_Product(satellite='16', sensor='SEIS', level='L1b', scan='SGPS'),
        GOES_Product(satellite='16', sensor='SUVI', level='L1b', scan='Fe093'),
        GOES_Product(satellite='16', sensor='SUVI', level='L1b', scan='Fe131'),
        GOES_Product(satellite='16', sensor='SUVI', level='L1b', scan='Fe171'),
        GOES_Product(satellite='16', sensor='SUVI', level='L1b', scan='Fe195'),
        GOES_Product(satellite='16', sensor='SUVI', level='L1b', scan='Fe284'),
        GOES_Product(satellite='16', sensor='SUVI', level='L1b', scan='He303'),
        ]

goes_descriptions = {
    "ABI-L1b-RadF": \
            "ABI Level 1b Full Disk",
    "ABI-L1b-RadC": \
            "ABI Level 1b CONUS",
    "ABI-L1b-RadM": \
            "ABI Level 1b Mesoscale",
    "ABI-L2-ACHAC": \
            "ABI Level 2 Cloud Top Height CONUS",
    "ABI-L2-ACHAF": \
            "ABI Level 2 Cloud Top Height Full Disk",
    "ABI-L2-ACHAM": \
            "ABI Level 2 Cloud Top Height Mesoscale",
    "ABI-L2-ACHTF": \
            "ABI Level 2 Cloud Top Temperature Full Disk",
    "ABI-L2-ACHTM": \
            "ABI Level 2 Cloud Top Temperature Mesoscale",
    "ABI-L2-ACMC": \
            "ABI Level 2 Clear Sky Mask CONUS",
    "ABI-L2-ACMF": \
            "ABI Level 2 Clear Sky Mask Full Disk",
    "ABI-L2-ACMM": \
            "ABI Level 2 Clear Sky Mask Mesoscale",
    "ABI-L2-ACTPC": \
            "ABI Level 2 Cloud Top Phase CONUS",
    "ABI-L2-ACTPF": \
            "ABI Level 2 Cloud Top Phase Full Disk",
    "ABI-L2-ACTPM": \
            "ABI Level 2 Cloud Top Phase Mesoscale",
    "ABI-L2-ADPC": \
            "ABI Level 2 Aerosol Detection CONUS",
    "ABI-L2-ADPF": \
            "ABI Level 2 Aerosol Detection Full Disk",
    "ABI-L2-ADPM": \
            "ABI Level 2 Aerosol Detection Mesoscale",
    "ABI-L2-AICEF": \
            "Ice Concentration and Extent",
    "ABI-L2-AITAF": \
            "Ice Age and Thickness",
    "ABI-L2-AODC": \
            "ABI Level 2 Aerosol Optical Depth CONUS",
    "ABI-L2-AODF": \
            "ABI Level 2 Aerosol Optical Depth Full Disk",
    "ABI-L2-BRFC": \
            "Land Surface Bidirectional Reflectance Factor (CONUS) 2 km resolution & DQFs",
    "ABI-L2-BRFF": \
            "Land Surface Bidirectional Reflectance Factor (Full Disk) 2 km resolution & DQFs",
    "ABI-L2-BRFM": \
            "Land Surface Bidirectional Reflectance Factor (Mesoscale) 2 km resolution & DQFs",
    "ABI-L2-CMIPC": \
            "ABI Level 2 Cloud and Moisture Imagery CONUS",
    "ABI-L2-CMIPF": \
            "ABI Level 2 Cloud and Moisture Imagery Full Disk",
    "ABI-L2-CMIPM": \
            "ABI Level 2 Cloud and Moisture Imagery Mesoscale",
    "ABI-L2-CODC": \
            "ABI Level 2 Cloud Optical Depth CONUS",
    "ABI-L2-CODF": \
            "ABI Level 2 Cloud Optical Depth Full Disk",
    "ABI-L2-CPSC": \
            "ABI Level 2 Cloud Particle Size CONUS",
    "ABI-L2-CPSF": \
            "ABI Level 2 Cloud Particle Size Full Disk",
    "ABI-L2-CPSM": \
            "ABI Level 2 Cloud Particle Size Mesoscale",
    "ABI-L2-CTPC": \
            "ABI Level 2 Cloud Top Pressure CONUS",
    "ABI-L2-CTPF": \
            "ABI Level 2 Cloud Top Pressure Full Disk",
    "ABI-L2-DMWC": \
            "ABI Level 2 Derived Motion Winds CONUS",
    "ABI-L2-DMWF": \
            "ABI Level 2 Derived Motion Winds Full Disk",
    "ABI-L2-DMWM": \
            "ABI Level 2 Derived Motion Winds Mesoscale",
    "ABI-L2-DMWVC": \
            "L2+ Derived Motion Winds - Vapor CONUS",
    "ABI-L2-DMWVF": \
            "L2+ Derived Motion Winds - Vapor Full Disk",
    "ABI-L2-DMWVF": \
            "L2+ Derived Motion Winds - Vapor Mesoscale",
    "ABI-L2-DSIC": \
            "ABI Level 2 Derived Stability Indices CONUS",
    "ABI-L2-DSIF": \
            "ABI Level 2 Derived Stability Indices Full Disk",
    "ABI-L2-DSIM": \
            "ABI Level 2 Derived Stability Indices Mesoscale",
    "ABI-L2-DSRC": \
            "ABI Level 2 Downward Shortwave Radiation CONUS",
    "ABI-L2-DSRF": \
            "ABI Level 2 Downward Shortwave Radiation Full Disk",
    "ABI-L2-DSRM": \
            "ABI Level 2 Downward Shortwave Radiation Mesoscale",
    "ABI-L2-FDCC": \
            "ABI Level 2 Fire (Hot Spot Characterization) CONUS",
    "ABI-L2-FDCF": \
            "ABI Level 2 Fire (Hot Spot Characterization) Full Disk",
    "ABI-L2-FDCM": \
            "ABI Level 2 Fire (Hot Spot Characterization) Mesoscale",
    "ABI-L2-LSAC": \
            "Land Surface Albedo (CONUS) 2km resolution & DQFs",
    "ABI-L2-LSAF": \
            "Land Surface Albedo (Full Disk) 2km resolution & DQFs",
    "ABI-L2-LSAM": \
            "Land Surface Albedo (Mesoscale) 2km resolution & DQFs",
    "ABI-L2-LSTC": \
            "ABI Level 2 Land Surface Temperature CONUS",
    "ABI-L2-LSTF": \
            "ABI Level 2 Land Surface Temperature Full Disk",
    "ABI-L2-LSTM": \
            "ABI Level 2 Land Surface Temperature Mesoscale",
    "ABI-L2-LVMPC": \
            "ABI Level 2 Legacy Vertical Moisture Profile CONUS",
    "ABI-L2-LVMPF": \
            "ABI Level 2 Legacy Vertical Moisture Profile Full Disk",
    "ABI-L2-LVMPM": \
            "ABI Level 2 Legacy Vertical Moisture Profile Mesoscale",
    "ABI-L2-LVTPC": \
            "ABI Level 2 Legacy Vertical Temperature Profile CONUS",
    "ABI-L2-LVTPF": \
            "ABI Level 2 Legacy Vertical Temperature Profile Full Disk",
    "ABI-L2-LVTPM": \
            "ABI Level 2 Legacy Vertical Temperature Profile Mesoscale",
    "ABI-L2-MCMIPC": \
            "ABI Level 2 Cloud and Moisture Imagery CONUS",
    "ABI-L2-MCMIPF": \
            "ABI Level 2 Cloud and Moisture Imagery Full Disk",
    "ABI-L2-MCMIPM": \
            "ABI Level 2 Cloud and Moisture Imagery Mesoscale",
    "ABI-L2-RRQPEF": \
            "ABI Level 2 Rainfall Rate (Quantitative Precipitation Estimate) Full Disk",
    "ABI-L2-RSRC": \
            "ABI Level 2 Reflected Shortwave Radiation Top-Of-Atmosphere CONUS",
    "ABI-L2-RSRF": \
            "ABI Level 2 Reflected Shortwave Radiation Top-Of-Atmosphere Full Disk",
    "ABI-L2-SSTF": \
            "ABI Level 2 Sea Surface (Skin) Temperature Full Disk",
    "ABI-L2-TPWC": \
            "ABI Level 2 Total Precipitable Water CONUS",
    "ABI-L2-TPWF": \
            "ABI Level 2 Total Precipitable Water Full Disk",
    "ABI-L2-TPWM": \
            "ABI Level 2 Total Precipitable Water Mesoscale",
    "ABI-L2-VAAF": \
            "ABI Level 2 Volcanic Ash: Detection and Height Full Disk",
    "EXIS-L1b-SFEU": \
            "EXIS-Solar Flux: EUV",
    "EXIS-L1b-SFXR": \
            "EXIS-Solar Flux: X-Ray",
    "GLM-L2-LCFA": \
            "GLM Level 2 Lightning Detection",
    "MAG-L1b-GEOF": \
            "MAG-Geomagnetic Field",
    "SEIS-L1b-EHIS": \
            "SEISS-Energetic Heavy Ions",
    "SEIS-L1b-MPSH": \
            "SEISS-Mag. Electrons & Protons: Med & High Energy",
    "SEIS-L1b-MPSL": \
            "SEISS-Mag. Electrons & Protons: Low Energy",
    "SEIS-L1b-SGPS": \
            "SEISS-Solar & Galactic Protons",
    "SUVI-L1b-Fe093": \
            "SUVI Level 1b Extreme Ultraviolet",
    "SUVI-L1b-Fe131": \
            "SUVI Level 1b Extreme Ultraviolet",
    "SUVI-L1b-Fe171": \
            "SUVI Level 1b Extreme Ultraviolet",
    "SUVI-L1b-Fe195": \
            "SUVI Level 1b Extreme Ultraviolet",
    "SUVI-L1b-Fe284": \
            "SUVI Level 1b Extreme Ultraviolet",
    "SUVI-L1b-He303": \
            "SUVI Level 1b Extreme Ultraviolet",
    }
