from CnnClassifier import logger
from CnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CnnClassifier.pipeline.stage03_model_trainer import ModelTrainingPipeline
from CnnClassifier.pipeline.stage04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"

try:
    logger.info(f"*****************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f"*****************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"

try:
    logger.info(f"*****************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e