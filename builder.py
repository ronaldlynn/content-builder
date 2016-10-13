#! /usr/bin/python

import jinja2, yaml, os, string, settings, json

template_location = settings.template_location
working_folder = settings.working_folder
data_folder = settings.data_folder
output_folder = settings.output_folder
data_extension = settings.data_extension
output_extension = settings.output_extension
template_extension = settings.template_extension
common_folder = settings.common_folder

print 'template_location: ' + template_location
print 'working_folder: ' + working_folder
print 'data_folder: ' + data_folder
print 'output_folder: ' + output_folder
print 'data_extension: ' + data_extension
print 'output_extension: ' + output_extension
print 'template_extension: ' + template_extension
print 'common_folder: ' + common_folder

def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

templateLoader = jinja2.FileSystemLoader( searchpath=template_location)
templateEnv = jinja2.Environment( loader=templateLoader, trim_blocks=True)

templateEnv.filters['jsonify'] = json.dumps

for input_subdir, dirs, files in os.walk(working_folder):

    if input_subdir.endswith(data_folder):
        output_subdir = input_subdir.replace(data_folder, output_folder);

        if not os.path.exists(output_subdir):
            print 'path missing. creating.'
            os.makedirs(output_subdir)

        for input_file in files:

            # if not a yaml file, skip it - avoids .DS_Store issues on OS X
            if input_file.endswith(data_extension):
                input_path = input_subdir + '/' + input_file

                output_path = output_subdir + '/' + input_file.replace(data_extension, output_extension)

                with open(input_path, 'r') as stream:

                    templateVars = yaml.load(stream)
                    templateVars['common_folder'] = common_folder
                    template_file = templateVars['exercise'] + template_extension

                    template = templateEnv.get_template( template_file )

                    outputText = template.render( templateVars )

                    with open(output_path, "wb") as fh:
                        fh.write(outputText)
