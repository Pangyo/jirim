console.log("home.js is imported.");

var DIR = 'img/soft-scraps-icons/';

var nodes = null;
var edges = null;
var network = null;
var container;

// Called when the Visualization API is loaded.
function draw(jsonObj) {
    // console.log(jsonObj);
    var DIR = '/static/img/';

    var nodeArr = [];

    var nodes = jsonObj;

    for (i = 0; i < nodes.length; i++) {
        node = nodes[i];
        // nodeArr.push({id:i+1, shape: 'circularImage', image: DIR + 'bluehouse.jpg', label:nodeName } );
        nodeArr.push({
            id: i + 1,
            label: decodeURIComponent(node.title)
        });
    }

    /*
    nodes = [{id: 1,  shape: 'circularImage', image: DIR + 'bluehouse.jpg', label:"û�ʹ�"},{id: 2,  shape: 'circularImage', image: DIR + 'sunsiri.jpg', label:"�ּ���"},{id: 3,  shape: 'circularImage', image: DIR + 'geunhye.jpg', brokenImage: DIR + 'missingBrokenImage.png', label:"�ڱ���"},
    ];
     */
    // create connections between people
    // value corresponds with the amount of contact between two people
/*
    edges = [{
            from: 2,
            to: 1
        }, {
            from: 2,
            to: 3
        }
    ];
*/

    // create a network
    container = document.getElementById('container');
    var data = {
        nodes: nodeArr,
        edges: edges
    };
    var options = {
        height: '90%',
        width: '90%',
        nodes: {
            borderWidth: 4,
            size: 30,
            color: {
                border: '#222222',
                background: '#666666'
            },
            font: {
                color: '#eeeeee'
            }
        },
        edges: {
            color: 'lightgray'
        },
        interaction:{
          hover:true
        }
    };
    var options = {interaction:{hover:true}};
    network = new vis.Network(container, data, options);
    event();
    console.log(network);
}

function updateNetworkHeight() {
    var width = window.innerWidth * 90 / 100;
    var height = window.innerHeight * 80 / 100;
    //  var container = document.getElementById('mynetwork');
    container.style.width = width + 'px';
    container.style.height = height + 'px';
    network.redraw();
}

function event() {
  network.on("click", function (params) {
        params.event = "[original event]";
        alert('<h2>Click event:</h2>' + JSON.stringify(params, null, 4));
    });
    network.on("doubleClick", function (params) {
        params.event = "[original event]";
        alert('<h2>doubleClick event:</h2>' + JSON.stringify(params, null, 4));
    });
    network.on("oncontext", function (params) {
        params.event = "[original event]";
        alert('<h2>oncontext (right click) event:</h2>' + JSON.stringify(params, null, 4));
    });
    network.on("dragStart", function (params) {
        params.event = "[original event]";
        alert('<h2>dragStart event:</h2>' + JSON.stringify(params, null, 4));
    });
    network.on("dragging", function (params) {
        params.event = "[original event]";
        alert('<h2>dragging event:</h2>' + JSON.stringify(params, null, 4));
    });
    network.on("dragEnd", function (params) {
        params.event = "[original event]";
        alert('<h2>dragEnd event:</h2>' + JSON.stringify(params, null, 4));
    });
    network.on("zoom", function (params) {
        alert('<h2>zoom event:</h2>' + JSON.stringify(params, null, 4));
    });
    network.on("showPopup", function (params) {
        alert('<h2>showPopup event: </h2>' + JSON.stringify(params, null, 4));
    });
    network.on("hidePopup", function () {
        console.log('hidePopup Event');
    });
    network.on("select", function (params) {
        console.log('select Event:', params);
    });
    network.on("selectNode", function (params) {
        console.log('selectNode Event:', params);
    });
    network.on("selectEdge", function (params) {
        console.log('selectEdge Event:', params);
    });
    network.on("deselectNode", function (params) {
        console.log('deselectNode Event:', params);
    });
    network.on("deselectEdge", function (params) {
        console.log('deselectEdge Event:', params);
    });
    network.on("hoverNode", function (params) {
        console.log('hoverNode Event:', params);
    });
    network.on("hoverEdge", function (params) {
        console.log('hoverEdge Event:', params);
    });
    network.on("blurNode", function (params) {
        console.log('blurNode Event:', params);
    });
    network.on("blurEdge", function (params) {
        console.log('blurEdge Event:', params);
    });
}

function reload() {
  $.ajax("http://naver.com", {
      success: function(data) {
        console.log(data);
         $('#main').html($(data).find('#main *'));
         $('#notification-bar').text('The page has been successfully loaded');
      },
      error: function() {
         $('#notification-bar').text('An error occurred');
      }
   });
}
