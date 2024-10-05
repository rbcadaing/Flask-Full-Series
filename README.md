Source : https://www.youtube.com/watch?v=p068JokuThU&list=PLOkVupluCIjuPtTkhO6jmA76uQR994Wvi

Open miniforge terminal and run below commands.
    1. `conda create -n FlaskMarket python=3.10.8 -y`
    2. `conda activate FlaskMarket`
    3. `pip install -r requirements.txt`
    4. `Deactivate active Virtual Environment` `conda deactivate`

Create Virtual Env using Python
    1. create virtual env `py -m venv .venv`
    2. activate venv `.venv\Scripts\activate`
    3. verify `venv where python`
    4. deactivate venv `deactivate`


Pre-req prior to running the app
    1. set FLASK_APP=market.py `setup flask entry env variable`
    2. set FLASK_DEBUG=1 `set flask to debug mode`


Initialize Database
    >>> from market import app, db
    >>> app.app_context().push()
    >>> db.create_all()
    >>> from market import Item
    >>> item1 = Item(name="Iphone 10",price=500,barcode='9876939783',description='desc')
    >>> db.session.add(item1)
    >>> db.session.commit()
Verify if data has been save to db
    >>> Item.query.all()

Clear Python Console
    >>> import os
    >>> os.system('cls')

Generate ramdom key

    >>> import os
    >>> os.urandom(12).hex()