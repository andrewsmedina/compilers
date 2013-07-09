#include <cstdlib>
#include <string>

enum Token {
	tok_eof = -1,
	// commands
	tok_def = -2,
	tok_extern = -3,
	// primary
	tok_identifier = -4,
	tok_number = -5,
};

static std::string IdentifierStr;  // Filled in if tok_identifier
static double NumVal;              // Filled in if tok_number

static int gettok() {
	static int LastChar = ' ';

	while (isspace(LastChar)) {
		LastChar = getchar();
	}

	if (isalpha(LastChar)) {
		IdentifierStr = LastChar;
		while (isalnum((LastChar = getchar()))) {
			IdentifierStr += LastChar;
		}

		if (IdentifierStr == "def") {
			return tok_def;
		}
		if (IdentifierStr == "extern") {
			return tok_extern;
		}
		return tok_identifier;
	}

	if (isdigit(LastChar) || LastChar == '.') {
		std::string NumStr;
		do {
			NumStr += LastChar;
			LastChar = getchar();
		} while (isdigit(LastChar) || LastChar == '.');

		NumVal = strtod(NumStr.c_str(), 0);
		return tok_number;
	}

	if (LastChar == '#') {
		do {
			LastChar = getchar();
		} while (LastChar != EOF && LastChar != '\n' && LastChar != '\r');

		if (LastChar != EOF) {
			return gettok();
		}
	}

	if (LastChar == EOF) {
		return tok_eof;
	}

	int ThisChar = LastChar;
	LastChar = getchar();
	return ThisChar;
}

// ExprAST - Base class for all expression nodes.
class ExprAST {
public:
	virtual ~ExprAST() {}
};

// NumberExprAST - Expression class for numeric literals like "1.0".
class NumberExprAST : public ExprAST {
	double Val;
public:
	NumberExprAST(double val) : Val(val) {}
};

// VariableExprAST - Expression class for referencing a variable, like "a".
class VariableExprAST : public ExprAST {
	std::string Name;
public:
	VariableExprAST(const std::string &name) : Name(name) {}
};

// BinaryExprAST - Expression class for a binary operator.
class BinaryExprAST : public ExprAST {
	char Op;
	ExprAST *LHS, *RHS;
public:
	BinaryExprAST(char op, ExprAST *lhs, ExprAST *rhs)
		: Op(op), LHS(lhs), RHS(rhs) {}
};

int main() {
	return 0;
}
