import requests
import ckan_api as api_utils
import utils as utils
import logging
import inspect
from cli_arguments import get_arguments


def main():
    utils.log_config()
    logging.info(f"[INFO] Program start | Current Function: {inspect.currentframe().f_code.co_name}")

    try:
        args = get_arguments()
        api_utils.api_attributes.ENDPOINT_PACKAGE_SEARCH['PARAMETERS_PACKAGE_SEARCH']['q'] = args.search_term
        
        api_response = requests.get(url = api_utils.api_attributes.ENDPOINT_PACKAGE_SEARCH['URL'], params = api_utils.api_attributes.ENDPOINT_PACKAGE_SEARCH['PARAMETERS_PACKAGE_SEARCH'])
        api_response.raise_for_status()

        logging.info(f"[INFO] API Request Successful | API status Code: {api_response.status_code}")

        results = api_utils.api_functions.get_datasets_title(data=api_response.json(), key='title')
        print(results)

        logging.info(f"[INFO] Program Ended | Current Function: {inspect.currentframe().f_code.co_name}")   

    except requests.exceptions.HTTPError as e:
        logging.exception(f"[Exception] API HTTP Exception | Exception msg: {e}")
    except requests.exceptions.ConnectionError as e:
        logging.exception(f"[Exception] API Connection Exception | Exception msg: {e}")
    except requests.exceptions.RequestException as e:
        logging.exception(f"[Exception] API Request Exception | Exception msg: {e}")
    except Exception as e:
        logging.exception(f"[Exception] Unknown Exception | Exception msg: {e}")



if __name__ == "__main__":
    main()