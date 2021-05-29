from src.lib.TestSpec import Spec
from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
import libraries

testspecs = [Spec(
        repo="pyGPGO",
        filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_GPGO_mcmc",
        params=[
            Param(
                name="niter",
                param_line=30,
                param_col=56,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[1, 100],
                steps=1
            ),
            Param(
                name="max_iter",
                param_line=34,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=36,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(res['x'], 0.75, atol=0.05)",
                args=[]
            )
        ],
        branchname="before_1c718d7f2bdb95d407b27412b25471c762355832"

    )]