import time

from yaml_reader import YamlPipelineExecutor


def main():
    pipeline_location = 'pipelines/wiki_yahoo_scraper_pipeline.yaml'
    scraper_start_time = time.time()

    yamlPipelineExecutor = YamlPipelineExecutor(pipeline_location=pipeline_location)
    # yamlPipelineExecutor.process_pipeline()
    yamlPipelineExecutor.start()
    print('Extracting time took:', round(time.time() - scraper_start_time, 1))


if __name__ == "__main__":
    main()
