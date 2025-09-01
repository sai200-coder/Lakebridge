from service.helper import (
    get_source_directory, get_report_file, get_source_tech,
    get_input_source, get_output_folder, get_error_file_path,
    get_catalog_name, get_schema_name, get_source_dialect,
    get_profile_name, get_target,get_validate, get_warehouse, get_override,
    get_open_config
)

from models.analyzer_model import AnalyzerModel
from models.transpile_model import TranspilerModel
from models.reconcile_model import ReconcilerModel
from models.full_config import FullConfigModel


def collect_user_config() -> FullConfigModel:
    analyzer = AnalyzerModel(
        source_directory=get_source_directory(),
        report_file=get_report_file(),
        source_tech=get_source_tech()
    )
    return {"analyzer": analyzer}
    
def create_transpiler_model() ->  FullConfigModel:
    catalog = get_catalog_name()
    return TranspilerModel(
        source_dialect=get_source_dialect(),
        input_source=get_input_source(),
        output_folder=get_output_folder(),
        error_file_path=get_error_file_path(),
        catalog_name=catalog,
        schema_name=get_schema_name(catalog),
        validate=get_validate(),
        warehouse=get_warehouse(),
        override=get_override(),
        open_config=get_open_config()
        )
    
    reconciler = ReconcilerModel(
        profile_name=get_profile_name(),
        target=get_target()
    )

    return FullConfigModel(
        analyzer=analyzer,
        transpiler=transpiler,
        reconciler=reconciler
    )
