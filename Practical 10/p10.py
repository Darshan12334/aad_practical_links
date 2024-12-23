import streamlit as st
import heapq

# Huffman Node class
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(char_freq):
    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Function to generate Huffman Codes
def generate_huffman_codes(root, code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = code

    generate_huffman_codes(root.left, code + "0", huffman_codes)
    generate_huffman_codes(root.right, code + "1", huffman_codes)

# Function to encode a text using Huffman codes
def encode_text(text, huffman_codes):
    try:
        return ''.join(huffman_codes[char] for char in text)
    except KeyError as e:
        raise ValueError(f"Character '{e.args[0]}' not found in Huffman codes. Please ensure all characters are defined.")

# Function to decode a binary string using Huffman Tree
def decode_text(binary_string, root):
    decoded_text = ""
    current = root

    for bit in binary_string:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root

    return decoded_text

# Streamlit App
st.title("Huffman Coding Tool")

# Input Frequencies
char_freq_input = st.text_area("Enter character frequencies (e.g., A:0.5,B:0.35,C:0.1):", "A:0.5,B:0.35,C:0.1,D:0.05,E:0.1")
char_freq = {pair.split(":")[0]: float(pair.split(":")[1]) for pair in char_freq_input.split(",")}

# Build Huffman Tree
huffman_tree_root = build_huffman_tree(char_freq)
huffman_codes = {}
generate_huffman_codes(huffman_tree_root, "", huffman_codes)

st.write("Huffman Codes:")
st.write(huffman_codes)

# Encoding Section
text_to_encode = st.text_input("Enter text to encode:", "CAD-BE")
if any(char not in char_freq for char in text_to_encode):
    st.warning("Some characters in the input text are not defined in the character frequencies.")
else:
    try:
        encoded_text = encode_text(text_to_encode, huffman_codes)
        st.write("Encoded Text:", encoded_text)
    except ValueError as e:
        st.error(e)

# Decoding Section
binary_to_decode = st.text_input("Enter binary string to decode:", "1100110110")
try:
    decoded_text = decode_text(binary_to_decode, huffman_tree_root)
    st.write("Decoded Text:", decoded_text)
except Exception as e:
    st.error("Error decoding the binary string. Ensure it is valid for the current Huffman tree.")
