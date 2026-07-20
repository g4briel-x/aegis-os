import pytest

from aegis_skills.frontmatter import FrontmatterError, parse_frontmatter_text


def test_parse_valid_frontmatter() -> None:
    text = "---\nname: demo\ndescription: test\n---\n# Demo\n"
    metadata, body = parse_frontmatter_text(text)
    assert metadata["name"] == "demo"
    assert body.startswith("# Demo")


def test_reject_missing_frontmatter() -> None:
    with pytest.raises(FrontmatterError):
        parse_frontmatter_text("# Demo\n")
