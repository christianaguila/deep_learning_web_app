var gmarkers =[];

function initMap(){
    var map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: parseFloat(12.87), lng: parseFloat(121.77)},
        zoom: 7,
        mapId: "e3a9a0796408a29c",
        gestureHandling: "cooperative",
        restriction: {
            latLngBounds: {north: parseFloat(18.5), south: parseFloat(4.5), west: parseFloat(115), east: parseFloat(130)},
            strictBounds: false,
          },
      });

    
    var img = new Image()
    var markers = []; 
    for(let i = 0; i<marker_locations.length; i++){
        let v = marker_locations[i]['fields']['predicted_plant_label'];
        if( v == 'Sorry, Plantita cannot recognize the Plant'){
            img.src = "/static/users/icons/map_unknown.png"
        }else{
            if (v == 'Anahaw - Saribus rotundifolius') {
                img.src = "/static/users/icons/map_anahaw.png"
              };
              if (v == 'Bagawak Morado - Clerodendrum quadriloculare') {
                img.src = "/static/users/icons/map_bagawakmorado.png"
              };
              if (v == 'Bignay - Antidesma bunius') {
                img.src = "/static/users/icons/map_bignay.png"
              };
              if (v == "Copeland's Pitcher - Nepenthes copelandii") {
                img.src = "/static/users/icons/map_pitcher.png"
              };
              if (v == 'Kalingag - Cinnamomum mercadoi') {
                img.src = "/static/users/icons/map_kalingag.png"
              };
              if (v == 'Katmon - Dillenia philippinensis') {
                img.src = "/static/users/icons/map_katmon.png"
              };
              if (v == 'Kris Plant - Alocasia sanderiana') {
                img.src = "/static/users/icons/map_krisplant.png"
              };
              if (v == 'Payau - Homalomena philippinensis') {
                img.src = "/static/users/icons/map_payau.png"
              };
              if (v == 'Tangisang-Bayawak - Ficus variegata') {
                img.src = "/static/users/icons/map_tangisang_bayawak.png"
              };
              if (v == 'Tayabak - Strongylodon macrobotrys') {
                img.src = "/static/users/icons/map_tayabak.png"
              };
        }
        let k = [marker_locations[i]['fields']['matched_address'], marker_locations[i]['fields']['latitude'] , marker_locations[i]['fields']['longitude'], img.src, 30, 30, marker_locations[i]['fields']['predicted_plant_label']]
        markers.push(k)
        
    }
    
    // ------------------ Marker Loop ---------------------//

    for(let i = 0; i<markers.length; i++){
        var currMarker = markers[i]

        const marker = new google.maps.Marker({
            position: {lat: parseFloat(currMarker[1]), lng: parseFloat(currMarker[2])},
            map,
            title: currMarker[0],
            icon: {
                url:currMarker[3],
                scaledSize: new google.maps.Size(currMarker[4], currMarker[5])
            },
            category: currMarker[6],
            animation: google.maps.Animation.DROP,
            });

            // marker.category = markers[i];
            gmarkers.push(marker);

        var circle = new google.maps.Circle({
            map: map,
            strokeColor: "#f4c1c1",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#f4c1c1",
            fillOpacity: 0.3,
            radius: 1000,
            });
            
        circle.bindTo('center', marker, 'position');
        const infowindow = new google.maps.InfoWindow({
                content: currMarker[0],
        });
        marker.addListener("click", toggleBounce)



    // ------------------ Information Window Loop ---------------------//
        function toggleBounce() {
            if (marker.getAnimation() !== null) {
              marker.setAnimation(null);
            } else {
              marker.setAnimation(google.maps.Animation.BOUNCE);
              setTimeout(function(){ marker.setAnimation(null); }, 1400);
            }
          }


            marker.addListener('click', function () {
                if (infowindow) { infowindow.close();}
                infowindow.open(map, marker);
                map.panTo(this.getPosition());
                map.setZoom(11);
                window.setTimeout(function() {map.setZoom(map.getZoom());},3000);
            });

        }
    

        filterMarkers = function (category) {
            for (i = 0; i < markers.length; i++) {
                markerval = gmarkers[i];
                // If is same category or category not picked
                if (markerval.category == category || category.length === 0) {
                    markerval.setVisible(true);
                }
                // Categories don't match 
                else {
                    markerval.setVisible(false);
                }
            }
        }
    
    }
