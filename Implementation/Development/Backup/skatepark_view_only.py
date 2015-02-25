from PyQt4.QtWebKit import *
import sqlite3
from PyQt4.QtSql import *
import time
##google.maps.event.addListener(marker, 'mouseover', function(event) {
##    infowindow.open(map,marker);
##  });
#        key = "AIzaSyC5RcJ7vLSEYF32KqDusnuRcLJiHW8EbDg"

class CustomQWebPage(QWebPage):
    def __init__(self):
        super().__init__()
        print("QWebPage constructor")

    def javaScriptConsoleMessage(self,message,lineNumber,sourceID):
        print(message,lineNumber,sourceID)
        print("javascript console message^")

class ViewOnlyMap(QWebView):
   

    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebSettings.JavascriptCanOpenWindows, True)
        self.settings().setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)
        self.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.CustomPage=CustomQWebPage()
        self.Coordinates=None
        self.setPage(self.CustomPage)
        self.loadFinished.connect(self.handle_load_finished)
        
        
        self.set_code()
        print("Code set")

    def mousePressEvent(self,event):
        super().mousePressEvent(event)
        if not self.parent.skatepark_name.isReadOnly():
            self.get_last_marker()
        else:
            print()
            print("In view only mode.")
            print()        

    def get_last_marker(self):
        print("GLM")
        #self.LastMarker=self.CustomPage.mainFrame().evaluateJavaScript("Test()")
        self.LastMarker= self.CustomPage.mainFrame().evaluateJavaScript("GetMarkers()")
        print(self.LastMarker)
        self.parent.fill_line_edits(self.LastMarker)

    def delete_all_markers(self):
        self.CustomPage.mainFrame().evaluateJavaScript("DeleteMarkers()")
        print()
        print("All Markers Deleted")
        print()
        

        

    def handle_load_finished(self,ok):
        if ok:
            print("Google Maps Loaded")
            self.get_marker_coordinates()
        else:
            print("Error: Google Maps Not Loaded.")
    

        
        
    def get_marker_coordinates(self):
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor=db.cursor()
            sql="select SkateparkLatitude, SkateparkLongitude, SkateparkDescription, SkateparkName from Skatepark"
            cursor.execute(sql)
            self.Coordinates=cursor.fetchall()
        for coordinate in self.Coordinates:
            Name=str(coordinate[3])
            Name="'{0}'".format(Name)
            
            Description=str(coordinate[2])
            Description="'{0}'".format(Description)
            
            print(Description)
            print(coordinate[0])
            print(coordinate[1])
            self.CustomPage.mainFrame().evaluateJavaScript("MarkersFromDatabase({0}, {1}, {2}, {3})".format(coordinate[0], coordinate[1], Description, Name))
            print("Marker added")
            
            
        
    
                        
        
            
        
    def set_code(self):

   
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
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC5RcJ7vLSEYF32KqDusnuRcLJiHW8EbDg"></script>
    <script>
     
        var map;
        var markers = [];
        var results = [];
        var coords = [];
        var highestLevel;
       
       
        function initialize() {
       
       
        var Centre = new google.maps.LatLng(52.20255705185695,0.1373291015625);
        var mapOptions = {
        zoom: 8,
        minZoom: 3,
        center: Centre,
        }
        map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);

        google.maps.event.addListener(map, 'click', function(event) {
        AddMarker(event.latLng);
        });

         }


         function MarkersFromDatabase(SkateparkLat,SkateparkLng,SkateparkDescription, SkateparkName) {
        
        var Skatepark = new google.maps.LatLng(SkateparkLat,SkateparkLng);

        AddMarker(Skatepark,SkateparkDescription, SkateparkName); }


       
       
        function AddMarker(Location,Description, SkateparkName) {
       
       
        var marker = new google.maps.Marker({
        title: 'Test',
        position: Location,
        animation: google.maps.Animation.DROP,
        map: map
        
        });
        //markers.push(marker);
        var lat = marker.getPosition().lat();
        var lng = marker.getPosition().lng();
        markers.push({"Object":marker,"Lat":lat,"Lng":lng, "Desc":Description});
		
	var contentString = ('<div id="content"><div id="siteNotice"></div> <h1 id="firstHeading" class="firstHeading">'+ SkateparkName + '</h1> <div id="bodyContent"><p>' + Description +'</p></div></div>');
		
      var infowindow = new google.maps.InfoWindow({
      content: contentString
  });
       
      google.maps.event.addListener(marker, 'rightclick', function(event) {
        marker.setMap(null);
        });
    google.maps.event.addListener(marker, 'mouseover', function(event) {
    infowindow.open(map,marker);
  });
  google.maps.event.addListener(marker,'mouseout', function(event){
  infowindow.close(map,marker)
  });
  

       }


function GetMarkers(){
    var Longitude=markers[markers.length - 1]["Lng"]
    var Latitude=markers[markers.length - 1]["Lat"]
    var coors=[Latitude,Longitude]
     return coors;
        }


function DeleteMarkers(){
    markers = [];
    initialize();
    }
    
google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html> '''
        self.setHtml(self.html) 
