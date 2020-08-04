var data = [{
  "city": "New York",
      "neighborhood": "N/A",
      "hits": 200
}, {
  "city": "New York",
      "neighborhood": "Brooklyn",
      "hits": 225
}, {
  "city": "New York",
      "neighborhood": "Queens",
      "hits": 1
}, {
  "city": "San Francisco",
      "neighborhood": "Chinatown",
      "hits": 268
}, {
  "city": "San Francisco",
      "neighborhood": "Downtown",
      "hits": 22
}, {
  "city": "Seattle",
      "neighborhood": "N/A",
      "hits": 2
}, {
  "city": "Seattle",
      "neighborhood": "Freemont",
      "hits": 25
}];
var pieChart = dc.pieChart("#pieChart"),
  rowChart = dc.rowChart("#rowChart");
var ndx = crossfilter(data),
  cityDimension = ndx.dimension(function (d) {
      return d.city;
  }),
  cityGroup = cityDimension.group().reduceSum(function (d) {
      return d.hits;
  }),
  neighborhoodDimension = ndx.dimension(function (d) {
      return d.neighborhood;
  }),
  neighborhoodGroup = neighborhoodDimension.group().reduceSum(function (d) {
      return d.hits;
  });

pieChart.width(200)
  .height(200)
  .slicesCap(4)
  .dimension(cityDimension)
  .group(cityGroup);
pieChart.filter = function() {};

  var colorScale = d3.scale.ordinal()
          .domain(["San Francisco", "New York", "Seattle"])
          .range(["#D82C8C", "#17A7CF", "#E58304"]);

  pieChart.colors(colorScale);

rowChart.width(500)
  .height(500)
  .dimension(neighborhoodDimension)
  .group(neighborhoodGroup);

dc.renderAll();

/*rating stars  Code by Zell Liew (https://codepen.io/zellwk/pen/YwjZQv)*/ 

               