from bulk_issue_importer.application import Application


def main() -> None:
    """
    Application entry point.
    """
    application = Application()
    application.run()


if __name__ == "__main__":
    main()