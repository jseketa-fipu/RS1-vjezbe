# tests/test_vjezba_02.py
import builtins

import pytest

import vjezba_02 as vjezba_02


def _feed_inputs(monkeypatch, inputs, record_prompts=False):
    """Monkeypatch builtins.input to return values from `inputs`."""
    it = iter(inputs)
    prompts = []

    def fake_input(prompt=""):
        if record_prompts:
            prompts.append(prompt)
        try:
            return next(it)
        except StopIteration:
            # Make failures obvious if the function requested more inputs than provided
            raise AssertionError("Function asked for more inputs than provided.")

    monkeypatch.setattr(builtins, "input", fake_input)
    return prompts


def test_input_positive_year_accepts_valid_first_try(monkeypatch):
    _feed_inputs(monkeypatch, ["2024"])
    result = vjezba_02.input_positive_year()
    assert result == 2024


def test_input_positive_year_rejects_non_digits_then_accepts(monkeypatch, capsys):
    _feed_inputs(monkeypatch, ["abcd", "1999"])
    result = vjezba_02.input_positive_year()
    captured = capsys.readouterr().out
    assert "Please enter digits only" in captured
    assert result == 1999


def test_input_positive_year_rejects_zero_and_negative_then_accepts(
    monkeypatch, capsys
):
    _feed_inputs(monkeypatch, ["0", "-5", "1"])
    result = vjezba_02.input_positive_year()
    captured = capsys.readouterr().out
    assert "Please enter a positive year" in captured
    assert result == 1


def test_input_positive_year_strips_whitespace(monkeypatch):
    _feed_inputs(monkeypatch, ["   2001   "])
    assert vjezba_02.input_positive_year() == 2001


def test_input_positive_year_uses_custom_prompt(monkeypatch):
    prompts = _feed_inputs(monkeypatch, ["7"], record_prompts=True)
    assert vjezba_02.input_positive_year(prompt="Gimme: ") == 7
    # Ensure our custom prompt was actually used
    assert prompts and prompts[0] == "Gimme: "


@pytest.mark.parametrize(
    "year,is_leap",
    [
        (1996, True),  # divisible by 4, not by 100
        (1900, False),  # divisible by 100, not by 400
        (2000, True),  # divisible by 400
        (2023, False),  # normal non-leap
        (2024, True),  # divisible by 4, not by 100
    ],
)
def test_main_prints_expected_leapness(monkeypatch, capsys, year, is_leap):
    # Feed the year to main() via input
    _feed_inputs(monkeypatch, [str(year)])
    vjezba_02.main()
    out = capsys.readouterr().out

    # First line from main should echo the year
    assert f"Year: {year}" in out

    if is_leap:
        assert f"Godina {year}. je prijestupna." in out
    else:
        assert f"Godine {year}. nije prijestupna." in out
