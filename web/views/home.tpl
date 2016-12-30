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
        
        <script type="text/javascript" src="/static/js/vis.js"/>
        
        <script type="text/javascript" src="/static/js/home.js"/>

    </head>

    <body onload="draw({{graph}}); drawLnb();" onresize="updateNetworkHeight()">
    {{graph}}

        <h3> keyword : {{keyword}} </h3>

        <!-- Left Navigation Bar -->
        <div id="lnb"> 

        </div>

        <!-- Graph -->
        <div id="container"/>

    </body>
</html>


    