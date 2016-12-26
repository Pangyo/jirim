<!DOCTYPE html>
<!-- saved from url=(0064)http://visjs.org/examples/network/nodeStyles/circularImages.html -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title> 지림 </title>

  <style type="text/css">
    body {
      font: 10pt arial;
    }
    #mynetwork {
      width: 800px;
      height: 800px;
      border: 1px solid lightgray;
      background-color:#333333;
    }
  </style>

  </script><script type="text/javascript" src="/static/js/vis.js"></script>
  <link href="/static/css/vis.min.css" rel="stylesheet" type="text/css">

  <script type="text/javascript"> 
  
  
    var DIR = 'img/soft-scraps-icons/';

    var nodes = null;
    var edges = null;
    var network = null;

    // Called when the Visualization API is loaded.
    function draw(jsonObj) {
      console.log(jsonObj);
      // create people.
      // value corresponds with the age of the person
      var DIR = '/static/img/';
    
      var nodeArr = [];
      
      var nodes = Object.keys(jsonObj);
      for (i = 0; i < nodes.length; i++) {
        console.log();
      
        nodeObj = jsonObj[nodes[i]];
        console.log(nodeObj);
        
        nodeName = nodes[i];
        
        nodeArr.push({id:i+1, shape: 'circularImage', image: DIR + 'bluehouse.jpg', label:nodeName } );
        }
      
      console.log(jsonObj['exid']);
      /*
      nodes = [
        {id: 1,  shape: 'circularImage', image: DIR + 'bluehouse.jpg', label:"청와대"},
        {id: 2,  shape: 'circularImage', image: DIR + 'sunsiri.jpg', label:"최순실"},
        {id: 3,  shape: 'circularImage', image: DIR + 'geunhye.jpg', brokenImage: DIR + 'missingBrokenImage.png', label:"박근혜"},
      ];
*/
      // create connections between people
      // value corresponds with the amount of contact between two people
      edges = [
        {from: 2, to: 1},
        {from: 2, to: 3}
      ]; 

      // create a network
      var container = document.getElementById('mynetwork');
      var data = {
        nodes: nodeArr,
        edges: edges
      };
      var options = {
        nodes: {
          borderWidth:4,
          size:30,
	      color: {
            border: '#222222',
            background: '#666666'
          },
          font:{color:'#eeeeee'}
        },
        edges: {
          color: 'lightgray'
        }
      };
      network = new vis.Network(container, data, options);
    }
  </script>
</head>

<body onload="draw({{graph}})">
{{graph}}

<h2> keyword : {{keyword}} </h2>


<div id="mynetwork"><div class="vis-network" tabindex="400" style="position: relative; overflow: hidden; touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); width: 400px; height: 400px"><canvas style="position: relative; touch-action: none; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); width: 400px; height: 400px;" width="400" height="400"></canvas></div></div>


</body></html>


