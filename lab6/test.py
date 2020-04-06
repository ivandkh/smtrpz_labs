from subprocess import getstatusoutput


def test_trivial():
    cmd = 'python lab6.py \"A\" \"hello\" '
    _, out = getstatusoutput(cmd)
    assert out == 'hello'


def test_dec():
    cmd = 'python lab6.py \"h\" \"hello\" '
    _, enc_out = getstatusoutput(cmd)

    cmd = 'python lab6.py \"h\" \"%s\" --dec' % enc_out
    _, dec = getstatusoutput(cmd)

    assert dec == 'hello'


def test_key_error():
    cmd = 'python lab6.py \"hello\" '
    exitcode, _ = getstatusoutput(cmd)
    assert exitcode > 0
