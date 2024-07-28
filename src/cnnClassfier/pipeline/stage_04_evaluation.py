from cnnClassfier.config.configuration import ConfigurationManager
from cnnClassfier.components.evaluation import Evaluation
from cnnClassfier import logger


STAGE_NAME = 'Evaluation Stage'

class EvaluationTrainigPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        
        
        
        
if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> Stage {STAGE_NAME} Started <<<<<<<')
        obj = EvaluationTrainigPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e