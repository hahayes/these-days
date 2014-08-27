
var datafile = 'data.json';
var diameter = 500,
    format = d3.format(",d"),
    color = d3.scale.category20c();

var bubble = d3.layout.pack()
    .sort(null)
    .size([diameter, diameter])
    .padding(1.5);

var svg = d3.select("body").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
    .attr("class", "bubble");

function loadData(error, root) {
  var node = svg.selectAll(".node")
      .data(bubbles(root))
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  node.append("title")
      .text(function(d) { return d.msg; });

  node.append("circle")
      .attr("r", function(d) { return d.value; })
      .style("fill", function(d) { return color(d.value); });

  node.append("text")
      .attr("dy", ".3em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.msg; });
}

d3.json(datafile, loadData);

function bubbles(root) {
  var items = [];
  for (var i=0; i<root.length; i++) {
    cur = root[i];
    cur.value = cur.msg.length;
    items.push(cur);
  }
  var obj = bubble.nodes({children: items});
  obj.shift();
  return obj;
}

d3.select(self.frameElement).style("height", diameter + "px");
