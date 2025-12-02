from models import Dog

# Create the table using the Base and engine
def create_table(Base, engine):
    Base.metadata.create_all(engine)

# Save a Dog instance to the database
def save(session, dog):
    session.add(dog)
    session.commit()
    return dog

# Create a new Dog and save it
def create(session, name, breed):
    dog = Dog(name=name, breed=breed)
    return save(session, dog)

# Get all Dog instances
def get_all(session):
    return session.query(Dog).all()

# Find a dog by name
def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

# Find a dog by id
def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

# Find a dog by name and breed
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

# Find or create a dog by name and breed
def find_or_create_by(session, name, breed):
    dog = find_by_name_and_breed(session, name, breed)
    if dog is None:
        dog = create(session, name, breed)
    return dog

# Update a dog's breed
def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()
    return dog
