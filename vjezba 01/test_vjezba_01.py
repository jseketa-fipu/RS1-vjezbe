# tests/test_vjezba_01.py
import builtins
import pytest

import vjezba_01


class InputFeeder:
    """
    Feeds a fixed sequence to input(). If the code asks for more,
    fail the test instead of hanging in an infinite loop.
    """

    def __init__(self, responses):
        self._iter = iter(responses)

    def __call__(self, prompt: str = "") -> str:
        try:
            return next(self._iter)
        except StopIteration:
            pytest.fail(f"Ran out of test inputs while waiting at prompt: {prompt!r}")


def test_check_input_for_float_valid(monkeypatch):
    monkeypatch.setattr(builtins, "input", InputFeeder(["3.14"]))
    assert vjezba_01.check_input_for_float("x") == 3.14


def test_check_input_for_float_retry_then_ok(monkeypatch, capsys):
    # invalid -> prints error -> valid
    monkeypatch.setattr(builtins, "input", InputFeeder(["abc", "2,5"]))
    val = vjezba_01.check_input_for_float("x")
    assert val == 2.5
    out = capsys.readouterr().out
    assert "Neispravan unos broja" in out


def test_check_if_operator_supported_valid(monkeypatch):
    monkeypatch.setattr(builtins, "input", InputFeeder(["+"]))
    assert vjezba_01.check_if_operator_supported("op: ") == "+"


def test_check_if_operator_supported_retry_then_ok(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", InputFeeder(["x", "/"]))
    op = vjezba_01.check_if_operator_supported("op: ")
    assert op == "/"
    out = capsys.readouterr().out
    assert "Nepodržani operator" in out


def test_check_for_division_by_zero_exits():
    with pytest.raises(SystemExit) as e:
        vjezba_01.check_for_division_by_zero(0.0, "/")
    assert e.value.code == 0  # matches your implementation


@pytest.mark.parametrize(
    "a, op, b, expected",
    [
        (5.0, "+", 3.0, 8.0),
        (5.0, "-", 3.0, 2.0),
        (5.0, "*", 3.0, 15.0),
        (6.0, "/", 3.0, 2.0),
    ],
)
def test_supported_operations(a, op, b, expected):
    func = vjezba_01.supported_operators[op]
    assert func(a, b) == expected


def test_end_to_end_ok(monkeypatch, capsys):
    # a=5, b=3, op=+
    monkeypatch.setattr(builtins, "input", InputFeeder(["5", "3", "+"]))
    vjezba_01.main()
    out = capsys.readouterr().out
    assert "Rezultat operacije 5.0 + 3.0 je 8.0" in out


def test_end_to_end_division_by_zero(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", InputFeeder(["5", "0", "/"]))
    with pytest.raises(SystemExit) as e:
        vjezba_01.main()
    assert e.value.code == 0
    out = capsys.readouterr().out
    assert "Dijeljenje s nulom nije dozvoljeno!" in out
