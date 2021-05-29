# Snowfakery Extras

This is a collection of sample code and directions for creating plugins and providers for Snowfakery.

## Things you'll need

1. Python 3 (generally recent-ish version).
2. Snowfakery 1.9 or later.
3. Faker module for python (`pip3 install Faker`).
    1. A Faker sample community provider like [Microservice](https://github.com/craiga/faker-microservice): `pip3 install faker-microservice`
4. A recipe to work from (see recipes folder).

## Creating a fakery provider for Snowfakery

1. Create a directory in your project to hold your plugins.
2. Create a file named `__init__.py` in that directory to make a package.
3. Create directory for your new provider with the pattern `faker_[my_service_name]`, in my case `faker_nonprofit`.
4. In the directory create a file named `__init__.py` this defines the faker provider module.
5. Create your provider in that file (see example for details):
    1. `import faker.providers` to make sure you have required classes.
    2. Define a series of dictionaries for providers creating text.
    3. Create a class that extends the base: `class Provider(faker.providers.BaseProvider):`
    4. Define a method that returns the desired values: `def nonprofit_name(self):`
6. Create `test.py` in your `plugins` directory.
7. Add tests to make sure it works cause it helps keep life easy (see example): `$ python -m plugins.test`

## Attach Your Provider to your recipe

1. Open the basic recipe you want to use for testing (start with something simple you already know how to use).
2. Add a new line at the top to load the new plugin: `- plugin: plugins.faker_nonprofit`
3. Add/Update a field to use the new provider.
