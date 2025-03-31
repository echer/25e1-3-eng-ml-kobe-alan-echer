"""25e1-3-eng-ml-kobe-alan-echer file for ensuring the package is executable
as `25e1-3-eng-ml-kobe-alan-echer` and `python -m 25e1_3_eng_ml_kobe_alan_echer`
"""
import sys
from pathlib import Path
from typing import Any

from kedro.framework.cli.utils import find_run_command
from kedro.framework.project import configure_project


def main(*args, **kwargs) -> Any:
    package_name = Path(__file__).parent.name
    configure_project(package_name)

    interactive = hasattr(sys, 'ps1')
    kwargs["standalone_mode"] = not interactive

    run = find_run_command(package_name)
    return run(*args, **kwargs)


if __name__ == "__main__":
    main()
