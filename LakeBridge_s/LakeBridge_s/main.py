# from service.helper import get_inputs
from service.config_service import collect_user_config
from service.config_service import create_transpiler_model
from service.analyzer_service import run_analyzer
from service.transpile_service import run_transpiler


def main():
    config1 = collect_user_config()
    # config = get_inputs()
    run_analyzer(config1["analyzer"])
    
    config2 = create_transpiler_model()
    
    run_transpiler(config2)
    
    #config3 = create_reconciler_model()
   # run_reconciler(config3.reconciler)
    #print(config.transpiler)
    #print(config.reconciler)
    
if __name__ == "__main__":
    main()
