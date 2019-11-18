# ML_REST_API_Boilerplate

**ML_REST_API_Boilerplate**, developer friendly boilerplate for creating machine learning REST API's

**Modules**
* api
* database
* models
* services
* utils

## Installation

Choose one of the following options:

* To install ML_REST_API_Boilerplate, first clone the repository and then run: `pip install -r requirements.txt`.

### Run

To start the app , run `python application.py`.

### Application

#### API
You can create API endpoint for GET/POST methods in [src/api/__init__.py](https://github.com/4Five-Labs-Inc/ML_REST_API_Boilerplate/blob/master/src/api/__init__.py)

    @app.route('/', methods=['GET'])
    def sample():
        return 'hello world'

#### Service
You can add all your app services in [src/services/__init__.py](https://github.com/4Five-Labs-Inc/ML_REST_API_Boilerplate/blob/master/src/services/__init__.py)

    def service_name(self):
        return 'sample service'

#### Database
You can register a database connection under [src/database](https://github.com/4Five-Labs-Inc/ML_REST_API_Boilerplate/blob/master/src/database/connection.py)

#### Models
You can load all your machine learning models under [src/models](https://github.com/4Five-Labs-Inc/ML_REST_API_Boilerplate/blob/master/src/models)

#### Utils
You can add any extra utilities to your application under [src/utils](https://github.com/4Five-Labs-Inc/ML_REST_API_Boilerplate/blob/master/src/utils/utils.py)

## Contributing

Contributions are generally appreciated.

See the [Contributors' guide](https://github.com/4Five-Labs-Inc/ML_REST_API_Boilerplate/blob/master/CONTRIBUTING.md) for more information.

## Authors

* [4fivelabs](https://4fivelabs.com)

## License

The source code of Iconic Narada boilerplate is licensed under [MIT](https://opensource.org/licenses/MIT). 