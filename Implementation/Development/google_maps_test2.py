import sys
import time

from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import sqlite3
#        key = "AIzaSyC5RcJ7vLSEYF32KqDusnuRcLJiHW8EbDg"
class GoogleMap(QWebView):

    def __init__(self):
        
        super().__init__()




        self.html='''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        width: 100%
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
    <script>
     
        var map;
        var markers = [];
        var geocoder;
        var results = [];
        var coords = [];
        var highestLevel;
       
       
        function initialize() {
       
        geocoder = new google.maps.Geocoder();
       
        var Centre = new google.maps.LatLng(52.20255705185695,0.1373291015625);
        var mapOptions = {
        zoom: 8,
        minZoom: 3,
        center: Centre,
        mapTypeId: google.maps.MapTypeId.TERRAIN
        }
        map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);
       
        google.maps.event.addListener(map, 'click', function(event) {
        addMarker(event.latLng);
        });
       
       
        }


        
       
       
       
       
        function codeLatLng(lat,lng) {
       
           var results;
           var lat = parseFloat(lat);
           var lng = parseFloat(lng);
           coords.push(lat);
           coords.push(lng);
       
           var latlng = new google.maps.LatLng(lat, lng);
       
            var address;
           geocoder.geocode({'latLng': latlng}, function(results, status) {
               if (status == google.maps.GeocoderStatus.OK) {
                    for( var i = 0; i < results.length; i++){
                         address = results[5].formatted_address;
                    }
    
                    console.log(results[5].formatted_address);
                     highestLevel = results.slice(-1)[0];
       
                    }
       
            else {
              console.log("fail");
            }
       
       
        });
       return address;
       
       
        }
       
       
        function addMarker(location) {
       
       
        var marker = new google.maps.Marker({
        position: location,
        map: map
        });
        //markers.push(marker);
        var lat = marker.getPosition().lat();
        var lng = marker.getPosition().lng();
        var actualAddress = codeLatLng(lat,lng);
        markers.push({"Address":actualAddress,"Object":marker,"Lat":lat,"Lng":lng});
       
        google.maps.event.addListener(marker, 'rightclick', function(event) {
        marker.setMap(null);
        });
       
       
        google.maps.event.addListener(marker, 'click', function(event) {
       
        
        var lat = marker.getPosition().lat();
        
        var lng = marker.getPosition().lng();
        coords2.push(lng);
        coords2.push(lat);
        //console.log(markers.indexOf(marker));
        
        //console.log(lat + " " + lng);
       
        
        //console.log(highestLevel);
       
       
       
        });
       
       
       
       
        }
         function GetMarkers(){
           return markers;
        }
    
 
        
       
       
       
       
        google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html> '''
        self.setHtml(self.html)


        



class GoogleMapsWindow(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Maps")
      
        self.create_map()
        self.layout()

    def layout(self):

        self.getMarkersPushButton = QPushButton("Get Markers")

        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.google_maps)
        self.vLayout.addWidget(self.getMarkersPushButton)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.vLayout)

        self.setCentralWidget(self.mainWidget)


        self.getMarkersPushButton.clicked.connect(self.getMarkers)



    def SkateparkAdded(self):
        print("Skatepark added to the database")

    def getMarkers(self):

        markers = self.google_maps.page().mainFrame().evaluateJavaScript("GetMarkers()")
        for marker in markers:
            longitude=marker["Lng"]
            latitude=marker["Lat"]
        values=(longitude,latitude)
   
            
        print("Writing to database...")
        

        with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor=db.cursor()
            sql="insert into Skatepark(SkateparkLongitude,SkateparkLatitude) values (?,?)"
            cursor.execute(sql,values)
            db.commit()
            self.SkateparkAdded()
       

           


    def showMarker(self, markerStr):
        print(markerStr)


    def create_map(self):
        self.google_maps = GoogleMap()
        
##        self.google_maps.page().mainFrame().addToJavaScriptWindowObject("GoogleMapsWindow", self.google_maps)
##        self.google_maps.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
##        self.google_maps.settings().setAttribute(QWebSettings.JavascriptCanOpenWindows, True)
##        self.google_maps.settings().setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)


        

        
if __name__=="__main__":
    application=QApplication(sys.argv)
    window=GoogleMapsWindow()
    window.show()
    window.raise_()
    application.exec_()
    print()
    
