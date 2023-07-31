#!/bin/env python

import os
import sys
import csv

def help():
    print( 'add file argument' )

def csv2xml():
    if len( sys.argv ) > 1:
        csv_file = sys.argv[1]

        if os.path.exists( csv_file ):
            csv_dir = os.path.dirname( os.path.abspath( csv_file ))
            xml_file = csv_dir +'/'+ 'gamelist.xml'
            open( xml_file, 'w' ).close()

            output = open( xml_file, 'a' )
            output.write( '<?xml version="1.0"?>' +'\n' )
            output.write( '<gameList>' +'\n'+'\n' ) 

            with open( csv_file,'r' ) as f:
                reader = csv.DictReader( f )
                for row in reader:
                    output.write( '<name>'+ row['name'] +'</name>'+'\n' )
                    output.write( '\n' )
                    print( row['name'] )
            output.close()
    else:
        help()

if __name__ == "__main__":
    csv2xml()

