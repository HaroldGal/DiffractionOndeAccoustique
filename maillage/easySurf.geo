Mesh.MshFileVersion = 2.2;
h=1/10;

/*
Point(1) = {-1/8,-1/8,0,h};
Point(2) = {-1/8,1/8,0,h};
Point(3) = {1/8,1/8,0,h};
Point(4) = {1/8,-1/8,0,h};
*/

Point(11) = {0, 0, 0, h};
Point(12) = {-1/4, 0, 0, h};
Point(13) = {0, -1/4, 0, h};
Point(14) = {1/4, 0, 0, h};
Point(15) = {0, 1/4, 0, h};


Point(5) = {0,0,0,h};
Point(6) = {2,0,0,h};

Point(7) = {0,-1,0,h};
Point(8) = {-3,0,0,h};
Point(9) = {0,1,0,h};
Point(10) = {3,0,0,h};

/*
Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,1};
*/

Circle(1) = {12,11,13};
Circle(2) = {13,11,14};
Circle(3) = {14,11,15};
Circle(4) = {15,11,12};

Ellipse(5) = {7,5,6,8};
Ellipse(6) = {8,5,6,9};
Ellipse(7) = {9,5,6,10};
Ellipse(8) = {10,5,6,7};

Line Loop(1) = {1,2,3,4};
Line Loop(2) = {5,6,7,8};
Plane Surface(2) = {1,2};
Physical Surface(1) = {2};
Physical Line(2) = {1, 2, 3, 4};
Physical Line(3) = {5, 6, 7, 8};
