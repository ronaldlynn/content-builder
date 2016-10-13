Content Builder
===============

The content builder script rapidly reads YAML content data and populates templates appropriately to quickly and consistently produce HTML content files.

## Environment Setup
Here's how to set up the local environment.

1. Install pip:

 ```
 $ sudo easy_install pip
 ```
1. Install virtualenv:

 ```
 $ sudo pip install virtualenv
 ```
1. Create virtual environment:

 ```
 $ mkdir ~/.virtualenv  # unless ~/.virtualenv already exists
 $ virtualenv --no-site-packages ~/.virtualenv/content-builder
 ```
1. Activate virtual environment:

 ```
 $ source ~/.virtualenv/content-builder/bin/activate
 ```
1. Install Jinja2 and PyYAML:

 ```
 (content-builder) $ pip install Jinja2
 (content-builder) $ pip install PyYAML
 ```
## Configure Paths
You'll need to set up the template, data, and output folders and files as they exist on your system.

1. Save ```settings-example.py``` as ```settings.py``` in the same folder.

1. Change the ```template_location``` and ```working_folder``` variables to match your local development environment.

## Running the Builder Script

1. Change to the folder containing the builder executable:
 ```
 $ cd <repo-path>/tools/builder/
 ```

1. Run the builder:

 ```
 $ python ./builder.py
 ```
