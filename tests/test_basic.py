"""Test basic qfinbox functionality."""

import qfinbox


def test_version() -> None:
    """Test that version is accessible."""
    assert hasattr(qfinbox, "__version__")
    assert isinstance(qfinbox.__version__, str)
    assert qfinbox.__version__ == "0.1.0"


def test_author() -> None:
    """Test that author information is accessible."""
    assert hasattr(qfinbox, "__author__")
    assert qfinbox.__author__ == "prashant-fintech"


def test_email() -> None:
    """Test that email information is accessible."""
    assert hasattr(qfinbox, "__email__")
    assert qfinbox.__email__ == "box_prashant@outlook.com"


def test_import() -> None:
    """Test that qfinbox can be imported without errors."""
    import qfinbox

    assert qfinbox is not None
