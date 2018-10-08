import inspect
import taretto
import pytest


@pytest.mark.parametrize(
    "mod",
    [taretto.navigate, taretto.ui, taretto.ui.core, taretto.ui.patternfly, taretto.ui.patternfly4],
    ids=lambda mod: mod.__name__,
)
def test_module_aliases(mod):
    print(mod, dir(mod))


@pytest.mark.parametrize(
    "mod, classname",
    [
        (taretto.ui, "View"),
        (taretto.ui, "Browser"),
        (taretto.ui, "DefaultPlugin"),
        (taretto.ui.patternfly, "VerticalNavigation"),
        (taretto.ui.patternfly4, "Navigation"),
    ],
    ids=lambda mod: mod.__name__,
)
def test_aliased_classes(mod, classname):
    klass = getattr(mod, classname)
    assert inspect.isclass(klass)
