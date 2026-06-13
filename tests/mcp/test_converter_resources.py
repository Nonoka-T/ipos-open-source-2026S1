from app.mcp.mcp_resources.converter_resources import (
    RESOURCE_DEFINITIONS,
    unit_reference,
)


def test_unit_reference_returns_dict():
    """Verify that unit_reference returns a dictionary."""
    result = unit_reference()
    assert isinstance(result, dict)


def test_unit_reference_has_required_keys():
    """Verify that the result contains expected keys."""
    result = unit_reference()
    assert "id" in result
    assert "title" in result
    assert "supported" in result


def test_unit_reference_distance_conversion():
    """Verify that distance conversion data is present."""
    result = unit_reference()
    distance = result["supported"]["distance"]
    assert "miles_to_kilometers" in distance


def test_resource_definitions_structure():
    """Verify that RESOURCE_DEFINITIONS is correctly structured."""
    assert len(RESOURCE_DEFINITIONS) == 1
    resource = RESOURCE_DEFINITIONS[0]
    assert resource["name"] == "unit_reference"
    assert callable(resource["func"])