from basic import db,Testdb


my_pussy = Testdb('indahsilvia',15)
db.session.add(my_pussy)
db.session.commit()


all_pussy = Testdb.query.all()
print(all_pussy)

# SELECT BY ID
pussy_one = Testdb.query.get(1)
print(pussy_one.name)

pussy_dwi = Testdb.query.filter_by(name='dwiagung')
print(pussy_dwi.all())

# # UPDATE TO DATABASE
first_pussy = Testdb.query.get(18)
first_pussy.age = 21
db.session.add(first_pussy)
db.session.commit()

second_pussy = Testdb.query.get(9)
db.session.delete(second_pussy)
db.session.commit()

# PRINT ALL DATABASE
all_pussy = Testdb.query.all()
print(all_pussy)
