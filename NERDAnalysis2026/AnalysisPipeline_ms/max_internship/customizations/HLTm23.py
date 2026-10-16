"""HLTm23: same menu and conditions as HLT, with the scouting track packer
storing floats at full float32 precision (23 mantissa bits, i.e. no truncation).

Appended to Jobs_HLTm23/run_cfg.py by 02_submit.py, which then calls customise().
"""


def customise(process):
    process.hltScoutingTrackPacker.mantissaPrecision = 23
    return process
