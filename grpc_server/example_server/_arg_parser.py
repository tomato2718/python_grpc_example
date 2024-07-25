__all__ = ["arg_parser"]

import argparse

arg_parser = argparse.ArgumentParser(
    add_help=False,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

information = arg_parser.add_argument_group("Program Informations")
information.add_argument(
    "--help",
    "-h",
    action="help",
    help="Show this help message and exit.",
)

requirement = arg_parser.add_argument_group("Requirement arguments")
requirement.add_argument(
    "--host",
    action="store",
    help="The HOST to run the service.",
    type=str,
    required=True,
)
requirement.add_argument(
    "--port",
    action="store",
    help="The PORT to run the service.",
    type=int,
    required=True,
)

optional = arg_parser.add_argument_group("Optional arguments")
optional.add_argument(
    "--workers",
    action="store",
    help="The workers count of the service",
    type=int,
    default=1,
)
