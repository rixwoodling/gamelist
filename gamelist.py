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
                    name = row['name']
                    desc = row['desc']
                    path = './'+ row['file']
                    image = './'+ row['file'].replace( '.zip','.png' )
                    video = './'+ row['file'].replace( '.zip','.mp4' )
                    genre = row['genre']
                    releasedate = row['releasedate'].replace( '-','' )
                    developer = row['developer']
                    publisher = row['publisher']
                    players = row['players']

                    output.write( '<game>'+'\n' )
                    output.write( '<name>'+ name +'</name>'+'\n' )
                    output.write( '<desc>'+ desc + '</desc>'+'\n' )
                    output.write( '<path>'+ path +'</path>'+'\n' )
                    output.write( '<image>'+ image + '</image>'+'\n' )
                    output.write( '<video>'+ video + '</video>'+'\n' )
                    output.write( '<genre>'+ genre + '</genre>'+'\n' )
                    output.write( '<releasedate>'+ releasedate + '</releasedate>'+'\n' )
                    output.write( '<developer>'+ developer + '</developer>'+'\n' )
                    output.write( '<publisher>'+ publisher + '</publisher>'+'\n' )
                    output.write( '<players>'+ players + '</players>'+'\n' )
                    output.write( '</game>'+'\n' )
                    output.write( '\n' )
                    print( row['name'] )
            output.close()
    else:
        help()

if __name__ == "__main__":
    csv2xml()

