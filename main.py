from MLops_project import logger
from MLops_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e