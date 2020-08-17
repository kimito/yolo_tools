# Annotation Format Converter from VoTT to Darknet

To Use:
1. Annotate images by [VoTT](https://github.com/microsoft/VoTT).
2. Export annotations with Pascal VOC format.
3. To create labels.txt from *.pbtxt, Run below in export directory.
```sh
grep name *.pbtxt | sed "s/^.*name: //" | sed "s/'//g" > labels.txt
```
3. Run:
```sh
python3 pascalvoc2darknet.py EXPORT_DIRECTORY
```
Here EXPORT_DIRECTRY is a path to the export directory.

4. You will see *.txt in "Annotation" subdirectory in export directory for annotation files for Darknet.