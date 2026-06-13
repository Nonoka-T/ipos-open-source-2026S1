import time
import pytest
from app.mcp.mcp_tools.miles_to_km import (
    TOOL_DEFINITION,
    MilestoKmRequest,
    MilestoKmResponse,
    miles_to_kilometers_value,
)

# Issue #9: Add test coverage for converter tools module
#Target: miles_to_km.py currently has 0% coverage


def test_miles_to_kilometers_basic():
    """Verify that 1 mile converts to approximately 1.609 kilometers."""
    result = miles_to_kilometers_value(1.0)
    assert round(result, 3) == 1.609


def test_miles_to_kilometers_large_value():
    """Verify conversion is accurate for larger distances."""
    result = miles_to_kilometers_value(100.0)
    assert round(result, 1) == 160.9


def test_miles_to_kilometers_zero_raises():
    """Verify that zero input raises an exception as per validation rules."""
    with pytest.raises(Exception):
        miles_to_kilometers_value(0.0)


def test_miles_to_kilometers_negative_raises():
    """Verify that negative input raises an exception."""
    with pytest.raises(Exception):
        miles_to_kilometers_value(-1.0)


def test_miles_to_kilometers_too_large_raises():
    """Verify that unrealistically large values are rejected."""
    with pytest.raises(Exception):
        miles_to_kilometers_value(999999.0)


def test_request_model_valid():
    """Verify that MilestoKmRequest accepts valid input."""
    req = MilestoKmRequest(miles=5.0)
    assert req.miles == 5.0


def test_response_model_fields():
    """Verify that MilestoKmResponse contains expected fields."""
    resp = MilestoKmResponse(
        result=8.0,
        operation="miles_to_kilometers",
        audited_at=time.time(),
    )
    assert resp.operation == "miles_to_kilometers"
    assert resp.result > 0


def test_tool_definition_structure():
    """Verify that TOOL_DEFINITION is correctly structured for MCP registration."""
    assert len(TOOL_DEFINITION) == 1
    tool = TOOL_DEFINITION[0]
    assert tool["name"] == "miles_to_kilometers"
    assert callable(tool["func"])