def get_aaroh(pattern):
    import numpy as np

    sargam_to_numeric_map = {'s':1,'r':2,'g':3,'m':4,'p':5,'d':6,'n':7}
    def covert_pattern_to_numeric(pattern):
        numeric_swar = []
        for swar in pattern:
            numeric_swar.append(sargam_to_numeric_map[swar])
        return numeric_swar

    pattern_numeric =  covert_pattern_to_numeric(pattern)
    def generate_aaroh(pattern):
        pattern_aaroh = pattern.copy()
        pattern_arroh_line = pattern.copy()
        for i in range(0,7):
            pattern_arroh_line = list(map(lambda x : x+1,pattern_arroh_line))
            pattern_aaroh.extend(pattern_arroh_line)
        return pattern_aaroh

    pattern_aaroh  = generate_aaroh(pattern_numeric)

    pattern_aaroh =  np.reshape(pattern_aaroh,(8,len(pattern)))

    for i in range(0,len(pattern_aaroh)):
        if pattern_aaroh[i][-1] == 8:
            end_block = i
            break

    pattern_aaroh = (np.delete(pattern_aaroh,np.s_[end_block+1:len(pattern_aaroh)],0))

    for i in range(pattern_aaroh.shape[0]):
        for j in range((pattern_aaroh.shape[1])):
            if (pattern_aaroh[i][j]) >= 8 :
                pattern_aaroh[i][j] = pattern_aaroh[i][j] - 7

    c_scale = {"Sa":1,"Re":2,"Ga":3,"Ma":4,"Pa":5,"Da":6,"Ni":7}

    final_pattern_shape = pattern_aaroh.shape
    def convert_pattern_to_scale(pattern):
        l = []
        for i in range(pattern.shape[0]):
            for j in range((pattern.shape[1])):
                l.append(get_key(c_scale,pattern[i][j]))
        return(l)
    def get_key(my_dict,val):
        for key, value in my_dict.items():
            if val == value:
                return key
    key_aaroh = convert_pattern_to_scale(pattern_aaroh)

    key_aaroh =  np.reshape(key_aaroh,(final_pattern_shape))

    return(key_aaroh)