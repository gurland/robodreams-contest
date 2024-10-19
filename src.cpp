#include <iostream>

using namespace std;

constexpr char32_t input_text[] = U"慼";

constexpr char get_char(std::bitset<5> code_point) {
    constexpr char alphabet[] = " \n.,-'abcdefghijklmnopqrstuvwxyz";
    return alphabet[code_point.to_ulong()];
}

void print_decoded(uint32_t utf8_char) {
    if (utf8_char >= 0xDFFF) {
        // Remove offset of the surrogate range
        utf8_char -= 0XDFFF - 0xD800;
    }
    for (int i = 15; i >= 0; i -= 5) {
        // Extract 4x5 bit bitsets out of the utf8 character
        unsigned int codepoint = (utf8_char >> i) & 0b11111;
        std::cout << get_char(codepoint);
    }
}


int main() {
    for (auto &&code_point : input_text) print_decoded(code_point);
}
