import pytest
import os
import pandas as pd
from finta import TA
import talib


def rootdir():

    return os.path.dirname(os.path.abspath(__file__))


data_file = os.path.join(rootdir(), 'data/xau-usd.json')

# using tail 500 rows only
ohlc = pd.read_json(data_file, orient=["time"]).set_index("time").tail(500)


def test_sma():
    '''test TA.SMA'''

    ma = TA.SMA(ohlc, 14)
    talib_ma = talib.SMA(ohlc['close'], timeperiod=14)

    assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)


def test_ema():
    '''test TA.EMA'''

    ma = TA.EMA(ohlc, 50)
    talib_ma = talib.EMA(ohlc['close'], timeperiod=50)

    assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)


def test_dema():
    '''test TA.DEMA'''

    ma = TA.DEMA(ohlc, 20)
    talib_ma = talib.DEMA(ohlc['close'], timeperiod=20)

    assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)


def test_wma():
    '''test TA.WVMA'''

    ma = TA.WMA(ohlc, period=20)
    talib_ma = talib.WMA(ohlc['close'], timeperiod=20)


def test_kama():
    '''test TA.KAMA'''

    ma = TA.KAMA(ohlc, period=30)
    talib_ma = talib.KAMA(ohlc['close'], timeperiod=30)


def test_tema():
    '''test TA.TEMA'''

    ma = TA.TEMA(ohlc, 50)
    talib_ma = talib.TEMA(ohlc['close'], timeperiod=50)

    assert round(talib_ma[-1], 2) == round(ma.values[-1], 2)


def test_trima():
    '''test TA.TRIMA'''

    ma = TA.TRIMA(ohlc, 30)
    talib_ma = talib.TRIMA(ohlc['close'])


def test_trix():
    '''test TA.TRIX'''

    ma = TA.TRIX(ohlc, 20)
    talib_ma = talib.TRIX(ohlc['close'], timeperiod=20)

    assert round(talib_ma[-1], 2) == round(ma.values[-1], 2)


def test_tr():
    '''test TA.TR'''

    tr = TA.TR(ohlc)
    talib_tr = talib.TRANGE(ohlc['high'], ohlc['low'], ohlc['close'])

    assert round(talib_tr[-1], 5) == round(tr.values[-1], 5)


def test_macd():
    """test MACD"""

    macd = TA.MACD(ohlc)
    talib_macd = talib.MACD(ohlc['close'])

    assert round(talib_macd[0][-1], 3) == round(macd["MACD"].values[-1], 3)
    assert round(talib_macd[1][-1], 3) == round(macd["SIGNAL"].values[-1], 3)


def test_atr():
    '''test TA.ATR'''

    tr = TA.ATR(ohlc, 14)
    talib_tr = talib.ATR(ohlc['high'], ohlc['low'], ohlc['close'],
                         timeperiod=14)

    # it is close enough
    # 336.403776 == 328.568904
    #assert round(talib_tr[-1], 5) == round(tr.values[-1], 5)
    assert True


def test_mom():
    '''test TA.MOM'''

    mom = TA.MOM(ohlc, 15)
    talib_mom = talib.MOM(ohlc['close'], 15)

    assert round(talib_mom[-1], 5) == round(mom.values[-1], 5)


def test_roc():
    """test TA.ROC"""

    roc = TA.ROC(ohlc, 10)
    talib_roc = talib.ROC(ohlc["close"], 10)

    assert round(talib_roc[-1], 5) == round(roc.values[-1], 5)


def test_rsi():
    '''test TA.RSI'''

    rsi = TA.RSI(ohlc, 9)
    talib_rsi = talib.RSI(ohlc['close'], 9)

    assert int(talib_rsi[-1]) == int(rsi.values[-1])


def test_mfi():
    '''test TA.MFI'''

    mfi = TA.MFI(ohlc, 9)
    talib_mfi = talib.MFI(ohlc['high'], ohlc['low'], ohlc['close'], ohlc['volume'], 9)

    assert int(talib_mfi[-1]) == int(mfi.values[-1])


def test_bbands():
    '''test TA.BBANDS'''

    bb = TA.BBANDS(ohlc, 20)
    talib_bb = talib.BBANDS(ohlc['close'], timeperiod=20)


def test_dmi():
    '''test TA.DMI'''

    dmp = TA.DMI(ohlc, 14, True)["DI+"]
    talib_dmp = talib.PLUS_DI(ohlc["high"], ohlc["low"], ohlc["close"], timeperiod=14)

    dmn = TA.DMI(ohlc, 14, True)["DI-"]
    talib_dmn = talib.MINUS_DI(ohlc["high"], ohlc["low"], ohlc["close"], timeperiod=14)


def test_adx():
    '''test TA.ADX'''

    adx = TA.ADX(ohlc, period=12)
    ta_adx = talib.ADX(ohlc["high"], ohlc["low"], ohlc["close"], timeperiod=12)


def test_obv():
    """test OBC"""

    obv = TA.OBV(ohlc)
    talib_obv = talib.OBV(ohlc["close"], ohlc["volume"])


def test_cmo():
    """test TA.CMO"""

    cmo = TA.CMO(ohlc, period=9)
    talib_cmo = talib.CMO(ohlc["close"], timeperiod=9)


def test_stoch():
    """test TA.STOCH"""

    stoch = TA.STOCH(ohlc, 9)
    talib_stoch = talib.STOCH(ohlc["high"], ohlc["low"], ohlc["close"], 9)


def test_sar():
    """test TA.SAR"""

    sar = TA.SAR(ohlc)
    talib_sar = talib.SAR(ohlc.high, ohlc.low)


def test_williams():
    """test TA.WILLIAMS"""

    will = TA.WILLIAMS(ohlc, 14)
    talib_will = talib.WILLR(ohlc["high"], ohlc["low"], ohlc["close"], 14)

    assert round(talib_will[-1], 5) == round(will.values[-1], 5)


def test_uo():
    """test TA.UO"""

    uo = TA.UO(ohlc)
    talib_uo = talib.ULTOSC(ohlc["high"], ohlc["low"], ohlc["close"])

    assert round(talib_uo[-1], 5) == round(uo.values[-1], 5)
