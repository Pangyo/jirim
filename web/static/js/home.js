console.log("home.js is imported.");

var DIR = 'img/soft-scraps-icons/';

var nodes = null;
var edges = null;
var network = null;
var container;

// Called when the Visualization API is loaded.
function draw(jsonObj) {
    // console.log(jsonObj);
    // create people.
    // value corresponds with the age of the person
    var DIR = '/static/img/';

    var nodeArr = [];

    var nodes = jsonObj['result'];

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
    edges = [{
            from: 2,
            to: 1
        }, {
            from: 2,
            to: 3
        }
    ];

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
        }
    };
    network = new vis.Network(container, data, options);
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

function drawLnb() {
    var lnb = document.getElementById('lnb');
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
