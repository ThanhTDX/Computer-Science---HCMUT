main: main.cpp 
	g++ -g main.cpp ./dsacpp/src/geom/*.cpp -I dsacpp/include -o ./bin/main 
	./bin/main

testcase:
	g++ ./dsacpp/dsa_main_test.cpp ./dsacpp/src/geom/*.cpp -I ./dsacpp/include -I ./doctest -o ./bin/dsa_main_test
	./bin/dsa_main_test