from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
from src.lib.TestSpec import Spec
import libraries

testspecs = [Spec(
    repo="ml-agents",
    filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/torch/test_attention.py".format(
        libraries.PROJECT_DIR),
    classname="none",
    testname="test_simple_transformer_training",
    params=[
        Param(
            name="lr",
            param_line=128,
            param_col=72,
            param_type=ParamType.LR,
            default_val=0.001,
            value_range=[1e-5, 1]
        ),
        Param(
            name="batch_size",
            param_line=130,
            param_col=17,
            param_type=ParamType.CHAINS,
            default_val=200,
            value_range=[4, 8, 32, 64, 128, 200, 256, 512, 1024]
        ),
        Param(
            name="iterations",
            param_line=133,
            param_col=19,
            param_type=ParamType.ITER,
            default_val=100,
            value_range=[10, 250]
        ),

    ],
    assertions=[

        AssertSpec(
            test=Test(testname="none",
                      classname="none",
                      filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/torch/test_attention.py".format(
                          libraries.PROJECT_DIR)
                      ),
            line=162,
            col_offset=-1,
            assert_type=AssertType.ASSERT,
            assert_string="assert error.item() < 0.3",
            args=[]
        )
    ],
    branchname="before_3f4b2b59cff8038bc6f25550e39296e2cc8695cb"
)]
