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
      position: absolute;
      width: 90vw;
      height: 80vh;
      top:55px;
      border: 1px solid lightgray;
      background-color:#333333;
      }
    </style>
    <link href="/static/css/vis.min.css" rel="stylesheet" type="text/css">
    <!-- Bootstrap Core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="/static/css/sb-admin.css" rel="stylesheet">
    <!-- Morris Charts CSS -->
    <link href="/static/css/morris.css" rel="stylesheet">
    <!-- Custom Fonts -->
    <link href="/static/css/fonts/font-awesome.min.css" rel="stylesheet" type="text/css">
    <script type="text/javascript" src="/static/js/jquery-3.1.1.min.js"> </script>
    <script type="text/javascript" src="/static/js/vis.min.js"> </script>
    <script type="text/javascript" src="/static/js/home.js"> </script>
  </head>
 </ul>

  <body onload="draw({{graph}});" onresize="updateNetworkHeight()">
    <div id="wrapper">
      <!-- Navigation -->
      <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/graph">JIRIM</a>
        </div>
        <!-- Top Menu Items -->
        <ul class="nav navbar-right top-nav">
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> John Smith <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li>
                <a href="#"><i class="fa fa-fw fa-user"></i> Profile</a>
              </li>
              <li>
                <a href="#"><i class="fa fa-fw fa-envelope"></i> Inbox</a>
              </li>
              <li>
                <a href="#"><i class="fa fa-fw fa-gear"></i> Settings</a>
              </li>
              <li class="divider"></li>
              <li>
                <a href="#"><i class="fa fa-fw fa-power-off"></i> Log Out</a>
              </li>
            </ul>
          </li>
        </ul>
        <!-- Sidebar Menu Items - These collapse to the responsive navigation menu on small screens -->
        <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav side-nav">
            <li class="active">
              % for r in graph["relations"]:
                 <li>
                   <a href="#" onclick="draw({{r}})"><i class="fa fa-fw fa-dashboard"></i> {{r["title"]}}</a>
                 </li>
                <br>
              % end
            </li>
          </ul>
        </div>
        <!-- /.navbar-collapse -->
      </nav>
      <div class="container-fluid">
        <!-- Page Heading -->
        <div class="row">
          <!--
          <h3> keyword : {{keyword}} </h3>
          <a href="#" onclick="reload();">검색어 리로드</a>
          -->
          <!-- Graph -->
          <div id="container"/>
          </div>
        </div>
      </div>
      <!-- /#page-wrapper -->
    </div>
    <!-- /#wrapper -->
    <!-- Bootstrap Core JavaScript -->
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>
