from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
from src.lib.TestSpec import Spec
import libraries

testspecs = [Spec(
    repo="pyro",
    filename="{0}/projects/pyro/tests/infer/test_predictive.py".format(
        libraries.PROJECT_DIR),
    classname="none",
    testname="test_posterior_predictive_svi_manual_guide[True]",
    params=[
        Param(
            name="iterations",
            param_line=45,
            param_col=19,
            param_type=ParamType.ITER,
            default_val=1000,
            value_range=[100, 1000]
        ),
        Param(
            name="num_samples",
            param_line=47,
            param_col=75,
            param_type=ParamType.ITER,
            default_val=10000,
            value_range=[100, 10000]
        ),

    ],
    assertions=[

        AssertSpec(
            test=Test(testname="none",
                      classname="none",
                      filename="{0}/projects/pyro/tests/infer/test_predictive.py".format(
                          libraries.PROJECT_DIR)
                      ),
            line=50,
            col_offset=-1,
            assert_type=AssertType.ASSERT_ALLCLOSE,
            assert_string="assert_close(marginal_return_vals.mean(dim=0), torch.ones(5) * 700, rtol=0.05)",
            args=[]
        )
    ],
    branchname="before_f9dee1e2cd494a2c473b09d9ffb6098ab16dc105"
),
    Spec(
    repo="pyro",
    filename="{0}/projects/pyro/tests/infer/test_predictive.py".format(
        libraries.PROJECT_DIR),
    classname="none",
    testname="test_posterior_predictive_svi_manual_guide[False]",
    params=[
        Param(
            name="iterations",
            param_line=45,
            param_col=19,
            param_type=ParamType.ITER,
            default_val=1000,
            value_range=[100, 1000]
        ),
        Param(
            name="num_samples",
            param_line=47,
            param_col=75,
            param_type=ParamType.ITER,
            default_val=10000,
            value_range=[100, 10000]
        ),

    ],
    assertions=[

        AssertSpec(
            test=Test(testname="none",
                      classname="none",
                      filename="{0}/projects/pyro/tests/infer/test_predictive.py".format(
                          libraries.PROJECT_DIR)
                      ),
            line=50,
            col_offset=-1,
            assert_type=AssertType.ASSERT_ALLCLOSE,
            assert_string="assert_close(marginal_return_vals.mean(dim=0), torch.ones(5) * 700, rtol=0.05)",
            args=[]
        )
    ],
    branchname="before_f9dee1e2cd494a2c473b09d9ffb6098ab16dc105"
)]
