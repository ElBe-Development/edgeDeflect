import argparse

parser = argparse.ArgumentParser(description='Beschreibung des Skripts')
parser.add_argument('--option1', help='Beschreibung der Option 1')
parser.add_argument('--option2', help='Beschreibung der Option 2')
args = parser.parse_args()

if args.option1:
    # Führen Sie Aktionen für Option 1 aus
    pass

if args.option2:
    # Führen Sie Aktionen für Option 2 aus
    pass