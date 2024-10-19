from pathlib import Path

head = """#include <iostream>
constexpr char g(std::bitset<5>p){return" \\n.,-'abcdefghijklmnopqrstuvwxyz"[p.to_ulong()];}int main(){for(auto p:U\""""

tail = """\"){if(!p)continue;p-=0x1F;if(p>=0xd81f)p-=0X7E0;for(int i:{15,10,5,0})std::cout<<g((p>>i)&0b11111);}}"""

characters = " \n.,-'abcdefghijklmnopqrstuvwxyz"
LATIN_BIN_MAPPING = {
    char: format(i, '05b')
    for i, char in enumerate(characters)
}

def utf_encode(latin_str: str) -> str:
    """Each character in the string is encoded using 5 bits only."""
    encoded_result = ""
    for char in latin_str.lower():
        char_code = LATIN_BIN_MAPPING.get(char, LATIN_BIN_MAPPING[" "])
        encoded_result += char_code

    return encoded_result


def encode_bin_to_chars(binary: str) -> str:
    result = ""
    for i in range(0, len(binary), 20):
        unicode_codepoint = int(binary[i:i+20], base=2) + 0x1F
        if unicode_codepoint > 0xD800 + 0x1F:
            unicode_codepoint += 0XDFFF - 0xD800 - 0x1F
        result += chr(unicode_codepoint)

    return result

# Driver function
if __name__ == "__main__":
    text_to_encode = Path("./input.txt").read_text()

    encoded_text_binary = utf_encode(text_to_encode)
    encoded_text_utf8 = encode_bin_to_chars(encoded_text_binary)

    cpp_contents = head + encoded_text_utf8 + tail

    with open("main.cpp", "w") as f:
        f.write(cpp_contents)

    print(f"Successfully generated code. Total CPP source length: {len(cpp_contents)}")
