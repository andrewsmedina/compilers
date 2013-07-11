clean:
	@rm -rf *.out
	@rm -rf *.out.*

compile: clean
	@clang++ -g toy.cpp `llvm-config --cppflags --ldflags --libs core jit native` -O3 -o toy

