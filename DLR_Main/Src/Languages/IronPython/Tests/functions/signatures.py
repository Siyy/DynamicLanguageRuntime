######################################################################################
#
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
# This source code is subject to terms and conditions of the Microsoft Public License. A 
# copy of the license can be found in the License.html file at the root of this distribution. If 
# you cannot locate the  Microsoft Public License, please send an email to 
# ironpy@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
# by the terms of the Microsoft Public License.
#
# You must not remove this notice, or any other, from this software.
#
#
#####################################################################################


#--IMPORTS---------------------------------------------------------------------
from iptest.assert_util import *

#--HELPERS---------------------------------------------------------------------
def gen_major_cases():
    '''
    Helper function used to automatically and exhaustively generate test cases
    for all Python function signatures IronPython optimizes for.
    '''
    NUM_PARAMS = 15
    NUM_KWPARAMS = 15
    NICE_SPACE = " " *3
    
    for num_params in xrange(0, NUM_PARAMS):
        for num_kwparams in xrange(0, NUM_KWPARAMS):
            print NICE_SPACE, "#--%d params with %d keyword params--#" % (num_params, num_kwparams)
            print NICE_SPACE, "def f%dParams%dKwparams(" % (num_params, num_kwparams),
            for i in xrange(0, num_params):
                if i==num_params-1 and num_kwparams==0:
                    print "p%d" % (i+1),
                else:
                    print "p%d," % (i+1),
            for i in xrange(0, num_kwparams):
                if i!=num_kwparams-1:
                    print "kw%d=%d," % (i+1, i+1), 
                else:
                    print "kw%d=%d" % (i+1, i+1), 
            print "):"
            if num_params==0:
                print NICE_SPACE, "    ret_valP = ()"
            else:
                print NICE_SPACE, "    ret_valP = (",
                for i in xrange(0, num_params):
                    print "p%d" % (i+1),
                    print ",",
                    if i==num_params-1:
                        print ")"
            
            if num_kwparams==0:
                print NICE_SPACE, "    ret_valKW = ()"
            else:
                print NICE_SPACE, "    ret_valKW = (",
                for i in xrange(0, num_kwparams):
                    print "kw%d" % (i+1),
                    print ",",
                    if i==num_kwparams-1:
                        print ")"
                                         
            print NICE_SPACE, "    return ret_valP, ret_valKW"                    
            print ""
            
            params = str(range(1, num_params+1))[1:-1]
            params_expected = params
            if num_params==1:
                params_expected += ","
                
            kwparams_expected = str(range(1, num_kwparams+1))[1:-1]
            if num_kwparams==1:
                kwparams_expected += ","
            print NICE_SPACE, "AreEqual(f%dParams%dKwparams(%s" % (num_params, num_kwparams, params), "),"
            print NICE_SPACE, "         ((%s), " % params_expected, "(%s))" % kwparams_expected, ")"
            print NICE_SPACE, ""
            
            for i in xrange(0, num_kwparams):
                kwparams = str(["kw%d=None" % (x+1) for x in xrange(0, i+1)])[1:-1].replace("'", "")
                kwparams_expected = "None," * (i+1)
                kwparams_expected += str(range(i+2, num_kwparams+1))[1:-1]
                print NICE_SPACE, "AreEqual(f%dParams%dKwparams(%s" % (num_params, num_kwparams, params),
                if num_params!=0:
                    print ",", 
                print kwparams, "),"
                print NICE_SPACE, "         ((%s), " % params_expected, "(%s))" % kwparams_expected, ")"
            print ""

    

