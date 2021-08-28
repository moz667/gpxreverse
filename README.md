# gpxreverse

Simply reverse the content of a gpx file thanks to the [gpxpy library](https://github.com/tkrajina/gpxpy).

## Installation
```bash
git clone https://github.com/moz667/gpxreverse.git .
pip3 install -r requirements.txt
```

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

### TODO List
 * [ ] Made a real installation ^_^
 * [ ] Made some tests
 * [ ] Interactive mode for select the entities to reverse
