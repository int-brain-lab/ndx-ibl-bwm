# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec

# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        name="""ndx-ibl-bwm""",
        version="""0.1.0""",
        doc="""extending NWB with IBL specific metadata for the brainwide map dataset""",
        author=[
            "Georg Raiser",
        ],
        contact=[
            "georg.raiser@internationalbrainlab.org",
        ],
    )
    ns_builder.include_namespace("core")
    ns_builder.include_type("LabMetaData", namespace="core")

    ibl_bwm_ext = NWBGroupSpec(
        name="ibl_bwm_metadata",
        doc="Extension with IBL specific metadata for the brainwide map dataset",
        neurodata_type_def="ibl_bwm_metadata",
        neurodata_type_inc="LabMetaData",
    )
    ibl_bwm_ext.add_dataset(
        name="revision",
        doc="data revision, specified as a date",
        dtype="text",
        quantity="?",
    )

    new_data_types = [ibl_bwm_ext]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "spec"))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
