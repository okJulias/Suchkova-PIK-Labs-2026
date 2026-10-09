#include <iostream>
#include <string>
#include <set>
#include <cmath>
#include <iomanip> 

class BiquadraticSolver {
private:
    double a = 0.0;
    double b = 0.0;
    double c = 0.0;
    std::set<double> roots; 

    bool is_float(const std::string& value) const {
        if (value.empty()) return false;
        
        std::string cleaned = value;
        if (!cleaned.empty() && cleaned[0] == '-') {
            cleaned.erase(0, 1);
        }

        int dot_pos = cleaned.find('.');
        if (dot_pos != std::string::npos) {
            cleaned.erase(dot_pos, 1);
        }

        if (cleaned.empty()) return false;
        for (char ch : cleaned) {
            if (!std::isdigit(ch)) return false;
        }
        
        return true;
    }

    double calculate_discriminant() const {
        return b * b - 4 * a * c;
    }

public:
    BiquadraticSolver() = default;

    void load_coefficients(int argc, char* argv[]) {
        bool a_ready = false, b_ready = false, c_ready = false;

        if (argc == 4) {
            if (is_float(argv[1]) && std::stod(argv[1]) != 0) {
                a = std::stod(argv[1]);
                a_ready = true;
            } else {
                std::cout << "CLI parameter 'a' is invalid. It will be requested via keyboard.\n";
            }

            if (is_float(argv[2])) {
                b = std::stod(argv[2]);
                b_ready = true;
            } else {
                std::cout << "CLI parameter 'b' is invalid. It will be requested via keyboard.\n";
            }

            if (is_float(argv[3])) {
                c = std::stod(argv[3]);
                c_ready = true;
            } else {
                std::cout << "CLI parameter 'c' is invalid. It will be requested via keyboard.\n";
            }
        }

        if (!a_ready) {
            while (true) {
                std::string input_a;
                std::cout << "Enter coefficient a (not equal to 0): ";
                std::getline(std::cin, input_a);
                if (is_float(input_a) && std::stod(input_a) != 0) {
                    a = std::stod(input_a);
                    break;
                }
                std::cout << "Please enter a valid number (not 0).\n";
            }
        }

        if (!b_ready) {
            while (true) {
                std::string input_b;
                std::cout << "Enter coefficient b: ";
                std::getline(std::cin, input_b);
                if (is_float(input_b)) {
                    b = std::stod(input_b);
                    break;
                }
                std::cout << "Please enter a valid number.\n";
            }
        }

        if (!c_ready) {
            while (true) {
                std::string input_c;
                std::cout << "Enter coefficient c: ";
                std::getline(std::cin, input_c);
                if (is_float(input_c)) {
                    c = std::stod(input_c);
                    break;
                }
                std::cout << "Please enter a valid number.\n";
            }
        }

        std::cout << std::fixed << std::setprecision(1);
        std::cout << "Coefficients loaded: a=" << a << ", b=" << b << ", c=" << c << "\n";
    }

    void solve() {
        double d = calculate_discriminant();
        
        if (d < 0) return; 
        
        double t_1 = (-b + std::sqrt(d)) / (2 * a);
        double t_2 = (-b - std::sqrt(d)) / (2 * a);
        
        if (t_1 >= 0) {
            roots.insert(std::sqrt(t_1));
            roots.insert(-std::sqrt(t_1));
        }
        if (t_2 >= 0) {
            roots.insert(std::sqrt(t_2));
            roots.insert(-std::sqrt(t_2));
        }
    }

    void print_results() const {
        std::cout << std::fixed << std::setprecision(1);   
        
        if (roots.empty()) {
            std::cout << "No real roots!\n";
        } else {
            std::cout << "Equation roots: [";
            bool first = true;
            for (double root : roots) {
                if (!first) std::cout << ", ";
                std::cout << root;
                first = false;
            }
            std::cout << "]\n";
        }
    }
};

int main(int argc, char* argv[]) {
    BiquadraticSolver solver;

    solver.load_coefficients(argc, argv);
    solver.solve();
    solver.print_results();

    return 0;
}
