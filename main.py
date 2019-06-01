from database import session
from flask import abort, flash, Flask, render_template, request, redirect, url_for

from models import Animal, AnimalType
from sqlalchemy import func


app = Flask(__name__)
app.secret_key = b"\xf9\x19\x8d\xd2\xb7N\x84\xae\x16\x0f'`U\x88x&\nF\xa2\xe9\xa1\xd7\x8b\t"


@app.route('/deposit', methods=['POST'])
def deposit():

    animal_type = session.query(AnimalType).filter(AnimalType.name == request.form['type']).first()
    if not animal_type:
        flash('Sorry, we do not accept animals of this type', 'danger')
        return redirect(url_for('animals_list'))

    animal = Animal(animal_type_id=animal_type.id,
                    name=request.form['name'],
                    weight=request.form['weight'],
                    age=request.form['age'])
    try:
        session.add(animal)
        session.commit()
    except:
        flash('Error occured', 'danger')

    return redirect(url_for('animals_list'))


@app.route('/')
def animals_list():
    animals = session.query(Animal).limit(10).all()
    return render_template('index.html', animals=animals)


@app.route('/stats')
def stats():
    animals = session.query(Animal).all()
    total = len(animals)
    count_by_type = session.query(func.count(Animal.id), AnimalType.name)\
        .select_from(Animal)\
        .join(Animal.animal_type)\
        .group_by(AnimalType.id).all()
    return render_template('stats.html', animals=animals, count_by_type=count_by_type, total=total,
                           count_by_user=[])


@app.route('/dummy/<amount>')
def dummy_data(amount):
    for i in range(int(amount)):
        for j in range(1, 5):
            animal = Animal(animal_type_id=j, name='test', weight=10, age=5)
            session.add(animal)
        if i % 1000 == 0:
            session.commit()
    return redirect(url_for('stats'))


if __name__ == '__main__':
    app.run()
