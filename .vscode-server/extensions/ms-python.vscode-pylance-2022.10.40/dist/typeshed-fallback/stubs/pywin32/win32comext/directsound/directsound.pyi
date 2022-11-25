from _typeshed import Incomplete

import _win32typing
from pywintypes import IID as IID

def DirectSoundCreate(guid: _win32typing.PyIID | None = ..., unk: Incomplete | None = ...) -> _win32typing.PyIUnknown: ...
def DirectSoundEnumerate(): ...
def DirectSoundCaptureCreate(guid: _win32typing.PyIID | None = ..., unk: Incomplete | None = ...) -> _win32typing.PyIUnknown: ...
def DirectSoundCaptureEnumerate(): ...
def DSCAPS() -> _win32typing.PyDSCAPS: ...
def DSBCAPS() -> _win32typing.PyDSBCAPS: ...
def DSCCAPS() -> _win32typing.PyDSCCAPS: ...
def DSCBCAPS() -> _win32typing.PyDSCBCAPS: ...
def DSBUFFERDESC() -> _win32typing.PyDSBUFFERDESC: ...
def DSCBUFFERDESC() -> _win32typing.PyDSCBUFFERDESC: ...

DS3DMODE_DISABLE: int
DS3DMODE_HEADRELATIVE: int
DS3DMODE_NORMAL: int
DSBCAPS_CTRL3D: int
DSBCAPS_CTRLFREQUENCY: int
DSBCAPS_CTRLPAN: int
DSBCAPS_CTRLPOSITIONNOTIFY: int
DSBCAPS_CTRLVOLUME: int
DSBCAPS_GETCURRENTPOSITION2: int
DSBCAPS_GLOBALFOCUS: int
DSBCAPS_LOCHARDWARE: int
DSBCAPS_LOCSOFTWARE: int
DSBCAPS_MUTE3DATMAXDISTANCE: int
DSBCAPS_PRIMARYBUFFER: int
DSBCAPS_STATIC: int
DSBCAPS_STICKYFOCUS: int
DSBLOCK_ENTIREBUFFER: int
DSBLOCK_FROMWRITECURSOR: int
DSBPLAY_LOOPING: int
DSBSTATUS_BUFFERLOST: int
DSBSTATUS_LOOPING: int
DSBSTATUS_PLAYING: int
DSCAPS_CERTIFIED: int
DSCAPS_CONTINUOUSRATE: int
DSCAPS_EMULDRIVER: int
DSCAPS_PRIMARY16BIT: int
DSCAPS_PRIMARY8BIT: int
DSCAPS_PRIMARYMONO: int
DSCAPS_PRIMARYSTEREO: int
DSCAPS_SECONDARY16BIT: int
DSCAPS_SECONDARY8BIT: int
DSCAPS_SECONDARYMONO: int
DSCAPS_SECONDARYSTEREO: int
DSCBCAPS_WAVEMAPPED: int
DSCCAPS_EMULDRIVER: int
DSSCL_EXCLUSIVE: int
DSSCL_NORMAL: int
DSSCL_PRIORITY: int
DSSCL_WRITEPRIMARY: int
DSSPEAKER_GEOMETRY_MAX: int
DSSPEAKER_GEOMETRY_MIN: int
DSSPEAKER_GEOMETRY_NARROW: int
DSSPEAKER_GEOMETRY_WIDE: int
DSSPEAKER_HEADPHONE: int
DSSPEAKER_MONO: int
DSSPEAKER_QUAD: int
DSSPEAKER_STEREO: int
DSSPEAKER_SURROUND: int
DSBCAPSType = _win32typing.PyDSBCAPS
DSBFREQUENCY_MAX: int
DSBFREQUENCY_MIN: int
DSBFREQUENCY_ORIGINAL: int
DSBPAN_CENTER: int
DSBPAN_LEFT: int
DSBPAN_RIGHT: int
DSBPN_OFFSETSTOP: int
DSBSIZE_MAX: int
DSBSIZE_MIN: int
DSBUFFERDESCType = _win32typing.PyDSBUFFERDESC
DSBVOLUME_MAX: int
DSBVOLUME_MIN: int
DSCAPSType = _win32typing.PyDSCAPSType
DSCBCAPSType = _win32typing.PyDSCBCAPSType
DSCBLOCK_ENTIREBUFFER: int
DSCBSTART_LOOPING: int
DSCBSTATUS_CAPTURING: int
DSCBSTATUS_LOOPING: int
DSCBUFFERDESCType = _win32typing.PyDSCBUFFERDESC
DSCCAPSType = _win32typing.PyDSCCAPSType
DSERR_ACCESSDENIED: int
DSERR_ALLOCATED: int
DSERR_ALREADYINITIALIZED: int
DSERR_BADFORMAT: int
DSERR_BADSENDBUFFERGUID: int
DSERR_BUFFERLOST: int
DSERR_BUFFERTOOSMALL: int
DSERR_CONTROLUNAVAIL: int
DSERR_DS8_REQUIRED: int
DSERR_FXUNAVAILABLE: int
DSERR_GENERIC: int
DSERR_INVALIDCALL: int
DSERR_INVALIDPARAM: int
DSERR_NOAGGREGATION: int
DSERR_NODRIVER: int
DSERR_NOINTERFACE: int
DSERR_OBJECTNOTFOUND: int
DSERR_OTHERAPPHASPRIO: int
DSERR_OUTOFMEMORY: int
DSERR_PRIOLEVELNEEDED: int
DSERR_SENDLOOP: int
DSERR_UNINITIALIZED: int
DSERR_UNSUPPORTED: int
DS_NO_VIRTUALIZATION: int
DS_OK: int
IID_IDirectSound: _win32typing.PyIID
IID_IDirectSoundBuffer: _win32typing.PyIID
IID_IDirectSoundCapture: _win32typing.PyIID
IID_IDirectSoundCaptureBuffer: _win32typing.PyIID
IID_IDirectSoundNotify: _win32typing.PyIID
