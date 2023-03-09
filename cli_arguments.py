import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description='My script description')
    parser.add_argument('--search_term', type=str, 
                        help='Please provide a search term for ckan API package searching!', required=True)

    args = parser.parse_args()
    return args