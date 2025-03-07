from importlib.resources import files
import os
from pynwb import load_namespaces, get_class

# Get path to the namespace.yaml file with the expected location when installed not in editable mode
__location_of_this_file = files(__name__)
__spec_path = __location_of_this_file / "spec" / "ndx-ibl-bwm.namespace.yaml"

# If that path does not exist, we are likely running in editable mode. Use the local path instead
if not os.path.exists(__spec_path):
    __spec_path = __location_of_this_file.parent.parent.parent / "spec" / "ndx-ibl-bwm.namespace.yaml"

# Load the namespace
load_namespaces(str(__spec_path))

ibl_bwm_metadata = get_class("ibl_bwm_metadata", "ndx-ibl-bwm")

__all__ = [
    "ibl_bwm_metadata",
]

# Remove these functions/modules from the package
del load_namespaces, get_class, files, os, __location_of_this_file, __spec_path
