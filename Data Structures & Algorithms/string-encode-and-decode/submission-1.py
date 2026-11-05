class Solution:

    def encode_str(self, s:str) -> str:
        encrypted_s = ""

        for ch in s:
            encrypted_s += chr(ord(ch) + 1)

        print(encrypted_s)
        return encrypted_s

    def encode(self, strs: List[str]) -> str:
        result = ""

        for str in strs:
            encrypted_str = self.encode_str(str)
            result += encrypted_str + "\n"
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        single_str = ""
        for ch in s:
            if ch == "\n":
                result.append(single_str)
                single_str = ""
            else:
                single_str += chr(ord(ch) - 1)
        return result


    
