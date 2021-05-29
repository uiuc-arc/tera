from src.lib.TestSpec import Spec
from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
import libraries

testspecs = [Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snpe_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snpe_on_linearGaussian[2-gaussian]",
        params=[
            Param(
                name="num_samples",
                param_line=42,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=73,
                param_col=38,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ],
        branchname="before_86d9b07238f5a0176638fecdd5622694d92f2962"
    )]