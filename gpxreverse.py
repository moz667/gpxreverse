#!/usr/bin/env python3

import argparse
from os.path import isfile
import sys

import gpxpy
import gpxpy.gpx

def parse_arguments(args):
    parser = argparse.ArgumentParser(description='Reverse tracks, segments and/or points on a gpx file.')
    
    parser.add_argument(
        "-i", "--input", nargs='+', required=True, 
        help="Input GPX file"
    )
    parser.add_argument(
        "-o", "--output", nargs='+', required=True, 
        help="Output GPX file (reversed)"
    )
    parser.add_argument("-t", "--tracks", help="Reverse tracks", action="store_true")
    parser.add_argument("-s", "--segments", help="Reverse segments", action="store_true")
    parser.add_argument("-p", "--points", help="Reverse points", action="store_true")
    
    return parser.parse_args()

def validate(args):
    if not args.tracks and not args.segments and not args.points:
        print("You must select at least one entity to revert (--tracks, --segments and/or --points)")
        exit(0)

    if len(args.input) != 1:
        print("Only one input file its required.")
        exit(0)

    if len(args.output) != 1:
        print("Only one output file its required.")
        exit(0)

    if not isfile(args.input[0]):
        print("Input file %s doesn't exists." % args.input[0])
        exit(0)

    if isfile(args.output[0]):
        print("Output file %s already exists." % args.output[0])
        exit(0)

def main(args):
    validate(args)
    cur_gpx = None

    with open(args.input[0], 'r') as input_file:
        cur_gpx = gpxpy.parse(input_file)
    
    new_gpx = gpxpy.gpx.GPX()

    if args.tracks:
        cur_gpx.tracks.reverse()

    for cur_track in cur_gpx.tracks:
        new_track = gpxpy.gpx.GPXTrack()
        new_track.name = cur_track.name
        
        if args.segments:
            cur_track.segments.reverse()

        for cur_segment in cur_track.segments:
            new_segment = gpxpy.gpx.GPXTrackSegment()

            if args.points:
                cur_segment.points.reverse()

            new_segment.points = cur_segment.points
            new_track.segments.append(new_segment)
        
        new_gpx.tracks.append(new_track)

    with open(args.output[0], 'w') as output_file:
        output_file.write(new_gpx.to_xml())

    print('All done!!!')

if __name__ == '__main__':
    arguments = parse_arguments(sys.argv[1:])
    main(arguments)
