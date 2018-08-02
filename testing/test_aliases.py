import taretto
import pytest


@pytest.mark.parametrize(
    "mod",
    [taretto, taretto.navigate, taretto.ui, taretto.ui.core, taretto.ui.patternfly],
    ids=lambda mod: mod.__name__,
)
def test_aliases(mod):
    print(mod, dir(mod))
