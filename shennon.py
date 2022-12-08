import math
from bitstring import BitArray

class Shennon():
    def __init__(self):
        self.p_sum = []
        self.len = []
        self.d = {}
        self.code = {}

    def calc(self, string):
        self.d = dict.fromkeys(set(string), 0)
        for i in string:
            self.d[i] += 1
        for key in self.d:
            self.d[key] = self.d[key] / len(string)
        self.d = dict(sorted(self.d.items(), key=lambda item: item[1], reverse=True))
        self.p_sum.append(0)
        tired = 0
        for value in self.d.values():
            tired += value
            self.p_sum.append(tired)
            self.len.append(int(math.log(value, 2) * (-1) + 0.9999))
        self.p_sum.pop(len(self.p_sum)-1)
        self.code = dict.fromkeys(self.d.keys(), '')
        i = 0
        for key in self.code:
            b = self.p_sum[i]
            for j in range(self.len[i]):
                b = b * 2
                if b > 1:
                    self.code[key] = self.code[key] + str(1)
                    b = b - 1
                else:
                    self.code[key] = self.code[key] + str(0)
            i += 1
            self.code[key] = BitArray(bin=self.code[key])

    def calc_by_prob(self, prob_list):
        prob_list = sorted(prob_list, reverse=True)
        self.p_sum.append(0)
        tired = 0
        for value in prob_list:
            tired += value
            self.p_sum.append(tired)
            self.len.append(int(math.log(value, 2) * (-1) + 0.9999))
        self.p_sum.pop(len(self.p_sum)-1)
        self.code = dict.fromkeys([str(x) for x in range(len(prob_list))], '')
        i = 0
        for key in self.code:
            b = self.p_sum[i]
            for j in range(self.len[i]):
                b = b * 2
                if b > 1:
                    self.code[key] = self.code[key] + str(1)
                    b = b - 1
                else:
                    self.code[key] = self.code[key] + str(0)
            i += 1
            self.code[key] = BitArray(bin=self.code[key])


    def save_probs(self):
        with open('probs.txt', 'w') as f:
            for key in self.d.keys():
                if key == '\n':
                    f.write('\\n' + ' ')
                else:
                    f.write(key + ' ')
            f.write('\n')
            for value in self.d.values():
                f.write(str(value) + ' ')

    def save_encoded(self, string):
        with open('encoded.bin', 'wb') as f:
            for i in string:
                obj = self.code.get(i)
                obj.tofile(f)





if __name__ == '__main__':
    #     length and average code length
    for i in range(n):
        a+= p[i] * p_len[i]
        b+=(-1)*p[i]*(math.log(p[i],2))
    print("The corresponding codeword length is:"+str(p_len))
    print("The average code length is:"+'%.5s' % str(a))
    print("Source entropy" + '%.5s' % str(b))
    print("The average information transmission rate is:" +'%.5s' % str(b/a))
    # Code
    for i in range(n):
        code[str(p_sum[i])] = '0.'
        b = p_sum[i]
        for j in range(p_len[i]):
            b = b * 2
            if b > 1:
                code[str(p_sum[i])] = code[str(p_sum[i])] + str(1)
                b = b - 1
            else:
                code[str(p_sum[i])] = code[str(p_sum[i])] + str(0)
    for each in code:
        code[each] = code[each][2:]
    print("Coding corresponding to each probability"+ str(code))