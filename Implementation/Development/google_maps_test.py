import sys
import time
import os
import subprocess
import os.path
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
 
 
class GoogleMapsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maps")
     
        self.create_map()
        self.display_map()
 
    def display_map(self):
     
        self.setCentralWidget(self.google_maps)
 
    def create_map(self):
        self.google_maps=QWebView()
        self.google_maps.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
        self.google_maps.settings().setAttribute(QWebSettings.JavascriptCanOpenWindows, True)
        self.google_maps.settings().setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)
 
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
       var results = []
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
     
     
     
     
     
       // // bounds of the desired area
       // var allowedBounds = new google.maps.LatLngBounds(
       // new google.maps.LatLng(70.33956792419954, 178.01171875),
       // new google.maps.LatLng(83.86483689701898, -88.033203125)
       // );
       // var lastValidCenter = map.getCenter();
     
       // google.maps.event.addListener(map, 'center_changed', function() {
       // if (allowedBounds.contains(map.getCenter())) {
       // // still within valid bounds, so save the last valid position
       // lastValidCenter = map.getCenter();
       // return;
       // }
     
       // // not valid anymore => return to last valid position
       // map.panTo(lastValidCenter);
       // });
     
     
       }
     
     
     
     
       function codeLatLng(lat,lng) {
     
       var results;
       var lat = parseFloat(lat);
       var lng = parseFloat(lng);
     
       var latlng = new google.maps.LatLng(lat, lng);
     
     
       geocoder.geocode({'latLng': latlng}, function(results, status) {
       if (status == google.maps.GeocoderStatus.OK) {
       console.log(results);
       console.log("test");
       console.log(results[5].formatted_address);
       highestLevel = results.slice(-1)[0];
     
       }
     
       else {
       console.log("fail");
       }
     
     
       });
     
     
     
       }
     
     
       function addMarker(location) {
     
     
       var marker = new google.maps.Marker({
       position: location,
       map: map
       });
     
       google.maps.event.addListener(marker, 'rightclick', function(event) {
       marker.setMap(null);
       });
     
     
       google.maps.event.addListener(marker, 'click', function(event) {
     
       $('#myModal').modal('show');
       var lat = marker.getPosition().lat();
       var lng = marker.getPosition().lng();
       console.log(markers.indexOf(marker));
       console.log(lat + " " + lng);
     
       codeLatLng(lat,lng);
       console.log(highestLevel);
     
     
     
       });
     
     
       markers.push(marker);
       }
     
     
     
     
     
       google.maps.event.addDomListener(window, 'load', initialize);
 
 
   </script>
 </head>
 <body>
   <div id="map-canvas"></div>
 </body>
</html> '''
        self.google_maps.setHtml(self.html)
 
if __name__=="__main__":
    application=QApplication(sys.argv)
    window=GoogleMapsWindow()
    window.show()
    window.raise_()
    application.exec_()
    print()
