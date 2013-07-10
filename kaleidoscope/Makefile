clean:
	@rm -rf *.out
	@rm -rf *.out.*

compile: clean
	@clang++ -g -O3 toy.cpp `llvm-config --cppflags --ldflags --libs core` -o toy

