import argparse
from functools import partial
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from models import first_model

# help_msg = "type function name. "+ os.linesep +\
#     "there is two possible options:"
#     -fn add_obj - will run a add_obj() function that will add record in the db,\n\
#     -fn get_obj - will run a get_obj() function thath will return record from db.\n\
#     -fn initdb - will run a initdb() function that will create db and table\n"


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-initdb', help='will run a initdb() function that will create db and table', action='store_true')
parser.add_argument('-add_obj', help='will run a add_obj() function that will add record in the db', action='store_true')
parser.add_argument('-get_obj', help='will run a get_obj() function thath will return record from db', action='store_true')
args = parser.parse_args()

engine = create_engine('sqlite:///sqldb.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def initdb():
    first_model.Base.metadata.create_all(engine)

    

def add_obj():
    try:
        with session as s:
            obj = first_model.First(first_name='John', second_name='Doe')
            s.add(obj)
            s.commit()
    except NameError:
        initdb()
        
    return 1

def get_obj():
    with session as s:
        try:
            obj = s.query(first_model.First)
            print('obj print => {}'.format(obj[0].full_name()))
        except AttributeError:
            print('obj print => {}'.format(obj[0].first_name))
        except IndexError:
            print('>>>>>WARNING: There is no records')
        except OperationalError:
            print('>>>>>WARNING: There is no tables yet. Please run python main.py -fn initdb')
    
def run_by_args():
    if not args.add_obj or not args.get_obj or not args.initdb:
        print('there is no args passed')
    if args.add_obj:
        add_obj()
    elif args.get_obj:
        get_obj()
    elif args.initdb:
        initdb()

if __name__ == '__main__':
    run_by_args()