def simple_test(funct,ins,outs):
    for i,o in zip(ins,outs):
        assert funct(i)==o,"Expected {} with input {} but got {}".format(o,i,funct(i))
    return True

def multi_param_test(funct,ins,outs):
    for i,o in zip(ins,outs):
        assert funct(*i)==o,"Expected {} with input {} but got {}".format(o,i,funct(*i))
    return True

def expects_no_output(funct,ins,outs):
    for i,o in zip(ins,outs):
        assert funct(i, nulloutput=True)==o,"Expected {} with input {} but got {}".format(o,i,funct(i))
    return True
