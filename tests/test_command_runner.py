from bulk_issue_importer.core.command_runner import CommandRunner


def test_command_runner():

    result = CommandRunner.run(
        ["python", "--version"]
    )

    assert result.return_code == 0
    assert "Python" in result.stdout