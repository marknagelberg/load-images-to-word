from docxtpl import DocxTemplate, InlineImage
import sys
import os

word_doc_template = sys.argv[1]
word_doc_w_images_loaded = sys.argv[2]
image_dirname = sys.argv[3]

# Don't want to overwrite your template with the loaded images version.
assert word_doc_template != word_doc_w_images_loaded

doc = DocxTemplate(word_doc_template)

images_to_load = {}

for image_filename in os.listdir(image_dirname):
    # Remove extension to filename in dict key.
    template_varname = image_filename.split('.')[0]
    images_to_load[template_varname] = InlineImage(doc, 
            os.path.join(image_dirname, image_filename))

doc.render(images_to_load)

doc.save(word_doc_w_images_loaded)
