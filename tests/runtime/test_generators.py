from pathlib import Path

import pytest

from aegis_runtime.generators import generate_skill, generate_skills


DEFINITION = """
name: Test Engineer
category: Engineering
path: engineering/test-engineer
role: Senior Test Engineer
mission: Make software behavior verifiable.
responsibilities: Test design, automation, reporting.
expertise: Python, pytest, quality engineering.
""".strip()


def _write_definition(path: Path, content: str = DEFINITION) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_generate_skill_creates_deterministic_asset_files(tmp_path: Path) -> None:
    definition = _write_definition(tmp_path / "generators" / "test.yaml")

    result = generate_skill(tmp_path, definition)

    assert result.name == "Test Engineer"
    assert result.output_path == tmp_path / "skills" / "engineering" / "test-engineer"
    assert [path.relative_to(result.output_path).as_posix() for path in result.files] == [
        "SKILL.md",
        "README.md",
        "expertise.md",
        "workflows.md",
        "checklists.md",
        "prompts.md",
        "examples/examples.md",
    ]
    assert "# Test Engineer" in result.files[0].read_text(encoding="utf-8")
    assert "- [ ] Requirement understood" in result.files[4].read_text(
        encoding="utf-8"
    )


def test_generate_skill_refuses_overwrite_without_force(tmp_path: Path) -> None:
    definition = _write_definition(tmp_path / "generators" / "test.yaml")
    generate_skill(tmp_path, definition)

    with pytest.raises(FileExistsError, match="--force"):
        generate_skill(tmp_path, definition)

    result = generate_skill(tmp_path, definition, force=True)
    assert result.name == "Test Engineer"


def test_generate_skill_rejects_path_escape(tmp_path: Path) -> None:
    definition = _write_definition(
        tmp_path / "generators" / "unsafe.yaml",
        DEFINITION.replace(
            "path: engineering/test-engineer",
            "path: ../outside",
        ),
    )

    with pytest.raises(ValueError, match="skills directory"):
        generate_skill(tmp_path, definition)


def test_generate_skills_uses_sorted_yaml_definitions(tmp_path: Path) -> None:
    _write_definition(tmp_path / "generators" / "b.yaml")
    _write_definition(
        tmp_path / "generators" / "a.yaml",
        DEFINITION.replace("Test Engineer", "API Engineer").replace(
            "engineering/test-engineer", "engineering/api-engineer"
        ),
    )

    results = generate_skills(tmp_path)

    assert [result.name for result in results] == ["API Engineer", "Test Engineer"]