#--AUTO GENERATED TEST CASES---------------------------------------------------
def test_args_plus_kwargs_optimizations():
    '''
    Because IronPython utilizes DLR site caching for function signatures,
    we must exhaustively cover all Python signatures with up to 14 param/keyword
    parameters.
    '''
    
    #--0 params with 0 keyword params--#
    def f0Params0Kwparams( ):
        ret_valP = ()
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f0Params0Kwparams( ),
             ((),  ()) )
    
    #--0 params with 1 keyword params--#
    def f0Params1Kwparams( kw1=1 ):
        ret_valP = ()
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params1Kwparams( ),
             ((),  (1,)) )
    
    AreEqual(f0Params1Kwparams( kw1=None ),
             ((),  (None,)) )

    #--0 params with 2 keyword params--#
    def f0Params2Kwparams( kw1=1, kw2=2 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params2Kwparams( ),
             ((),  (1, 2)) )
    
    AreEqual(f0Params2Kwparams( kw1=None ),
             ((),  (None,2)) )
    AreEqual(f0Params2Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,)) )

    #--0 params with 3 keyword params--#
    def f0Params3Kwparams( kw1=1, kw2=2, kw3=3 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params3Kwparams( ),
             ((),  (1, 2, 3)) )
    
    AreEqual(f0Params3Kwparams( kw1=None ),
             ((),  (None,2, 3)) )
    AreEqual(f0Params3Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3)) )
    AreEqual(f0Params3Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,)) )

    #--0 params with 4 keyword params--#
    def f0Params4Kwparams( kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params4Kwparams( ),
             ((),  (1, 2, 3, 4)) )
    
    AreEqual(f0Params4Kwparams( kw1=None ),
             ((),  (None,2, 3, 4)) )
    AreEqual(f0Params4Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4)) )
    AreEqual(f0Params4Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4)) )
    AreEqual(f0Params4Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,)) )

    #--0 params with 5 keyword params--#
    def f0Params5Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params5Kwparams( ),
             ((),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f0Params5Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5)) )
    AreEqual(f0Params5Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5)) )
    AreEqual(f0Params5Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5)) )
    AreEqual(f0Params5Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5)) )
    AreEqual(f0Params5Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,)) )

    #--0 params with 6 keyword params--#
    def f0Params6Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params6Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f0Params6Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f0Params6Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6)) )
    AreEqual(f0Params6Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6)) )
    AreEqual(f0Params6Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6)) )
    AreEqual(f0Params6Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6)) )
    AreEqual(f0Params6Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,)) )

    #--0 params with 7 keyword params--#
    def f0Params7Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params7Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f0Params7Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f0Params7Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f0Params7Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f0Params7Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f0Params7Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7)) )
    AreEqual(f0Params7Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7)) )
    AreEqual(f0Params7Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,)) )

    #--0 params with 8 keyword params--#
    def f0Params8Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params8Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f0Params8Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f0Params8Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f0Params8Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f0Params8Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f0Params8Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f0Params8Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f0Params8Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f0Params8Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((),  (None,None,None,None,None,None,None,None,)) )

    #--0 params with 9 keyword params--#
    def f0Params9Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params9Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f0Params9Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f0Params9Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((),  (None,None,None,None,None,None,None,None,None,)) )

    #--0 params with 10 keyword params--#
    def f0Params10Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params10Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f0Params10Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f0Params10Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--0 params with 11 keyword params--#
    def f0Params11Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params11Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f0Params11Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f0Params11Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--0 params with 12 keyword params--#
    def f0Params12Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params12Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f0Params12Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f0Params12Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--0 params with 13 keyword params--#
    def f0Params13Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params13Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f0Params13Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f0Params13Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--0 params with 14 keyword params--#
    def f0Params14Kwparams( kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ()
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f0Params14Kwparams( ),
             ((),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f0Params14Kwparams( kw1=None ),
             ((),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None ),
             ((),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None ),
             ((),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None ),
             ((),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f0Params14Kwparams( kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--1 params with 0 keyword params--#
    def f1Params0Kwparams( p1 ):
        ret_valP = ( p1 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f1Params0Kwparams(1 ),
             ((1,),  ()) )
    

    #--1 params with 1 keyword params--#
    def f1Params1Kwparams( p1, kw1=1 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params1Kwparams(1 ),
             ((1,),  (1,)) )
    
    AreEqual(f1Params1Kwparams(1 , kw1=None ),
             ((1,),  (None,)) )

    #--1 params with 2 keyword params--#
    def f1Params2Kwparams( p1, kw1=1, kw2=2 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params2Kwparams(1 ),
             ((1,),  (1, 2)) )
    
    AreEqual(f1Params2Kwparams(1 , kw1=None ),
             ((1,),  (None,2)) )
    AreEqual(f1Params2Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,)) )

    #--1 params with 3 keyword params--#
    def f1Params3Kwparams( p1, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params3Kwparams(1 ),
             ((1,),  (1, 2, 3)) )
    
    AreEqual(f1Params3Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3)) )
    AreEqual(f1Params3Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3)) )
    AreEqual(f1Params3Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,)) )

    #--1 params with 4 keyword params--#
    def f1Params4Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params4Kwparams(1 ),
             ((1,),  (1, 2, 3, 4)) )
    
    AreEqual(f1Params4Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4)) )
    AreEqual(f1Params4Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4)) )
    AreEqual(f1Params4Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4)) )
    AreEqual(f1Params4Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,)) )

    #--1 params with 5 keyword params--#
    def f1Params5Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params5Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f1Params5Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5)) )
    AreEqual(f1Params5Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5)) )
    AreEqual(f1Params5Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5)) )
    AreEqual(f1Params5Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5)) )
    AreEqual(f1Params5Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,)) )

    #--1 params with 6 keyword params--#
    def f1Params6Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params6Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f1Params6Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f1Params6Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6)) )
    AreEqual(f1Params6Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6)) )
    AreEqual(f1Params6Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6)) )
    AreEqual(f1Params6Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6)) )
    AreEqual(f1Params6Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,)) )

    #--1 params with 7 keyword params--#
    def f1Params7Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params7Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f1Params7Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f1Params7Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f1Params7Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f1Params7Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f1Params7Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7)) )
    AreEqual(f1Params7Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7)) )
    AreEqual(f1Params7Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,)) )

    #--1 params with 8 keyword params--#
    def f1Params8Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params8Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f1Params8Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f1Params8Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f1Params8Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f1Params8Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f1Params8Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f1Params8Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f1Params8Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f1Params8Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1,),  (None,None,None,None,None,None,None,None,)) )

    #--1 params with 9 keyword params--#
    def f1Params9Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params9Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f1Params9Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1,),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f1Params9Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,)) )

    #--1 params with 10 keyword params--#
    def f1Params10Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params10Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f1Params10Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1,),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f1Params10Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--1 params with 11 keyword params--#
    def f1Params11Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params11Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f1Params11Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1,),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f1Params11Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--1 params with 12 keyword params--#
    def f1Params12Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params12Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f1Params12Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1,),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f1Params12Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--1 params with 13 keyword params--#
    def f1Params13Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params13Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f1Params13Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1,),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f1Params13Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--1 params with 14 keyword params--#
    def f1Params14Kwparams( p1, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f1Params14Kwparams(1 ),
             ((1,),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f1Params14Kwparams(1 , kw1=None ),
             ((1,),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None ),
             ((1,),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None ),
             ((1,),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1,),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1,),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1,),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1,),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1,),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f1Params14Kwparams(1 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1,),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--2 params with 0 keyword params--#
    def f2Params0Kwparams( p1, p2 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f2Params0Kwparams(1, 2 ),
             ((1, 2),  ()) )
    

    #--2 params with 1 keyword params--#
    def f2Params1Kwparams( p1, p2, kw1=1 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params1Kwparams(1, 2 ),
             ((1, 2),  (1,)) )
    
    AreEqual(f2Params1Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,)) )

    #--2 params with 2 keyword params--#
    def f2Params2Kwparams( p1, p2, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params2Kwparams(1, 2 ),
             ((1, 2),  (1, 2)) )
    
    AreEqual(f2Params2Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2)) )
    AreEqual(f2Params2Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,)) )

    #--2 params with 3 keyword params--#
    def f2Params3Kwparams( p1, p2, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params3Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3)) )
    
    AreEqual(f2Params3Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3)) )
    AreEqual(f2Params3Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3)) )
    AreEqual(f2Params3Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,)) )

    #--2 params with 4 keyword params--#
    def f2Params4Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params4Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4)) )
    
    AreEqual(f2Params4Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4)) )
    AreEqual(f2Params4Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4)) )
    AreEqual(f2Params4Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4)) )
    AreEqual(f2Params4Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,)) )

    #--2 params with 5 keyword params--#
    def f2Params5Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params5Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f2Params5Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5)) )
    AreEqual(f2Params5Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5)) )
    AreEqual(f2Params5Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5)) )
    AreEqual(f2Params5Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5)) )
    AreEqual(f2Params5Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,)) )

    #--2 params with 6 keyword params--#
    def f2Params6Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params6Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f2Params6Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f2Params6Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6)) )
    AreEqual(f2Params6Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6)) )
    AreEqual(f2Params6Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6)) )
    AreEqual(f2Params6Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6)) )
    AreEqual(f2Params6Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,)) )

    #--2 params with 7 keyword params--#
    def f2Params7Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params7Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f2Params7Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f2Params7Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f2Params7Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f2Params7Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f2Params7Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7)) )
    AreEqual(f2Params7Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7)) )
    AreEqual(f2Params7Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,)) )

    #--2 params with 8 keyword params--#
    def f2Params8Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params8Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f2Params8Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,)) )

    #--2 params with 9 keyword params--#
    def f2Params9Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params9Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f2Params9Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,)) )

    #--2 params with 10 keyword params--#
    def f2Params10Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params10Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f2Params10Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--2 params with 11 keyword params--#
    def f2Params11Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params11Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f2Params11Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--2 params with 12 keyword params--#
    def f2Params12Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params12Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f2Params12Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--2 params with 13 keyword params--#
    def f2Params13Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params13Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f2Params13Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--2 params with 14 keyword params--#
    def f2Params14Kwparams( p1, p2, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f2Params14Kwparams(1, 2 ),
             ((1, 2),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None ),
             ((1, 2),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None ),
             ((1, 2),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None ),
             ((1, 2),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f2Params14Kwparams(1, 2 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--3 params with 0 keyword params--#
    def f3Params0Kwparams( p1, p2, p3 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f3Params0Kwparams(1, 2, 3 ),
             ((1, 2, 3),  ()) )
    

    #--3 params with 1 keyword params--#
    def f3Params1Kwparams( p1, p2, p3, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params1Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1,)) )
    
    AreEqual(f3Params1Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,)) )

    #--3 params with 2 keyword params--#
    def f3Params2Kwparams( p1, p2, p3, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params2Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2)) )
    
    AreEqual(f3Params2Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2)) )
    AreEqual(f3Params2Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,)) )

    #--3 params with 3 keyword params--#
    def f3Params3Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params3Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3)) )
    
    AreEqual(f3Params3Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3)) )
    AreEqual(f3Params3Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3)) )
    AreEqual(f3Params3Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,)) )

    #--3 params with 4 keyword params--#
    def f3Params4Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params4Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4)) )
    
    AreEqual(f3Params4Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4)) )
    AreEqual(f3Params4Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4)) )
    AreEqual(f3Params4Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4)) )
    AreEqual(f3Params4Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,)) )

    #--3 params with 5 keyword params--#
    def f3Params5Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params5Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f3Params5Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5)) )
    AreEqual(f3Params5Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5)) )
    AreEqual(f3Params5Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5)) )
    AreEqual(f3Params5Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5)) )
    AreEqual(f3Params5Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,)) )

    #--3 params with 6 keyword params--#
    def f3Params6Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params6Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f3Params6Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f3Params6Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6)) )
    AreEqual(f3Params6Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6)) )
    AreEqual(f3Params6Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6)) )
    AreEqual(f3Params6Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6)) )
    AreEqual(f3Params6Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,)) )

    #--3 params with 7 keyword params--#
    def f3Params7Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params7Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f3Params7Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f3Params7Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f3Params7Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f3Params7Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f3Params7Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7)) )
    AreEqual(f3Params7Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7)) )
    AreEqual(f3Params7Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,)) )

    #--3 params with 8 keyword params--#
    def f3Params8Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params8Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f3Params8Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,)) )

    #--3 params with 9 keyword params--#
    def f3Params9Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params9Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f3Params9Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,)) )

    #--3 params with 10 keyword params--#
    def f3Params10Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params10Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f3Params10Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--3 params with 11 keyword params--#
    def f3Params11Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params11Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f3Params11Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--3 params with 12 keyword params--#
    def f3Params12Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params12Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f3Params12Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--3 params with 13 keyword params--#
    def f3Params13Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params13Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f3Params13Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--3 params with 14 keyword params--#
    def f3Params14Kwparams( p1, p2, p3, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f3Params14Kwparams(1, 2, 3 ),
             ((1, 2, 3),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None ),
             ((1, 2, 3),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None ),
             ((1, 2, 3),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f3Params14Kwparams(1, 2, 3 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--4 params with 0 keyword params--#
    def f4Params0Kwparams( p1, p2, p3, p4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f4Params0Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  ()) )
    

    #--4 params with 1 keyword params--#
    def f4Params1Kwparams( p1, p2, p3, p4, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params1Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1,)) )
    
    AreEqual(f4Params1Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,)) )

    #--4 params with 2 keyword params--#
    def f4Params2Kwparams( p1, p2, p3, p4, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params2Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2)) )
    
    AreEqual(f4Params2Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2)) )
    AreEqual(f4Params2Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,)) )

    #--4 params with 3 keyword params--#
    def f4Params3Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params3Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3)) )
    
    AreEqual(f4Params3Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3)) )
    AreEqual(f4Params3Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3)) )
    AreEqual(f4Params3Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,)) )

    #--4 params with 4 keyword params--#
    def f4Params4Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params4Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4)) )
    
    AreEqual(f4Params4Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4)) )
    AreEqual(f4Params4Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4)) )
    AreEqual(f4Params4Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4)) )
    AreEqual(f4Params4Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,)) )

    #--4 params with 5 keyword params--#
    def f4Params5Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params5Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f4Params5Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5)) )
    AreEqual(f4Params5Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5)) )
    AreEqual(f4Params5Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5)) )
    AreEqual(f4Params5Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5)) )
    AreEqual(f4Params5Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,)) )

    #--4 params with 6 keyword params--#
    def f4Params6Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params6Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f4Params6Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f4Params6Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6)) )
    AreEqual(f4Params6Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6)) )
    AreEqual(f4Params6Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6)) )
    AreEqual(f4Params6Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6)) )
    AreEqual(f4Params6Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,)) )

    #--4 params with 7 keyword params--#
    def f4Params7Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params7Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f4Params7Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f4Params7Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f4Params7Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f4Params7Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f4Params7Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7)) )
    AreEqual(f4Params7Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7)) )
    AreEqual(f4Params7Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,)) )

    #--4 params with 8 keyword params--#
    def f4Params8Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params8Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f4Params8Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,)) )

    #--4 params with 9 keyword params--#
    def f4Params9Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params9Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f4Params9Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,)) )

    #--4 params with 10 keyword params--#
    def f4Params10Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params10Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f4Params10Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--4 params with 11 keyword params--#
    def f4Params11Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params11Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f4Params11Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--4 params with 12 keyword params--#
    def f4Params12Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params12Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f4Params12Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--4 params with 13 keyword params--#
    def f4Params13Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params13Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f4Params13Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--4 params with 14 keyword params--#
    def f4Params14Kwparams( p1, p2, p3, p4, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f4Params14Kwparams(1, 2, 3, 4 ),
             ((1, 2, 3, 4),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None ),
             ((1, 2, 3, 4),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None ),
             ((1, 2, 3, 4),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f4Params14Kwparams(1, 2, 3, 4 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--5 params with 0 keyword params--#
    def f5Params0Kwparams( p1, p2, p3, p4, p5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f5Params0Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  ()) )
    

    #--5 params with 1 keyword params--#
    def f5Params1Kwparams( p1, p2, p3, p4, p5, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params1Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1,)) )
    
    AreEqual(f5Params1Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,)) )

    #--5 params with 2 keyword params--#
    def f5Params2Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params2Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2)) )
    
    AreEqual(f5Params2Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2)) )
    AreEqual(f5Params2Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,)) )

    #--5 params with 3 keyword params--#
    def f5Params3Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params3Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3)) )
    
    AreEqual(f5Params3Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3)) )
    AreEqual(f5Params3Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3)) )
    AreEqual(f5Params3Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,)) )

    #--5 params with 4 keyword params--#
    def f5Params4Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params4Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4)) )
    
    AreEqual(f5Params4Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4)) )
    AreEqual(f5Params4Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4)) )
    AreEqual(f5Params4Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4)) )
    AreEqual(f5Params4Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,)) )

    #--5 params with 5 keyword params--#
    def f5Params5Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params5Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f5Params5Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5)) )
    AreEqual(f5Params5Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5)) )
    AreEqual(f5Params5Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5)) )
    AreEqual(f5Params5Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5)) )
    AreEqual(f5Params5Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,)) )

    #--5 params with 6 keyword params--#
    def f5Params6Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params6Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f5Params6Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f5Params6Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6)) )
    AreEqual(f5Params6Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6)) )
    AreEqual(f5Params6Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6)) )
    AreEqual(f5Params6Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6)) )
    AreEqual(f5Params6Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,)) )

    #--5 params with 7 keyword params--#
    def f5Params7Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7)) )
    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7)) )
    AreEqual(f5Params7Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,)) )

    #--5 params with 8 keyword params--#
    def f5Params8Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f5Params8Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,)) )

    #--5 params with 9 keyword params--#
    def f5Params9Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f5Params9Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,)) )

    #--5 params with 10 keyword params--#
    def f5Params10Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f5Params10Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--5 params with 11 keyword params--#
    def f5Params11Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f5Params11Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--5 params with 12 keyword params--#
    def f5Params12Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f5Params12Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--5 params with 13 keyword params--#
    def f5Params13Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f5Params13Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--5 params with 14 keyword params--#
    def f5Params14Kwparams( p1, p2, p3, p4, p5, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 ),
             ((1, 2, 3, 4, 5),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None ),
             ((1, 2, 3, 4, 5),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f5Params14Kwparams(1, 2, 3, 4, 5 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--6 params with 0 keyword params--#
    def f6Params0Kwparams( p1, p2, p3, p4, p5, p6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f6Params0Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  ()) )
    

    #--6 params with 1 keyword params--#
    def f6Params1Kwparams( p1, p2, p3, p4, p5, p6, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params1Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1,)) )
    
    AreEqual(f6Params1Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,)) )

    #--6 params with 2 keyword params--#
    def f6Params2Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params2Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2)) )
    
    AreEqual(f6Params2Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2)) )
    AreEqual(f6Params2Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,)) )

    #--6 params with 3 keyword params--#
    def f6Params3Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params3Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3)) )
    
    AreEqual(f6Params3Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3)) )
    AreEqual(f6Params3Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3)) )
    AreEqual(f6Params3Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,)) )

    #--6 params with 4 keyword params--#
    def f6Params4Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params4Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4)) )
    
    AreEqual(f6Params4Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4)) )
    AreEqual(f6Params4Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4)) )
    AreEqual(f6Params4Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4)) )
    AreEqual(f6Params4Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,)) )

    #--6 params with 5 keyword params--#
    def f6Params5Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params5Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f6Params5Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5)) )
    AreEqual(f6Params5Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5)) )
    AreEqual(f6Params5Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5)) )
    AreEqual(f6Params5Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5)) )
    AreEqual(f6Params5Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,)) )

    #--6 params with 6 keyword params--#
    def f6Params6Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params6Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f6Params6Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f6Params6Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6)) )
    AreEqual(f6Params6Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6)) )
    AreEqual(f6Params6Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6)) )
    AreEqual(f6Params6Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6)) )
    AreEqual(f6Params6Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,)) )

    #--6 params with 7 keyword params--#
    def f6Params7Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7)) )
    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7)) )
    AreEqual(f6Params7Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,)) )

    #--6 params with 8 keyword params--#
    def f6Params8Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f6Params8Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,)) )

    #--6 params with 9 keyword params--#
    def f6Params9Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f6Params9Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,)) )

    #--6 params with 10 keyword params--#
    def f6Params10Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f6Params10Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--6 params with 11 keyword params--#
    def f6Params11Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f6Params11Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--6 params with 12 keyword params--#
    def f6Params12Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f6Params12Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--6 params with 13 keyword params--#
    def f6Params13Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f6Params13Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--6 params with 14 keyword params--#
    def f6Params14Kwparams( p1, p2, p3, p4, p5, p6, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 ),
             ((1, 2, 3, 4, 5, 6),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None ),
             ((1, 2, 3, 4, 5, 6),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f6Params14Kwparams(1, 2, 3, 4, 5, 6 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--7 params with 0 keyword params--#
    def f7Params0Kwparams( p1, p2, p3, p4, p5, p6, p7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f7Params0Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  ()) )
    

    #--7 params with 1 keyword params--#
    def f7Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params1Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1,)) )
    
    AreEqual(f7Params1Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,)) )

    #--7 params with 2 keyword params--#
    def f7Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params2Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2)) )
    
    AreEqual(f7Params2Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2)) )
    AreEqual(f7Params2Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,)) )

    #--7 params with 3 keyword params--#
    def f7Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params3Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3)) )
    
    AreEqual(f7Params3Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3)) )
    AreEqual(f7Params3Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3)) )
    AreEqual(f7Params3Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,)) )

    #--7 params with 4 keyword params--#
    def f7Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params4Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4)) )
    
    AreEqual(f7Params4Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4)) )
    AreEqual(f7Params4Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4)) )
    AreEqual(f7Params4Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4)) )
    AreEqual(f7Params4Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,)) )

    #--7 params with 5 keyword params--#
    def f7Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params5Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f7Params5Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5)) )
    AreEqual(f7Params5Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5)) )
    AreEqual(f7Params5Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5)) )
    AreEqual(f7Params5Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5)) )
    AreEqual(f7Params5Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,)) )

    #--7 params with 6 keyword params--#
    def f7Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params6Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f7Params6Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f7Params6Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6)) )
    AreEqual(f7Params6Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6)) )
    AreEqual(f7Params6Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6)) )
    AreEqual(f7Params6Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6)) )
    AreEqual(f7Params6Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,)) )

    #--7 params with 7 keyword params--#
    def f7Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7)) )
    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7)) )
    AreEqual(f7Params7Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,)) )

    #--7 params with 8 keyword params--#
    def f7Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f7Params8Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,)) )

    #--7 params with 9 keyword params--#
    def f7Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f7Params9Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,)) )

    #--7 params with 10 keyword params--#
    def f7Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f7Params10Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--7 params with 11 keyword params--#
    def f7Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f7Params11Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--7 params with 12 keyword params--#
    def f7Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f7Params12Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--7 params with 13 keyword params--#
    def f7Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f7Params13Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--7 params with 14 keyword params--#
    def f7Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 ),
             ((1, 2, 3, 4, 5, 6, 7),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f7Params14Kwparams(1, 2, 3, 4, 5, 6, 7 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--8 params with 0 keyword params--#
    def f8Params0Kwparams( p1, p2, p3, p4, p5, p6, p7, p8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f8Params0Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  ()) )
    

    #--8 params with 1 keyword params--#
    def f8Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1,)) )
    
    AreEqual(f8Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,)) )

    #--8 params with 2 keyword params--#
    def f8Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2)) )
    
    AreEqual(f8Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2)) )
    AreEqual(f8Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,)) )

    #--8 params with 3 keyword params--#
    def f8Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3)) )
    
    AreEqual(f8Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3)) )
    AreEqual(f8Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3)) )
    AreEqual(f8Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,)) )

    #--8 params with 4 keyword params--#
    def f8Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4)) )
    
    AreEqual(f8Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4)) )
    AreEqual(f8Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4)) )
    AreEqual(f8Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4)) )
    AreEqual(f8Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,)) )

    #--8 params with 5 keyword params--#
    def f8Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f8Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5)) )
    AreEqual(f8Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5)) )
    AreEqual(f8Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5)) )
    AreEqual(f8Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5)) )
    AreEqual(f8Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,)) )

    #--8 params with 6 keyword params--#
    def f8Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f8Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f8Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6)) )
    AreEqual(f8Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6)) )
    AreEqual(f8Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6)) )
    AreEqual(f8Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6)) )
    AreEqual(f8Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,)) )

    #--8 params with 7 keyword params--#
    def f8Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7)) )
    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7)) )
    AreEqual(f8Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,)) )

    #--8 params with 8 keyword params--#
    def f8Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f8Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,)) )

    #--8 params with 9 keyword params--#
    def f8Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f8Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,)) )

    #--8 params with 10 keyword params--#
    def f8Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f8Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--8 params with 11 keyword params--#
    def f8Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f8Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--8 params with 12 keyword params--#
    def f8Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f8Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--8 params with 13 keyword params--#
    def f8Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f8Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--8 params with 14 keyword params--#
    def f8Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f8Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--9 params with 0 keyword params--#
    def f9Params0Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f9Params0Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  ()) )
    

    #--9 params with 1 keyword params--#
    def f9Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1,)) )
    
    AreEqual(f9Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,)) )

    #--9 params with 2 keyword params--#
    def f9Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2)) )
    
    AreEqual(f9Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2)) )
    AreEqual(f9Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,)) )

    #--9 params with 3 keyword params--#
    def f9Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3)) )
    
    AreEqual(f9Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3)) )
    AreEqual(f9Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3)) )
    AreEqual(f9Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,)) )

    #--9 params with 4 keyword params--#
    def f9Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4)) )
    
    AreEqual(f9Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4)) )
    AreEqual(f9Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4)) )
    AreEqual(f9Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4)) )
    AreEqual(f9Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,)) )

    #--9 params with 5 keyword params--#
    def f9Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f9Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5)) )
    AreEqual(f9Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5)) )
    AreEqual(f9Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5)) )
    AreEqual(f9Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5)) )
    AreEqual(f9Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,)) )

    #--9 params with 6 keyword params--#
    def f9Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f9Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f9Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6)) )
    AreEqual(f9Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6)) )
    AreEqual(f9Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6)) )
    AreEqual(f9Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6)) )
    AreEqual(f9Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,)) )

    #--9 params with 7 keyword params--#
    def f9Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7)) )
    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7)) )
    AreEqual(f9Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,)) )

    #--9 params with 8 keyword params--#
    def f9Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f9Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,)) )

    #--9 params with 9 keyword params--#
    def f9Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f9Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,)) )

    #--9 params with 10 keyword params--#
    def f9Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f9Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--9 params with 11 keyword params--#
    def f9Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f9Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--9 params with 12 keyword params--#
    def f9Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f9Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--9 params with 13 keyword params--#
    def f9Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f9Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--9 params with 14 keyword params--#
    def f9Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f9Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--10 params with 0 keyword params--#
    def f10Params0Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f10Params0Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  ()) )
    

    #--10 params with 1 keyword params--#
    def f10Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1,)) )
    
    AreEqual(f10Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,)) )

    #--10 params with 2 keyword params--#
    def f10Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2)) )
    
    AreEqual(f10Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2)) )
    AreEqual(f10Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,)) )

    #--10 params with 3 keyword params--#
    def f10Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3)) )
    
    AreEqual(f10Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3)) )
    AreEqual(f10Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3)) )
    AreEqual(f10Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,)) )

    #--10 params with 4 keyword params--#
    def f10Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4)) )
    
    AreEqual(f10Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4)) )
    AreEqual(f10Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4)) )
    AreEqual(f10Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4)) )
    AreEqual(f10Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,)) )

    #--10 params with 5 keyword params--#
    def f10Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f10Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5)) )
    AreEqual(f10Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5)) )
    AreEqual(f10Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5)) )
    AreEqual(f10Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5)) )
    AreEqual(f10Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,)) )

    #--10 params with 6 keyword params--#
    def f10Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f10Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f10Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6)) )
    AreEqual(f10Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6)) )
    AreEqual(f10Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6)) )
    AreEqual(f10Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6)) )
    AreEqual(f10Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,)) )

    #--10 params with 7 keyword params--#
    def f10Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7)) )
    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7)) )
    AreEqual(f10Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,)) )

    #--10 params with 8 keyword params--#
    def f10Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f10Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,)) )

    #--10 params with 9 keyword params--#
    def f10Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f10Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,)) )

    #--10 params with 10 keyword params--#
    def f10Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f10Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--10 params with 11 keyword params--#
    def f10Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f10Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--10 params with 12 keyword params--#
    def f10Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f10Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--10 params with 13 keyword params--#
    def f10Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f10Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--10 params with 14 keyword params--#
    def f10Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f10Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--11 params with 0 keyword params--#
    def f11Params0Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f11Params0Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  ()) )
    

    #--11 params with 1 keyword params--#
    def f11Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1,)) )
    
    AreEqual(f11Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,)) )

    #--11 params with 2 keyword params--#
    def f11Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2)) )
    
    AreEqual(f11Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2)) )
    AreEqual(f11Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,)) )

    #--11 params with 3 keyword params--#
    def f11Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3)) )
    
    AreEqual(f11Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3)) )
    AreEqual(f11Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3)) )
    AreEqual(f11Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,)) )

    #--11 params with 4 keyword params--#
    def f11Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4)) )
    
    AreEqual(f11Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4)) )
    AreEqual(f11Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4)) )
    AreEqual(f11Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4)) )
    AreEqual(f11Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,)) )

    #--11 params with 5 keyword params--#
    def f11Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f11Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5)) )
    AreEqual(f11Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5)) )
    AreEqual(f11Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5)) )
    AreEqual(f11Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5)) )
    AreEqual(f11Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,)) )

    #--11 params with 6 keyword params--#
    def f11Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f11Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f11Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6)) )
    AreEqual(f11Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6)) )
    AreEqual(f11Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6)) )
    AreEqual(f11Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6)) )
    AreEqual(f11Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,)) )

    #--11 params with 7 keyword params--#
    def f11Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7)) )
    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7)) )
    AreEqual(f11Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,)) )

    #--11 params with 8 keyword params--#
    def f11Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f11Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,)) )

    #--11 params with 9 keyword params--#
    def f11Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f11Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,)) )

    #--11 params with 10 keyword params--#
    def f11Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f11Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--11 params with 11 keyword params--#
    def f11Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f11Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--11 params with 12 keyword params--#
    def f11Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f11Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--11 params with 13 keyword params--#
    def f11Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f11Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--11 params with 14 keyword params--#
    def f11Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f11Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--12 params with 0 keyword params--#
    def f12Params0Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f12Params0Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  ()) )
    

    #--12 params with 1 keyword params--#
    def f12Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1,)) )
    
    AreEqual(f12Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,)) )

    #--12 params with 2 keyword params--#
    def f12Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2)) )
    
    AreEqual(f12Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2)) )
    AreEqual(f12Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,)) )

    #--12 params with 3 keyword params--#
    def f12Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3)) )
    
    AreEqual(f12Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3)) )
    AreEqual(f12Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3)) )
    AreEqual(f12Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,)) )

    #--12 params with 4 keyword params--#
    def f12Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4)) )
    
    AreEqual(f12Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4)) )
    AreEqual(f12Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4)) )
    AreEqual(f12Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4)) )
    AreEqual(f12Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,)) )

    #--12 params with 5 keyword params--#
    def f12Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f12Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5)) )
    AreEqual(f12Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5)) )
    AreEqual(f12Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5)) )
    AreEqual(f12Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5)) )
    AreEqual(f12Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,)) )

    #--12 params with 6 keyword params--#
    def f12Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f12Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f12Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6)) )
    AreEqual(f12Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6)) )
    AreEqual(f12Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6)) )
    AreEqual(f12Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6)) )
    AreEqual(f12Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,)) )

    #--12 params with 7 keyword params--#
    def f12Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7)) )
    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7)) )
    AreEqual(f12Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,)) )

    #--12 params with 8 keyword params--#
    def f12Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f12Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,)) )

    #--12 params with 9 keyword params--#
    def f12Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f12Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,)) )

    #--12 params with 10 keyword params--#
    def f12Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f12Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--12 params with 11 keyword params--#
    def f12Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f12Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--12 params with 12 keyword params--#
    def f12Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f12Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--12 params with 13 keyword params--#
    def f12Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f12Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--12 params with 14 keyword params--#
    def f12Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f12Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--13 params with 0 keyword params--#
    def f13Params0Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f13Params0Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  ()) )
    

    #--13 params with 1 keyword params--#
    def f13Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1,)) )
    
    AreEqual(f13Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,)) )

    #--13 params with 2 keyword params--#
    def f13Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2)) )
    
    AreEqual(f13Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2)) )
    AreEqual(f13Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,)) )

    #--13 params with 3 keyword params--#
    def f13Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3)) )
    
    AreEqual(f13Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3)) )
    AreEqual(f13Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3)) )
    AreEqual(f13Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,)) )

    #--13 params with 4 keyword params--#
    def f13Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4)) )
    
    AreEqual(f13Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4)) )
    AreEqual(f13Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4)) )
    AreEqual(f13Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4)) )
    AreEqual(f13Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,)) )

    #--13 params with 5 keyword params--#
    def f13Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f13Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5)) )
    AreEqual(f13Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5)) )
    AreEqual(f13Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5)) )
    AreEqual(f13Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5)) )
    AreEqual(f13Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,)) )

    #--13 params with 6 keyword params--#
    def f13Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f13Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f13Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6)) )
    AreEqual(f13Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6)) )
    AreEqual(f13Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6)) )
    AreEqual(f13Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6)) )
    AreEqual(f13Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,)) )

    #--13 params with 7 keyword params--#
    def f13Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7)) )
    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7)) )
    AreEqual(f13Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,)) )

    #--13 params with 8 keyword params--#
    def f13Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f13Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,)) )

    #--13 params with 9 keyword params--#
    def f13Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f13Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,)) )

    #--13 params with 10 keyword params--#
    def f13Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f13Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--13 params with 11 keyword params--#
    def f13Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f13Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--13 params with 12 keyword params--#
    def f13Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f13Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--13 params with 13 keyword params--#
    def f13Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f13Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--13 params with 14 keyword params--#
    def f13Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f13Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--14 params with 0 keyword params--#
    def f14Params0Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ()
        return ret_valP, ret_valKW

    AreEqual(f14Params0Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  ()) )
    

    #--14 params with 1 keyword params--#
    def f14Params1Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1,)) )
    
    AreEqual(f14Params1Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,)) )

    #--14 params with 2 keyword params--#
    def f14Params2Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2)) )
    
    AreEqual(f14Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2)) )
    AreEqual(f14Params2Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,)) )

    #--14 params with 3 keyword params--#
    def f14Params3Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3)) )
    
    AreEqual(f14Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3)) )
    AreEqual(f14Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3)) )
    AreEqual(f14Params3Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,)) )

    #--14 params with 4 keyword params--#
    def f14Params4Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4)) )
    
    AreEqual(f14Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4)) )
    AreEqual(f14Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4)) )
    AreEqual(f14Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4)) )
    AreEqual(f14Params4Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,)) )

    #--14 params with 5 keyword params--#
    def f14Params5Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5)) )
    
    AreEqual(f14Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5)) )
    AreEqual(f14Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5)) )
    AreEqual(f14Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5)) )
    AreEqual(f14Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5)) )
    AreEqual(f14Params5Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,)) )

    #--14 params with 6 keyword params--#
    def f14Params6Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6)) )
    
    AreEqual(f14Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6)) )
    AreEqual(f14Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6)) )
    AreEqual(f14Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6)) )
    AreEqual(f14Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6)) )
    AreEqual(f14Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6)) )
    AreEqual(f14Params6Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,)) )

    #--14 params with 7 keyword params--#
    def f14Params7Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7)) )
    
    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7)) )
    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7)) )
    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7)) )
    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7)) )
    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7)) )
    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7)) )
    AreEqual(f14Params7Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,)) )

    #--14 params with 8 keyword params--#
    def f14Params8Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7, 8)) )
    
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7, 8)) )
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7, 8)) )
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7, 8)) )
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7, 8)) )
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7, 8)) )
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7, 8)) )
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,8)) )
    AreEqual(f14Params8Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,)) )

    #--14 params with 9 keyword params--#
    def f14Params9Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7, 8, 9)) )
    
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7, 8, 9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7, 8, 9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7, 8, 9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7, 8, 9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7, 8, 9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,8, 9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,9)) )
    AreEqual(f14Params9Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,)) )

    #--14 params with 10 keyword params--#
    def f14Params10Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7, 8, 9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7, 8, 9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7, 8, 9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7, 8, 9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,8, 9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,9, 10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,10)) )
    AreEqual(f14Params10Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,)) )

    #--14 params with 11 keyword params--#
    def f14Params11Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7, 8, 9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7, 8, 9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,8, 9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,9, 10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,10, 11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,11)) )
    AreEqual(f14Params11Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,)) )

    #--14 params with 12 keyword params--#
    def f14Params12Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,9, 10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,10, 11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,11, 12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,12)) )
    AreEqual(f14Params12Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--14 params with 13 keyword params--#
    def f14Params13Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,12, 13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,None,13)) )
    AreEqual(f14Params13Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    #--14 params with 14 keyword params--#
    def f14Params14Kwparams( p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, kw1=1, kw2=2, kw3=3, kw4=4, kw5=5, kw6=6, kw7=7, kw8=8, kw9=9, kw10=10, kw11=11, kw12=12, kw13=13, kw14=14 ):
        ret_valP = ( p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9 , p10 , p11 , p12 , p13 , p14 , )
        ret_valKW = ( kw1 , kw2 , kw3 , kw4 , kw5 , kw6 , kw7 , kw8 , kw9 , kw10 , kw11 , kw12 , kw13 , kw14 , )
        return ret_valP, ret_valKW

    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,6, 7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,7, 8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,8, 9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,9, 10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,10, 11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,11, 12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,12, 13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,None,13, 14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,None,None,14)) )
    AreEqual(f14Params14Kwparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , kw1=None, kw2=None, kw3=None, kw4=None, kw5=None, kw6=None, kw7=None, kw8=None, kw9=None, kw10=None, kw11=None, kw12=None, kw13=None, kw14=None ),
             ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),  (None,None,None,None,None,None,None,None,None,None,None,None,None,None,)) )

    
#--MAIN------------------------------------------------------------------------
run_test(__name__)
