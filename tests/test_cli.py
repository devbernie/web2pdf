"""
CLI command tests
"""

from typing import Optional
import pytest
from click.testing import CliRunner
from web2pdf.cli import main

@pytest.fixture
def runner():
    return CliRunner()

def test_basic_conversion(runner, tmp_path):
    output_file = tmp_path / "output.pdf"
    result = runner.invoke(main, [
        "https://example.com",
        str(output_file),
        "--verbose"
    ])
    
    assert result.exit_code == 0
    assert output_file.exists()

def test_invalid_url(runner, tmp_path):
    output_file = tmp_path / "output.pdf"
    result = runner.invoke(main, [
        "invalid_url",
        str(output_file)
    ])
    
    assert result.exit_code != 0
    assert "Invalid URL format" in result.output

def test_auth_credentials(runner, tmp_path):
    output_file = tmp_path / "output.pdf"
    result = runner.invoke(main, [
        "https://httpbin.org/basic-auth/user/pass",
        str(output_file),
        "--auth-user", "user",
        "--auth-pass", "pass"
    ])
    
    assert result.exit_code == 0
    assert output_file.exists()