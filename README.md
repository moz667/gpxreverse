# gpxreverse

Simply reverse the content of a gpx file

## Usage

```bash
python3 gpxreverse -i original.gpx -o reversed.gpx [OPTIONS]
```
### Mandatory arguments
 * -i, --input [input-file.gpx]: gpx source file to convert
 * -o, --output [ouput-file.gpx]: gpx target file of reversed input file
### OPTIONS: At least one of these arguments
 * -t, --tracks: reverse tracks
 * -s, --segments: reverse segments
 * -p, --points: reverse points
