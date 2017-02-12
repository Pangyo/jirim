<!DOCTYPE html>
<!-- saved from url=(0064)http://visjs.org/examples/network/nodeStyles/circularImages.html -->
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title> 지림 </title>

            <style type="text/css">
            html, body {
              font: 10pt arial;
            }
            #container {
              width: 90vw;
              height: 80vh;
              border: 1px solid lightgray;
              background-color:#333333;
            }
            </style>

            <link href="/static/css/vis.min.css" rel="stylesheet" type="text/css">
            <script type="text/javascript" src="/static/js/jquery-3.1.1.min.js"> </script>
            <script type="text/javascript" src="/static/js/vis.min.js"> </script>
            <script type="text/javascript" src="/static/js/home.js"> </script>
    </head>

    <body onload="draw({{graph}});" onresize="updateNetworkHeight()">
        <h3> keyword : {{keyword}} </h3>
        <a href="#" onclick="reload();">검색어 리로드</a>

        <!-- Left Navigation Bar -->
        <div id="lnb">

        </div>

        <!-- Graph -->
        <div id="container"/>

    </body>
</html>
