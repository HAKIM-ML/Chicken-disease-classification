from cnnClassfier import logger
from cnnClassfier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassfier.pipeline.stage02_base_model import PrepareBaseModelTrainigPipeline
from cnnClassfier.pipeline.stage_03_train import ModelTrainingPipeline
from cnnClassfier.pipeline.stage_04_evaluation import EvaluationTrainigPipeline


STAGE_NAME  = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started >>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<< Stage {STAGE_NAME} Completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME  = "Prepare Base Model"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started >>>>>>")
    base_model = PrepareBaseModelTrainigPipeline()
    base_model.main()
    logger.info(f"<<<<<< Stage {STAGE_NAME} Completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME  = "Model Trainig"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started >>>>>>")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"<<<<<< Stage {STAGE_NAME} Completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME  = "Model Evaluation"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started >>>>>>")
    model_evaluation = EvaluationTrainigPipeline()
    model_evaluation.main()
    logger.info(f"<<<<<< Stage {STAGE_NAME} Completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

