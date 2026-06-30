from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)

Base = declarative_base()




class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    first_name = Column(String(30))
    last_name = Column(String(30), nullable=True)
    age = Column(Integer)
    national_id = Column(String)

    def __repr__(self):
        return f"User(id = {self.id}, firstname = {self.first_name}, lastname = {self.last_name})"
    
Base.metadata.create_all(engine)


session = SessionLocal()


#inserting to DB
#ali = User(first_name = "Ali", age = 31)
#session.add(ali)
#session.commit()


#inserting multiuser in User table
#maryam = User(first_name = "maryam", age = 27)
#anousha = User(first_name = "anousha", age = 6)
#users = [maryam, anousha]
#session.add_all(users)
#session.commit()

#retrieve_all_data
#users = session.query(User).all()
#print(users)

#retrieve_Data_With_Filter
user = session.query(User).filter_by(first_name = "maryam").first()
#print(user)

#updating a record of data
#user.last_name="bigdeli"
#session.commit()

#delete sth
session.delete(user)
session.commit()

# all users
users_all = session.query(User).all()

# query all users with age greater than or equal to 25
users_filtered = session.query(User).filter(User.age >=25).all()

print("ALL Users: ", len(users_all))
print("Filtered Users: ", len(users_filtered ))

# add multiple filters
# query all users with age greater than or equal to 25 and name equals to something
users_filtered = session.query(User).filter(User.age >=25,User.name == "ali").all()

# or you can use where
users_filtered = session.query(User).where(User.age >=25,User.name == "ali").all()

# users with similar name contianing specific substrings
users_similar_name = session.query(User).filter(User.name.like("%ali%")).all()

# users with case insensitive match
users_similar_name = session.query(User).filter(User.name.ilike("%ali%")).all()

# users with starting and ending chars
users_starting_ali = session.query(User).filter(User.name.like("Ali%")).all()
users_ending_ali = session.query(User).filter(User.name.like("%Ali")).all()



from sqlalchemy import or_ ,and_, not_

Session = sessionmaker(bind=engine)
serssion= Session()


# query those who has ali as name or age above 25
#users_filtered = session.query(User).filter(or_(User.age >=25,User.name == "ali")).all()

# query those who has ali as name and age above 25
#users_filtered = session.query(User).filter(and_(User.age >=25,User.name == "ali")).all()

# query those whos name is not ali
#users_filtered = session.query(User).filter(not_(User.name == "ali")).all()

# getting users which are note named ali or age between 35,60
#users = session.query(User).filter(or_(not_(User.name == "ali"),and_(User.age >35,User.age<60)))


