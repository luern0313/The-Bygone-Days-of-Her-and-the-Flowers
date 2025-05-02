import math


class Lmd05:
    char_set = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#&"

    @classmethod
    def lmd0_5(cls, block_length=24) -> str:
        return cls(block_length).solve()

    def __init__(self, block_length):
        # 8  16 24 32
        # 24 48 72 96
        assert block_length % 24 == 0
        assert block_length >= 24
        assert block_length <= 96

        self.byte_array = bytearray()
        self.block_length = block_length
        self.rs = None
        self.cond = None
        self.init_magic_num()

    def set_byte_array(self, byte):
        self.byte_array = bytearray(byte)
        self.init_magic_num()

    def init_magic_num(self):
        self.rs = [0xae3115a1, 0xca0ef573, 0x866b151a, 0x993da81e]
        self.cond = 0

    def bits_transform_1(self, seed) -> int:
        self.rs[0] = ((self.rs[1] & self.rs[2]) | ((~self.rs[1]) & self.rs[3])) ^ self.rs[0]
        self.rs[0] ^= seed
        return self.rs[0]

    def bits_transform_2(self, seed) -> int:
        self.rs[1] = (self.rs[2] | self.rs[0] & ~self.rs[3]) ^ self.rs[1]
        self.rs[1] ^= seed
        return self.rs[1]

    def bits_transform_3(self, seed) -> int:
        self.rs[2] = self.rs[0] ^ self.rs[1] ^ self.rs[2] ^ self.rs[3]
        self.rs[2] ^= seed
        return self.rs[2]

    def bits_transform_4(self, seed) -> int:
        self.rs[3] = (self.rs[1] ^ ~self.rs[3] ^ (~self.rs[0] | self.rs[2]))
        self.rs[3] ^= seed
        return self.rs[3]

    def bits_transform(self, seed, output_bits, input_bits=32) -> int:
        t_full = Lmd05.get_full_int(seed, input_bits)
        self.cond = (self.cond ^ t_full) + 1 & 3

        if self.cond == 0:
            return self.bits_transform_1(seed) & (1 << output_bits) - 1
        elif self.cond == 1:
            return self.bits_transform_2(seed) & (1 << output_bits) - 1
        elif self.cond == 2:
            return self.bits_transform_3(seed) & (1 << output_bits) - 1
        elif self.cond == 3:
            return self.bits_transform_4(seed) & (1 << output_bits) - 1

    @staticmethod
    def get_full_int(integer, length) -> int:
        f_int = 0
        for _ in range(math.ceil(32 / length)):
            f_int <<= length
            f_int |= integer
        f_int &= 4294967295
        return f_int

    @staticmethod
    def loop_shift_left(x, n, length=32) -> int:
        return ((x << n) | (x >> length - n)) & ((1 << length) - 1)

    @staticmethod
    def compose_char(int1, int2) -> int:
        hex_num = int1 >> 4 & 3
        hex_num <<= 2
        hex_num ^= int1 & 15
        hex_num <<= 2
        hex_num ^= int1 >> 6 & 3
        hex_num ^= int2 & 15
        return hex_num

    def solve(self) -> str:
        block_length_half = self.block_length // 2
        vector_list = []
        for _ in range(block_length_half):
            vector_list.append(self.bits_transform(0, 8))
        vector_offset = 0

        full = self.block_length - len(self.byte_array) % self.block_length
        for i in range(full):
            full = self.loop_shift_left(full, 1, 8)
            self.byte_array.append(full)

        for offset_block in range(0, len(self.byte_array), self.block_length):
            for i in range(self.block_length):
                index = (i // 2 + vector_offset) % block_length_half
                b = self.byte_array[offset_block + i]
                vector_list[index] ^= self.bits_transform((i << 8) | b, 8, 16)

                vector_offset += b
                vector_offset %= block_length_half

        result_str_list = []

        random_result = self.rs[0] ^ self.rs[1] ^ self.rs[2] ^ self.rs[3]
        for i in range(len(vector_list)):
            vector_list[i] ^= random_result & 255

        for i in range(0, len(vector_list), 3):
            index0 = (i + vector_offset) % block_length_half
            index1 = (index0 + 1) % block_length_half
            index2 = (index0 + 2) % block_length_half
            result_str_list.insert(0, Lmd05.char_set[Lmd05.compose_char(vector_list[index0], vector_list[index1] >> 4)])
            result_str_list.insert(0, Lmd05.char_set[Lmd05.compose_char(vector_list[index2], vector_list[index1])])

        return "".join(result_str_list)


if __name__ == "__main__":
    lmd05 = Lmd05(24)
    lmd05.set_byte_array("0123456789012345678901230123456789".encode(encoding="utf-8"))
    print(lmd05.solve())
    lmd05.set_byte_array("luern0313".encode(encoding="utf-8"))
    print(lmd05.solve())
