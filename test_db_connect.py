from sqlalchemy import create_engine

# Replace 'your_database_uri' with your actual database URI
# Example format for SQLite: 'sqlite:///example.db'
# Example format for MySQL: 'mysql://username:password@localhost/dbname'
# Example format for PostgreSQL: 'postgresql://username:password@localhost/dbname'

user_name = "webapp"
password = "Webapp123#"
db_name = "application"
port = 3306

database_uri = f'mysql+pymysql://{user_name}:{password}@127.0.0.1:{port}/{db_name}'


print(database_uri)
try:
    # Create an SQLAlchemy engine
    engine = create_engine(database_uri)

    # Try to connect to the database
    with engine.connect() as connection:
        print("Connection successful!")

except Exception as e:
    print(e)