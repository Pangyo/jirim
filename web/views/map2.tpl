
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8"> 
  <title> Galaxy Chart D3 example</title>
  <script src="/static/js/jquery-3.1.1.min.js"></script>
  <script src="/static/js/d3.min.js"></script>
  <script src="/static/js/galaxy.js"></script>
  <script src="/static/js/main-d3.js"></script>
  <style>
    
    .chart rect {
    fill: steelblue;
    }
    
    .chart text {
    fill: white;
    font: 10px sans-serif;
    text-anchor: end;
    }
    
    circle {
    fill: rgb(31, 79, 80);
    fill-opacity: .75;
    stroke: rgb(31, 119, 80);
    stroke-width: 1px;
    }
    
    .leaf circle {
    fill: #ff7f0e;
    fill-opacity: 1;
    }
    
    text {
    font: 10px sans-serif;
    }

    .link {
    stroke: #999;
    stroke-opacity: .6;
    }
    
  </style>
</head>
<body>
  <svg class="chart"></svg>
  <script src="/static/js/main-d3.js"></script>
  <script type="text/javascript"> 
    main("Federal_Budget.csv"); 
  </script>

<p> A "Galaxy Chart" is a way to display hierarchical data where the
value of a category is the sum of its children, such as a budget.  The
area of a circle is proportional to the value of that node, and the
child nodes are arranged radially in descending order.  The area of a
circle is equal to the sum of the areas of its satellite-children.
One advantage of this presentation is that it focuses attention on
the major elements, and presents inconsequential elements as, well,
inconsequential nodes.</p>


</body>
</html>
